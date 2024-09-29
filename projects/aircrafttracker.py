import requests

# Configura tu área de interés
LAT_MIN = 42.0
LON_MIN = -9.0
LAT_MAX = 43.0
LON_MAX = -8.0

# URL de la API de OpenSky Network
API_URL = f"https://opensky-network.org/api/states/all?lamin={LAT_MIN}&lomin={LON_MIN}&lamax={LAT_MAX}&lomax={LON_MAX}"

# Realiza la solicitud a la API
response = requests.get(API_URL)
data = response.json()

# Procesa la información de vuelos
if 'states' in data:
    for aircraft in data['states']:
        icao24 = aircraft[0]            # Identificador ICAO del avión
        print(icao24)
        callsign = aircraft[1].strip()  # Llamado del avión
        origin_country = aircraft[2]    # País de origen
        latitude = aircraft[6]          # Latitud
        longitude = aircraft[5]         # Longitud
        altitude = aircraft[7]          # Altitud en pies
        velocity = aircraft[11]         # Velocidad en km/h

        # Define tus criterios de alerta
        if altitude and velocity:  # Verifica que la altitud y velocidad estén presentes
            if altitude > 10000 and velocity > 300:  # Ejemplo de criterios
                print(f"Alerta: Avión {callsign} ({icao24})")
                print(f"  País de origen: {origin_country}")
                print(f"  Latitud: {latitude}")
                print(f"  Longitud: {longitude}")
                print(f"  Altitud: {altitude} pies")
                print(f"  Velocidad: {velocity} km/h")
                print("-------------------------")
else:
    print("No se encontraron vuelos en la zona especificada.")