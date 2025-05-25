# main.py

import subprocess
from tts import text_to_speech
from speech import listen_for_requests, get_command
from assistant import ask_perplexity
from deebot_control import launch_deebot_cleaning, send_deebot_to_base
from weather import get_weather_forecast

def execute_command(command):
    if command:
        if "mail" in command:
            text_to_speech("Je vais ouvrir votre boîte mail.")
            subprocess.run(["open", "https://mail.google.com"], check=True)
        elif "calendrier" in command:
            text_to_speech("Je vais ouvrir votre calendrier.")
            subprocess.run(["open", "https://calendar.google.com"], check=True)
        elif "météo" in command:
            meteo = get_weather_forecast("Bordeaux")
            text_to_speech(meteo)

        elif "yoga" in command:
            text_to_speech("Je vous ouvre votre session de yoga.")
            subprocess.run(["open", "https://www.downdogapp.com/web"], check=True)
        elif "films" in command or "film" in command:
            text_to_speech("Je vous ouvre amazon vidéo.")
            subprocess.run(["open", "https://www.primevideo.com/region/eu/storefront"], check=True)
        elif "notes" in command or "note" in command:
            subprocess.run(["open", "-a", "Obsidian", "/Users/pierrearensuntas/Library/Mobile Documents/iCloud~md~obsidian"], check=True)
        elif "assistant" in command or "question" in command:
            text_to_speech("Quelle est votre question pour Perplexity ?")
            question = get_command()
            if question:
                text_to_speech("Je réfléchis à votre question.")
                response = ask_perplexity(question)
                print(f"Réponse Perplexity : {response}")
                text_to_speech(response)
            else:
                text_to_speech("Je n'ai pas compris votre question.")
        elif "nettoyage" in command:
            text_to_speech("Je vais lancer le nettoyage.")
            launch_deebot_cleaning()
        elif "retour à la base" in command or "charger le robot" in command:
            text_to_speech("Je vais renvoyer le robot à sa base.")
            send_deebot_to_base()
        else:
            text_to_speech("Commande non reconnue.")

def main():
    while True:
        listen_for_requests()
        text_to_speech("Je vous écoute.")
        command = get_command()
        execute_command(command)

if __name__ == "__main__":
    main()
