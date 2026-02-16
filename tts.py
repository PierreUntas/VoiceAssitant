# tts.py

from gtts import gTTS
import subprocess
import os
import tempfile

def text_to_speech(text):
    """
    Text-to-speech using Google TTS API for natural French voice.
    """
    try:
        # Create temporary file for audio
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
            temp_file = fp.name
        
        # Generate speech using Google TTS
        tts = gTTS(text=text, lang='fr', slow=False)
        tts.save(temp_file)
        
        # Play the audio file using mpg123 (silent mode)
        subprocess.run(["mpg123", "-q", temp_file], check=True, 
                      stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Clean up temporary file
        os.remove(temp_file)
        
    except Exception as e:
        print(f"Erreur TTS: {e}. Message: {text}")
