import cv2
import pytesseract
import re
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from collections import deque


def cleanup(im):
    """Cleanup an image by subtracting its median pixel value, then scaling it up."""
    arr = np.array(im, dtype=float)
    if arr.mean(axis=-1).max() < 200:
        arr[:] = 0  # no text here, return black image
    else:
        arr -= np.median(arr) + 5
        arrmax = arr.max(axis=(0, 1))
        if all(arrmax != 0):
            arr *= 255 / arrmax
        arr = arr.clip(0, 255)
    return arr.astype(np.uint8)


def extract_text(image_region):
    """Extract text from the provided image region."""
    custom_config = r'--oem 3 --psm 6'
    return pytesseract.image_to_string(image_region, config=custom_config)


def moving_average(data, window_size):
    """Calculate the moving average for a list of numbers."""
    if len(data) < window_size:
        return np.mean(data) if data else 0
    return np.mean(data[-window_size:])


def read_speed_and_altitude_from_video(video_path):
    cap = cv2.VideoCapture(video_path)

    # Salta los primeros 50 segundos
    cap.set(cv2.CAP_PROP_POS_MSEC, 350000)  # 50000 milisegundos = 50 segundos

    # Definición de la región donde se espera que esté SPEED
    rect_start_x = int(0.8 * 270)  # Cambia según el ancho del vídeo
    rect_start_y = int(0.8 * 1145)  # Cambia según el alto del vídeo
    rect_width = 225  # Ancho del rectángulo
    rect_height = 30  # Alto del rectángulo

    # Definición de la región donde se espera que esté ALTITUDE
    altitude_rect_start_y = rect_start_y + rect_height  # Posición justo debajo de SPEED

    # Buffers para almacenar valores detectados
    speed_buffer = deque(maxlen=5)  # Mantiene los últimos 5 valores
    altitude_buffer = deque(maxlen=5)  # Mantiene los últimos 5 valores

    frame_counter = 0  # Contador de fotogramas

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Extrae la región donde se encuentra el SPEED
        speed_region = frame[rect_start_y:rect_start_y + rect_height, rect_start_x:rect_start_x + rect_width]
        # Extrae la región donde se encuentra la ALTITUDE
        altitude_region = frame[altitude_rect_start_y:altitude_rect_start_y + rect_height, rect_start_x:rect_start_x + rect_width]

        # Dibuja rectángulos sobre las regiones de interés
        cv2.rectangle(frame, (rect_start_x, rect_start_y), (rect_start_x + rect_width, rect_start_y + rect_height), (0, 255, 0), 2)
        cv2.rectangle(frame, (rect_start_x, altitude_rect_start_y), (rect_start_x + rect_width, altitude_rect_start_y + rect_height), (255, 0, 0), 2)

        # Limpia las imágenes antes de extraer texto
        cleaned_speed_region = cleanup(speed_region)
        cleaned_altitude_region = cleanup(altitude_region)

        # Realiza la extracción de texto en paralelo
        with ThreadPoolExecutor() as executor:
            speed_future = executor.submit(extract_text, cleaned_speed_region)
            altitude_future = executor.submit(extract_text, cleaned_altitude_region)

            speed_text = speed_future.result()
            altitude_text = altitude_future.result()

        # Limpia el texto detectado y extrae solo los números
        speed_numbers = re.findall(r'\d+', speed_text.replace('"', '').replace("'", '').strip())
        altitude_numbers = re.findall(r'\d+', altitude_text.replace('"', '').replace("'", '').strip())

        # Obtener valores detectados
        if speed_numbers:
            speed_value = int(speed_numbers[0])  # Convertir a entero para el promedio
            speed_buffer.append(speed_value)  # Añadir al buffer
        else:
            speed_value = "No speed detected"

        if altitude_numbers:
            altitude_value = int(altitude_numbers[0])  # Convertir a entero para el promedio
            altitude_buffer.append(altitude_value)  # Añadir al buffer
        else:
            altitude_value = "No altitude detected"

        # Calcular promedios
        avg_speed = moving_average(list(speed_buffer), window_size=5)
        avg_altitude = moving_average(list(altitude_buffer), window_size=5)

        # Muestra los valores promedio detectados en el frame original
        cv2.putText(frame, f"Speed: {avg_speed:.2f}", (rect_start_x, rect_start_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        cv2.putText(frame, f"Altitude: {avg_altitude:.2f}", (rect_start_x, altitude_rect_start_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

        # Muestra el frame original con la detección
        cv2.imshow('Original Frame', frame)

        frame_counter += 1
        if frame_counter % 5 == 0:  # Ajustar el intervalo de detección
            cv2.waitKey(1)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Uso del programa
video_path = 'C:/Users/mateo/Desktop/python/projects/rockettelemetry/ift.mp4'  # Cambia esto a la ruta de tu vídeo
read_speed_and_altitude_from_video(video_path)
