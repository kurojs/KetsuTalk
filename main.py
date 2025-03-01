import speech_recognition as sr
import subprocess
import json
import os
import requests
from pydub import AudioSegment
from pydub.playback import play
from translate import Translator
import keyboard

OLLAMA_MODEL = "phi3"
OLLAMA_PROMPT = "You are a native Japanese teacher who is teaching Japanese. Please speak only in Japanese and explain in Japanese. Please do not use other languages."
VOICEVOX_SPEAKER_ID = 61  # Change this based on the speaker ID in VoiceVox
TRANSLATION_LIMIT = 500  

translator = Translator(to_lang="en")
translator_ja_en = Translator(from_lang="ja", to_lang="en")

def ollama_response(prompt):
    try:
        process = subprocess.Popen(['ollama', 'run', OLLAMA_MODEL], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
        stdout, stderr = process.communicate(input=prompt)
        if process.returncode == 0:
            return stdout.strip()
        else:
            print(f"Error running Ollama: {stderr}")
            return ""
    except Exception as e:
        print(f"Connection error with Ollama: {e}")
        return ""

# Text to speech function using VoiceVox
def japanese_text_to_speech(text, speaker_id=VOICEVOX_SPEAKER_ID):
    url = f"http://localhost:50021/audio_query?text={text}&speaker={speaker_id}"
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        audio_query = response.json()
        
        synthesis_url = f"http://localhost:50021/synthesis?speaker={speaker_id}"
        synthesis_response = requests.post(synthesis_url, headers=headers, json=audio_query)
        synthesis_response.raise_for_status()
        
        audio_path = "output_jp.wav"
        with open(audio_path, "wb") as audio_file:
            audio_file.write(synthesis_response.content)
        return audio_path
    except requests.exceptions.RequestException as e:
        print(f"VoiceVox connection error: {e}")
        return ""

# Speech recognition function
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Press 'v' to start talking or 'e' to write the message...")
        while True:
            if keyboard.is_pressed('v'):
                print("Listening... Press 'b' to stop.")
                audio = r.listen(source)
                while not keyboard.is_pressed('b'):
                    pass
                try:
                    text = r.recognize_google(audio, language="ja-JP")
                    print(f"You said: {text}")
                    return text
                except sr.UnknownValueError:
                    print("I couldn't understand what you said.")
                    return ""
                except sr.RequestError as e:
                    print(f"Error requesting Google Speech Recognition results; {e}")
                    return ""
            elif keyboard.is_pressed('e'):
                text = input("Write your message: ")
                print(f"You said: {text}")
                return text

def split_text(text, limit):
    return [text[i:i+limit] for i in range(0, len(text), limit)]

def main():
    print("Japanese immersive environment started. Press 'v' to start speaking and 'b' to stop, or 'e' to type the message.")
    while True:
        user_input = recognize_speech()
        if user_input:
            translation = translator_ja_en.translate(user_input)
            print(f"You said (translation): {translation}")

            confirm = input("Type 'c' to confirm or 'r' to listen again: ").strip().lower()
            if confirm == 'c':
                response = ollama_response(f"{OLLAMA_PROMPT}\n{user_input}")
                if response:
                    response_parts = split_text(response, TRANSLATION_LIMIT)
                    for part in response_parts:
                        response_translation = translator_ja_en.translate(part)
                        print(f"Answer (Japanese): {part}")
                        print(f"Answer (translation): {response_translation}")

                        audio_path = japanese_text_to_speech(part, speaker_id=VOICEVOX_SPEAKER_ID)
                        if audio_path:
                            audio = AudioSegment.from_file(audio_path)
                            play(audio)
                            os.remove(audio_path)
                else:
                    print("No response was obtained.")
            elif confirm == 'r':
                print("Listening again...")

if __name__ == "__main__":
    main()