
# KetsuTalk

**KetsuTalk** is an immersive desktop application designed to help you learn Japanese with AI-powered conversations. Combining speech recognition, text-to-speech, and dynamic interactions, **KetsuTalk** uses **Ollama** for AI-driven dialogue and **VoiceVox** for realistic voice synthesis, providing a unique learning experience. Build your Japanese skills with the determination of a virtual sensei at your side.


## 👾 Project Status: Pre-Alpha 🛠️

This project is currently in **pre-alpha** development. It is a work in progress and not yet feature-complete. The main functionality is in place, but there are still many features to be added and bugs to be fixed. Expect improvements, enhancements, and new features in the future!


## Key Features
- **Immersive Conversations**: Engage in interactive, AI-powered conversations in Japanese.
- **Voice Interaction**: Send and receive voice messages to practice listening and speaking skills.
- **AI-Powered Teaching**: Get responses, corrections, and translations from a virtual sensei.
- **Customizable**: Adjust voice settings and prompt responses to personalize your learning experience.
- **Easy Setup**: Simple configuration for Ollama and VoiceVox integration to get started quickly.

## Technologies Used
- **Ollama**: Ollama provides the AI model for conversational dialogue. It helps generate realistic and intelligent responses.  
  Learn more: [Ollama GitHub](https://github.com/ollama/ollama)
  
- **VoiceVox**: A text-to-speech engine that creates high-quality, realistic Japanese voices for the application.  
  Learn more: [VoiceVox Guide](https://voicevox.hiroshiba.jp/how_to_use/)

## Installation
To get started, follow these steps:

### 1. Install **Ollama**  
Download and install **Ollama** from the official website:  
[Ollama Downloads](https://ollama.com/)

- After installation, open **PowerShell** (or your terminal) and run the following command to set up the **phi3** model:
```bash
ollama run phi3
```

### 2. Install **VoiceVox**
Download and install **VoiceVox** from the official site:  
[VoiceVox Downloads](https://voicevox.hiroshiba.jp/how_to_use/)

- Ensure you have **VoiceVox** running locally (usually on port 50021).

### 3. Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/kurojs/KetsuTalk.git
```

### 4. Install Python Dependencies
Before running the application, you need to install the required Python dependencies. Run the following command to install them:

```bash
pip install speechrecognition pydub requests translate keyboard
```

### 5. Run the Application
Execute the main Python script to start the application:
```bash
python main.py
```

## Future Plans
- **Desktop App**: Full-featured multilingual desktop application with an intuitive interface.
- **Advanced Features**: Editable prompts, more voice options, and personalized learning experiences.
- **Enhanced Conversations**: More dynamic conversations and corrections to simulate real-life interactions.

## Contributing
Feel free to fork the repository, open issues, and submit pull requests. Contributions are always welcome!

---

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
