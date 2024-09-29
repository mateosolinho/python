import cv2
import pytesseract
import re

# Configura la ruta a Tesseract si no está en tu PATH
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Cambia esta ruta según tu instalación

def read_speed_from_video(video_path):
    cap = cv2.VideoCapture(video_path)

    # Definición de la región donde se espera que esté SPEED
    rect_start_x = int(0.8 * 250)  # Cambia según el ancho del vídeo
    rect_start_y = int(0.8 * 1125)  # Cambia según el alto del vídeo
    rect_width = 320  # Ancho del rectángulo
    rect_height = 50  # Alto del rectángulo

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Extrae la región donde se encuentra el SPEED
        speed_region = frame[rect_start_y:rect_start_y + rect_height, rect_start_x:rect_start_x + rect_width]
        
        # Dibuja un rectángulo sobre la región de interés
        cv2.rectangle(frame, (rect_start_x, rect_start_y), (rect_start_x + rect_width, rect_start_y + rect_height), (0, 255, 0), 2)

        # Usa Tesseract para extraer el texto sin preprocesamiento
        custom_config = r'--oem 3 --psm 6'  # Ajusta estos valores según necesites
        speed_text = pytesseract.image_to_string(speed_region, config=custom_config)

        # Limpiar el texto detectado y extraer solo los números
        cleaned_text = speed_text.replace('"', '').replace("'", '').strip()
        numbers = re.findall(r'\d+', cleaned_text)  # Encuentra todos los números en el texto

        if numbers:
            speed_value = numbers[0]  # Tomar el primer número encontrado
            print(f"Número detectado: {speed_value}")  # Imprime el número leído
        else:
            speed_value = "No speed detected"

        # Muestra el valor detectado en el frame original
        cv2.putText(frame, f"Speed: {speed_value}", (rect_start_x, rect_start_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Muestra el frame original con la detección
        cv2.imshow('Original Frame', frame)

        # Muestra el texto detectado en una ventana aparte
        cv2.imshow('Detected Text', speed_region)
        cv2.putText(speed_region, cleaned_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.imshow('Text Recognition', speed_region)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Uso del programa
video_path = 'C:/Users/mateo/Desktop/python/rockettelemetry/ift.mp4'  # Cambia esto a la ruta de tu vídeo
read_speed_from_video(video_path)
