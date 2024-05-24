import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

# Credenciales de la API de Twitter
bearer_token = os.getenv('BEARER_TOKEN')

# Función para crear los headers de autenticación
def create_headers(bearer_token):
    headers = {"Authorization": f"Bearer {bearer_token}"}
    return headers

# Función para obtener el place_id utilizando geo/reverse_geocode
def get_place_id(lat, long):
    geo_url = f"https://api.twitter.com/1.1/geo/reverse_geocode.json?lat={lat}&long={long}"
    headers = create_headers(bearer_token)
    response = requests.get(geo_url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Request returned an error: {response.status_code} {response.text}")
    places = response.json().get('result', {}).get('places', [])
    if not places:
        raise Exception("No places found for the given coordinates.")
    return places[0]['id']  # Retorna el primer place_id encontrado

# Coordenadas de Recoleta, Buenos Aires
lat = -34.5883
long = -58.3935

try:
    place_id = get_place_id(lat, long)
    print(f"Place ID: {place_id}")
except Exception as e:
    print(f"Error al obtener place_id: {e}")