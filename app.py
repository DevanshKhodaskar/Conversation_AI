from flask import Flask, render_template, request, jsonify
import sounddevice as sd
import numpy as np
import whisper
import tempfile
import scipy.io.wavfile as wav
import threading
import os
from kokoro import KPipeline
from dotenv import load_dotenv
import groq

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize Flask app
app = Flask(__name__)

# Recorder configuration
samplerate = 16000
channels = 1

# Recorder class for capturing audio
class Recorder:
    def __init__(self):
        self.recording = False
        self.audio = []
        self.stream = None

    def start(self):
        self.recording = True
        self.audio = []
        self.stream = sd.InputStream(samplerate=samplerate, channels=channels, dtype='int16', callback=self.callback)
        self.stream.start()

    def stop(self):
        self.recording = False
        if self.stream:
            self.stream.stop()
            self.stream.close()
            self.stream = None

    def callback(self, indata, frames, time, status):
        if self.recording:
            self.audio.append(indata.copy())

    def save(self, filename):
        if self.audio:
            audio_np = np.concatenate(self.audio, axis=0)
            wav.write(filename, samplerate, audio_np)

recorder = Recorder()

# Transcribe audio using Whisper
def transcribe_whisper(filename):
    model = whisper.load_model("small")
    result = model.transcribe(filename)
    return result['text']

# Query Groq API with a system prompt
def query_groq(prompt):
    client = groq.Groq(api_key=groq_api_key)

    system_message = '''You are a helpful AI assistant. Your goal is to provide accurate, concise, and friendly responses. Follow these guidelines:
    - Be clear and direct in your answers.
    - If you're unsure, acknowledge it and suggest alternatives.
    - Use a friendly and professional tone.
    - Avoid jargon unless necessary, and explain technical terms when used.
    - Respect user privacy and do not ask for personal information.
    - If a request is unclear, ask for clarification.
    - Provide step-by-step instructions when applicable.
    - Be patient and supportive, especially with complex topics.
    - Always aim to be helpful and constructive in your responses.'''

    chat = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ]
    )
    return chat.choices[0].message.content

# Text-to-speech using Kokoro
tts_pipeline = KPipeline(lang_code='a')

def speak_with_kokoro(text):
    for _, _, audio in tts_pipeline(text, voice='af_heart'):
        sd.play(audio, 24000)
        sd.wait()

# Web routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_recording():
    threading.Thread(target=recorder.start).start()
    return jsonify({"status": "recording started"})

@app.route('/stop', methods=['POST'])
def stop_recording():
    recorder.stop()
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
        recorder.save(tmpfile.name)
        text = transcribe_whisper(tmpfile.name)
        reply = query_groq(text)
        threading.Thread(target=speak_with_kokoro, args=(reply,)).start()
        return jsonify({"transcript": text, "response": reply})

if __name__ == '__main__':
    app.run(debug=True)
