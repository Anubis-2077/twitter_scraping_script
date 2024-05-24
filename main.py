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

# Función para realizar la búsqueda de tweets
def search_tweets(query, tweet_fields, max_results=10):
    search_url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&tweet.fields={tweet_fields}&max_results={max_results}"
    headers = create_headers(bearer_token)
    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Request returned an error: {response.status_code} {response.text}")
    return response.json()


############## busqueda ######################

query = "#iphone"
tweet_fields = "author_id,text,created_at,geo"
place_id = "place_id_for_recoleta"  # Reemplaza con el place_id de Recoleta
geocode = "-34.599722222222, -58.381944444444,50km"
max_results = 10


##############json#####################

# Realizar la búsqueda de tweets
try:
    json_response = search_tweets(query, tweet_fields, max_results)
    tweets = json_response['data']
except Exception as e:
    print(f"Error durante la búsqueda: {e}")

# Procesar y mostrar los tweets
tweet_data = []
for tweet in tweets:
    tweet_info = {
        'author_id': tweet['author_id'],
        'text': tweet['text'],
        'created_at': tweet['created_at'],
        'geo': tweet.get('geo', 'N/A')
    }
    tweet_data.append(tweet_info)

# Mostrar los resultados
for data in tweet_data:
    print(f"Author ID: {data['author_id']}, Texto: {data['text']}, Creado: {data['created_at']}, Geo: {data['geo']}")
    print("---")

# Guardar los resultados en un archivo JSON
with open('tweets_prueba.json', 'w') as f:
    json.dump(tweet_data, f, indent=4)