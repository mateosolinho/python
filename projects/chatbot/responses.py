import random
import json

intents = json.loads(open('intents.json').read())

# Función para obtener una respuesta aleatoria asociada a una intención específica
def get_response(intents_list, intent_name):
    for i in intents_list['intents']:
        if i['tag'] == intent_name: # Cuando encuentra un tag igual al intent_name escoge una frase random de las respuestas disponibles
            return random.choice(i['responses'])
