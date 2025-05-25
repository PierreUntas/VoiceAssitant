# weather.py
from meteofrance_api.client import MeteoFranceClient

def get_weather_forecast(ville="Bordeaux"):
    client = MeteoFranceClient()
    places = client.search_places(ville)
    if not places:
        return f"Aucune ville trouvée pour {ville}."
    lieu = places[0]
    forecast = client.get_forecast(lieu.latitude, lieu.longitude)
    today = forecast.daily_forecast[0]
    message = (
        f"Météo à {ville} aujourd'hui : {today['weather12H']['desc']}. "
        f"Température min : {today['T']['min']} degrés, "
        f"max : {today['T']['max']} degrés."
    )
    return message
