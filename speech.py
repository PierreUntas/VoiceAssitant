# speech.py

import speech_recognition as sr
from config import WORD_TO_CALL

def listen_for_requests():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"Dites '{WORD_TO_CALL}' pour activer le mode d'écoute")
        while True:
            try:
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio, language="fr-FR").lower()
                print(f"Vous avez dit : {command}")
                if WORD_TO_CALL in command:
                    print("Mode d'écoute activé")
                    return
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print(f"Erreur de requête : {e}")

def get_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("En attente de votre demande...")
        audio = recognizer.listen(source)
        try:
            request = recognizer.recognize_google(audio, language="fr-FR")
            print(f"Demande reçue : {request}")
            return request.lower()
        except sr.UnknownValueError:
            print("Je n'ai pas compris votre demande.")
            return None
        except sr.RequestError as e:
            print(f"Erreur de requête : {e}")
            return None
