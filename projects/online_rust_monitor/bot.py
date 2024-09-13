import discord
from discord.ext import commands
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import json
import re
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configura tu bot y token
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True  # Añade esta línea

bot = commands.Bot(command_prefix='!', intents=intents)

api_key = os.getenv('BATTLEMETRICS_API_KEY')
discord_token = os.getenv('DISCORD_TOKEN')

# URL de la API de BattleMetrics para obtener el identificador de coincidencia
match_url = 'https://api.battlemetrics.com/players/match'

# Cabeceras de la solicitud
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

def fetch_all_pages(url, match_data):
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

async def scrape_player_page(player_id):
    url = f'https://www.battlemetrics.com/players/{player_id}'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        h5_tags = soup.find_all('h5')
        for h5 in h5_tags:
            a_tags = h5.find_all('a', href=True)
            for a_tag in a_tags:
                if a_tag['href'] == '/servers/rust/3344761':
                    small_tag = h5.find('small')
                    if small_tag:
                        last_seen_text = small_tag.text
                        # Convertir el texto en una fecha legible
                        return convert_last_seen_text(last_seen_text)
                    break
            else:
                continue
            break
    return None

def convert_last_seen_text(text):
    # Ejemplos de textos que el scraping podría devolver
    if "now" in text:
        return "El jugador está conectado"
    match = re.match(r"last seen (\d+) (hour|minute)s? ago", text)
    if match:
        amount, unit = match.groups()
        if unit == "hour":
            if int(amount) == 1:
                return f"Última vez visto hace 1 hora"
            else:
                return f"Última vez visto hace {amount} horas"
        elif unit == "minute":
            if int(amount) == 1:
                return f"Última vez visto hace 1 minuto"
            else:
                return f"Última vez visto hace {amount} minutos"
    return text

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command(name='player')
async def player(ctx, *, player_name: str):
    await ctx.send('Buscando jugadores, por favor espera...')
    
    print(f'Received command with player_name: {player_name}')
    
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
    
    # Obtener todos los resultados
    all_players = fetch_all_pages(match_url, match_data)
    print(f'Found {len(all_players)} players')

    # Obtener la fecha actual y la fecha límite (24 horas atrás)
    now = datetime.utcnow()
    twenty_four_hours_ago = now - timedelta(days=1)
    twenty_four_hours_ago_unix = int(twenty_four_hours_ago.timestamp())

    # Filtrar los jugadores que se conectaron en las últimas 24 horas
    recent_players = []
    for item in all_players:
        last_seen_str = item.get('attributes', {}).get('lastSeen')
        if last_seen_str:
            last_seen = datetime.fromisoformat(last_seen_str.replace('Z', '+00:00'))
            last_seen_unix = int(last_seen.timestamp())
            if last_seen_unix > twenty_four_hours_ago_unix:
                recent_players.append(item)

    print(f'Found {len(recent_players)} recent players')

    # Obtener los IDs de relationships de los jugadores filtrados
    relationships_ids = []
    for player in recent_players:
        player_id = player.get('relationships', {}).get('player', {}).get('data', {}).get('id')
        if player_id:
            relationships_ids.append(player_id)

    # Realizar scraping directamente para cada ID en la lista de IDs obtenida
    results = []
    for player_id in relationships_ids:
        dato = await scrape_player_page(player_id)
        if dato:  # Solo añade si dato no es None
            results.append(f'Player ID {player_id}: {dato}')
            results.append(f'Link al perfil ➜ https://www.battlemetrics.com/players/{player_id}')
    
    if results:
        response_message = '\n'.join(results)
    else:
        response_message = 'No se encontraron jugadores recientes con ese nombre.'

    await ctx.send(response_message)

# Ejecutar el bot
bot.run(discord_token)
