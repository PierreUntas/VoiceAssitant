# main.py

import subprocess
from tts import text_to_speech
from speech import listen_for_requests, get_command
from assistant import ask_perplexity
from deebot_control import launch_deebot_cleaning, send_deebot_to_base
from weather import get_weather_forecast
from youtube_control import play_youtube_music, stop_youtube_music


def execute_command(command):
    if command:

        if (
            "arrête la musique" in command
            or "stop musique" in command
            or "stop la musique" in command
            or "stoppe musique" in command
        ):
            stopped = stop_youtube_music()
            if stopped:
                text_to_speech("J'ai arrêté le processus")
            else:
                text_to_speech("Aucune est en cours de lecture.")

        # 2. Commandes de lancement de musique ENSUITE
        elif (
            "joue" in command
            or (
                "musique" in command
                and "arrête" not in command
                and "stop" not in command
                and "stoppe" not in command
            )
        ):
            titre = command.replace("joue", "").replace("musique", "").strip()
            if titre:
                text_to_speech(f"Je lance {titre} sur YouTube sans publicité.")
                success = play_youtube_music(titre)
                if not success:
                    text_to_speech("Je n'ai pas trouvé cette musique sur YouTube.")
            else:
                text_to_speech("Quelle musique souhaitez-vous écouter ?")

        elif "mail" in command:
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

        elif "gmf" in command or "assurance" in command:
            text_to_speech("Je vais ouvrir votre espace client GMF.")
            subprocess.run(["open", "https://mon-espace-societaire.gmf.fr/homepage"], check=True)
        
        elif "arrête la musique" in command or "stop musique" in command or "stop la musique" in command:
            stopped = stop_youtube_music()
            if stopped:
                text_to_speech("J'ai arrêté la musique.")
            else:
                text_to_speech("Aucune musique n'est en cours de lecture.")

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
