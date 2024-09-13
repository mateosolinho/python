from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import json

# Tu API Key de BattleMetrics
api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6IjMyZDU3MjYyMWJkZWQ2YTMiLCJpYXQiOjE3MjYyMzE0NjEsIm5iZiI6MTcyNjIzMTQ2MSwiaXNzIjoiaHR0cHM6Ly93d3cuYmF0dGxlbWV0cmljcy5jb20iLCJzdWIiOiJ1cm46dXNlcjo5MTE2MDcifQ.E2guUHK5wUtngkbLY0yA7hZrNr5tunb0xo3cRjmZ_bs'

# Nombre del jugador a buscar
player_name = 'Luka'  # Reemplaza con el nombre del jugador

# URL de la API de BattleMetrics para obtener el identificador de coincidencia
match_url = 'https://api.battlemetrics.com/players/match'

# Datos a enviar en el cuerpo de la solicitud
match_data = {
    "data": [
        {
            "type": "identifier",
            "attributes": {
                "type": "name",
                "identifier": player_name
            }
        }
    ]
}

# Cabeceras de la solicitud
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

def fetch_all_pages(url):
    all_results = []
    while url:
        print(f"Fetching data from URL: {url}")
        response = requests.post(url, headers=headers, data=json.dumps(match_data))
        if response.status_code == 200:
            data = response.json()
            print(f"Received {len(data.get('data', []))} results")
            all_results.extend(data.get('data', []))
            
            # Obtener la URL de la siguiente página
            next_page_url = data.get('links', {}).get('next')
            url = next_page_url
        else:
            print(f"Request error: {response.status_code}, {response.text}")
            break
    return all_results

# Obtener todos los resultados
print("Fetching player data from API...")
all_players = fetch_all_pages(match_url)

# Obtener la fecha actual y la fecha límite (24 horas atrás)
now = datetime.utcnow()
twenty_four_hours_ago = now - timedelta(days=1)
twenty_four_hours_ago_unix = int(twenty_four_hours_ago.timestamp())

# Filtrar los jugadores que se conectaron en las últimas 24 horas
recent_players = []
for item in all_players:
    last_seen_str = item.get('attributes', {}).get('lastSeen')
    print(f"Processing player with lastSeen: {last_seen_str}")
    if last_seen_str:
        last_seen = datetime.fromisoformat(last_seen_str.replace('Z', '+00:00'))
        last_seen_unix = int(last_seen.timestamp())
        if last_seen_unix > twenty_four_hours_ago_unix:
            recent_players.append(item)

# Mostrar los jugadores recientes para depuración
print("Filtered recent players:")
print(json.dumps(recent_players, indent=4))

# Mostrar los IDs de relationships de los jugadores filtrados
print("IDs de relationships de jugadores recientes (últimas 24 horas):")
relationships_ids = []
for player in recent_players:
    player_id = player.get('relationships', {}).get('player', {}).get('data', {}).get('id')
    if player_id:
        print(player_id)
        relationships_ids.append(player_id)

# El href que quieres buscar
href_deseado = '/servers/rust/3344761'

# Función para hacer scraping de una página de un jugador
def scrape_player_page(player_id):
    url = f'https://www.battlemetrics.com/players/{player_id}'
    
    print(f"Scraping URL: {url}")
    
    # Realiza la solicitud HTTP
    response = requests.get(url)

    if response.status_code == 200:
        # Analiza el contenido HTML de la página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encuentra todos los elementos <h5> en la página
        h5_tags = soup.find_all('h5')

        for h5 in h5_tags:
            # Busca el enlace <a> dentro del <h5> y verifica su href
            a_tags = h5.find_all('a', href=True)
            for a_tag in a_tags:
                if a_tag['href'] == href_deseado:
                    # Dentro del <h5>, busca la etiqueta <small>
                    small_tag = h5.find('small')
                    if small_tag:
                        dato = small_tag.text
                        print(f'Dato encontrado para player ID {player_id}: {dato}')
                    break
            else:
                continue
            break
    else:
        print(f'No se pudo acceder a la página para player ID {player_id}')

# Realizar scraping directamente para cada ID en la lista de IDs obtenida
for player_id in relationships_ids:
    scrape_player_page(player_id)
