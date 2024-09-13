import requests
import json
from datetime import datetime

# Tu API Key de Steam
api_key = '9A7211947D9A19327F493860DF3516CE'

# ID de Steam del jugador
# steam_id = '76561198304699862'  # Reemplaza por el SteamID del jugador que quieras consultar
steam_id = '76561198249151164'  # Reemplaza por el SteamID del jugador que quieras consultar

# Función para obtener la información de la cuenta
def obtener_info_cuenta(steam_id, api_key):
    url = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/'
    params = {
        'key': api_key,
        'steamids': steam_id
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if 'players' in data['response'] and len(data['response']['players']) > 0:
            jugador = data['response']['players'][0]
            personastate = jugador.get('personastate', 'No disponible')
            return {
                'nombre': jugador.get('personaname', 'Desconocido'),
                'perfil_url': jugador.get('profileurl', 'No disponible'),
                'creado_en': datetime.utcfromtimestamp(jugador.get('timecreated', 0)).strftime('%Y-%m-%d %H:%M:%S') if jugador.get('timecreated') else 'No disponible',
                'ultimo_login': datetime.utcfromtimestamp(jugador.get('lastlogoff', 0)).strftime('%Y-%m-%d %H:%M:%S') if jugador.get('lastlogoff') else 'No disponible',
                'avatar': jugador.get('avatar', 'No disponible'),
                'nivel_privacidad': jugador.get('communityvisibilitystate', 'Desconocido'),
                'estado_conexion': interpret_personastate(personastate)
            }
        else:
            return None
    else:
        return None

def interpret_personastate(state_code):
    estados = {
        0: 'Offline',
        1: 'Online',
        2: 'Busy',
        3: 'Away',
        4: 'Snooze',
        5: 'Looking to trade',
        6: 'Looking to play'
    }
    return estados.get(int(state_code), 'Desconocido')

# Función para obtener la cantidad de horas jugadas en Rust
def obtener_owned_games(steam_id, api_key):
    url = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v1/'
    params = {
        'key': api_key,
        'steamid': steam_id,
        'include_appinfo': True,
        'include_played_free_games': True
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        juegos = data['response'].get('games', [])
        return juegos
    else:
        return f"Error en la API: {response.status_code}"

# Obtener los datos
info_cuenta = obtener_info_cuenta(steam_id, api_key)
juegos = obtener_owned_games(steam_id, api_key)

if info_cuenta:
    # Exportar la información de la cuenta
    with open('info_cuenta.json', 'w') as f:
        json.dump(info_cuenta, f, indent=4)
    print("Información de la cuenta exportada a info_cuenta.json")

    # Comprobar el nivel de privacidad y exportar los juegos si es adecuado
    nivel_privacidad = info_cuenta.get('nivel_privacidad', 'Desconocido')
    if nivel_privacidad != 'Desconocido' and int(nivel_privacidad) < 2:
        if isinstance(juegos, list):
            with open('juegos.json', 'w') as f:
                json.dump(juegos, f, indent=4)
            print("Datos de los juegos exportados a juegos.json")
        else:
            print(juegos)  # Mostrar el error en caso de que `juegos` no sea una lista
    else:
        print(f"El nivel de privacidad de la cuenta es {nivel_privacidad}, no se pueden mostrar los datos de los juegos")
else:
    print("No se pudo obtener la información de la cuenta")
