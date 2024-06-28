# Importación de bibliotecas necesarias
import json
import nltk
import warnings
from nltk.stem import WordNetLemmatizer # Procesamiento del lenguaje natural
from responses import get_response
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC # sklearn para el entrenamiento del modelo
warnings.filterwarnings('ignore')

# Descarga de recursos para la tokenización y lematización
nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

intents = json.loads(open('intents.json').read())

# Inicialización de palabras unicas, clases de intenciones y conjuntos de ellas
words = []
classes = []
documents = []
ignore_words = ['?', '!', '.', ',']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern) # Coge palabras clave del JSON
        words.extend(word_list)
        documents.append((word_list, intent['tag'])) # Gracias a esto se relacionan los tokens con las respuestas
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words] # Convierte cada palabra a su forma lematizada
words = sorted(list(set(words))) # Elimina las palabras repetidas

classes = sorted(list(set(classes))) # Elimina las preguntas repetidas

# print(words)
# print(classes)
# print(documents)

# Configura el vectorizador TF-IDF con lematización y tokenización personalizada
vectorizer = TfidfVectorizer(tokenizer=lambda text: [lemmatizer.lemmatize(w) for w in nltk.word_tokenize(text.lower()) if w not in ignore_words])
X_train = vectorizer.fit_transform([' '.join(doc) for doc, _ in documents]) # Transforma los documentos en una matriz de características TF-IDF
y_train = [tag for _, tag in documents] # Crea una lista de etiquetas de intención para el entrenamiento

clf = SVC(kernel='linear') # Se crea un clasificador utilizando un kernel lineal ????
clf.fit(X_train, y_train) #Se entrena dicho clasificador utilizando los datos de entrada

# Función para clasificar una frase y predecir la etiqueta de intención
def classify(sentence):
    X_test = vectorizer.transform([sentence]) # Transforma la frase en un vector TF-IDF usando el vectorizador entrenado
    tag = clf.predict(X_test)[0] # Predice la etiqueta de intención usando el clasificador SVM entrenado
    return tag

# Función para obtener la respuesta del chatbot basada en la etiqueta de intención predicha
def chatbot_response(text): 
    tag = classify(text) # Obtiene la etiqueta de intención predicha usando la función classify
    response = get_response(intents, tag)  # Obtiene la respuesta asociada a la etiqueta de intención usando una función get_response
    return response

# Bucle principal que permite la interacción continua con el chatbot
while True:
    user_input = input("Tu: ")
    if user_input.lower() == "Salir":
        break
    response = chatbot_response(user_input) # Obtiene la respuesta del chatbot basada en la entrada del usuario
    print(f"ChatBot: {response}")
