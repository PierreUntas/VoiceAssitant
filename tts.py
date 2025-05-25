# tts.py

import subprocess

def text_to_speech(text):
    subprocess.run(["say", "-v", "Amélie", text], check=True)
