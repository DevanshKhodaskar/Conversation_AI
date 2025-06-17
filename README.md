# Voice Assistant (Flask + Whisper + Groq + Kokoro)

A modern, interactive voice assistant web app built with Flask, OpenAI Whisper for speech-to-text, Groq LLM for conversational AI, and Kokoro for text-to-speech. The UI is clean and responsive, providing real-time status updates and a beautiful user experience.

---

## Features
- 🎙 **Record your voice** and transcribe speech to text using Whisper
- 🤖 **Conversational AI**: Get concise, friendly, and helpful responses powered by Groq LLM
- 🔊 **Text-to-Speech**: Listen to AI responses with Kokoro TTS
- 🌐 **Modern UI**: Responsive, aesthetic, and informative web interface

---

## Demo
![Screenshot](/Screenshot%202025-06-17%20234005.png)

---

## Prompt Template
The system prompt template for the AI assistant is defined in the code and can be customized. For reference, see the prompt template in:

```
Prompt_templates/Screenshot 2025-06-17 234005.png
```

---

## Requirements
- Python 3.8+
- [Flask](https://flask.palletsprojects.com/)
- [sounddevice](https://python-sounddevice.readthedocs.io/)
- [numpy](https://numpy.org/)
- [openai-whisper](https://github.com/openai/whisper)
- [scipy](https://scipy.org/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [groq](https://pypi.org/project/groq/)
- [kokoro](https://github.com/your-kokoro-repo) <!-- Update with actual repo if public -->


## Usage
- Click **Start Recording** to begin capturing your voice.
- Click **Stop & Process** to transcribe, get an AI response, and hear the reply.
- The UI will show status updates (e.g., "Recording...", "Processing...", "Ready").
- Your spoken words and the AI's reply will be displayed and read aloud.

---

## Project Structure
```
New Project/
├── app.py                # Main Flask app
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html        # Web UI template
├── Temp/Experiments/     # Experimental scripts (optional)
└── venv/                 # Python virtual environment (optional)
```

---

## Customization
- **Prompt Template**: The system prompt for Groq LLM is defined in `app.py` and can be customized for different assistant personalities or behaviors.
- **UI**: Modify `templates/index.html` for further UI enhancements.

---

## Credits
- [OpenAI Whisper](https://github.com/openai/whisper)
- [Groq LLM](https://groq.com/)
- [Kokoro TTS](https://github.com/your-kokoro-repo) <!-- Update if public -->


---

## 🚀 Step-by-Step Tutorial: Clone & Run the Voice Assistant Project

### 1. **Install Prerequisites**
- **Python 3.8+**  
  Download and install from [python.org](https://www.python.org/downloads/).
- **Git**  
  Download and install from [git-scm.com](https://git-scm.com/downloads/).

---

### 2. **Clone the Repository**
Open your terminal (Command Prompt, PowerShell, or Terminal) and run:
```bash
git clone https://github.com/DevanshKhodaskar/Conversation_AI.git
```


### 3. **Navigate to the Project Directory**

Or use the folder name that matches your cloned repo.

---

### 4. **(Optional but Recommended) Create a Virtual Environment**
```bash
python -m venv venv
```
Activate the virtual environment:
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

---

### 5. **Install Dependencies**
```bash
pip install -r requirements.txt
```

---

### 6. **Set Up Environment Variables**
Create a file named `.env` in the project root directory.  
Add your Groq API key (and any other required keys):
```
GROQ_API_KEY=your_groq_api_key_here
```

---

### 7. **Run the Application**
```bash
python app.py
```
You should see output indicating that Flask is running, e.g.:
```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

---

### 8. **Open the Web App**
Open your browser and go to:  
[http://localhost:5000](http://localhost:5000)

---

### 9. **Using the App**
- Click **Start Recording** to begin capturing your voice.
- Click **Stop & Process** to transcribe, get an AI response, and hear the reply.
- Watch the status messages and results update in real time.

---

## 🛠️ Troubleshooting
- **Missing dependencies?**  
  Double-check your `