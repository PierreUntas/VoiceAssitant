# youtube_control.py

import urllib.parse
import urllib.request
import re
import subprocess

mpv_process = None  # Variable globale

def play_youtube_music(query):
    global mpv_process
    # Recherche YouTube
    query_string = urllib.parse.urlencode({"search_query": query})
    url = "https://www.youtube.com/results?" + query_string
    html_content = urllib.request.urlopen(url)
    search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    if not search_results:
        print("Aucun résultat trouvé.")
        return False
    video_url = f"https://www.youtube.com/watch?v={search_results[0]}"
    print(f"Lancement de : {video_url}")

    # Arrêter l'ancien mpv si besoin
    if mpv_process and mpv_process.poll() is None:
        mpv_process.terminate()
        mpv_process.wait()

    # Lance la lecture audio avec mpv (sans pub, sans reprise, sans fenêtre)
    mpv_process = subprocess.Popen([
        "mpv", "--no-video", "--no-resume-playback", "--force-window=no", video_url
    ])
    return True

def stop_youtube_music():
    global mpv_process
    if mpv_process and mpv_process.poll() is None:
        mpv_process.terminate()
        mpv_process.wait()  # Attend la fin effective du processus
        mpv_process = None
        print("Lecture arrêtée.")
        return True
    print("Aucune musique en cours.")
    return False
