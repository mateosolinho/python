import cv2
import pytesseract
import re
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from collections import deque
import csv
from openpyxl import Workbook

def cleanup(im):
    """Limpia una imagen restando su valor mediano de píxeles y luego escalándola."""
    arr = np.array(im, dtype=float)
    if arr.mean(axis=-1).max() < 200:
        arr[:] = 0  # si no hay texto, devuelve imagen en negro
    else:
        arr -= np.median(arr) + 5
        arrmax = arr.max(axis=(0, 1))
        if all(arrmax != 0):
            arr *= 255 / arrmax
        arr = arr.clip(0, 255)
    return arr.astype(np.uint8)

def extract_text(image_region):
    """Extrae texto de la región de imagen proporcionada."""
    custom_config = r'--oem 3 --psm 6'
    return pytesseract.image_to_string(image_region, config=custom_config)

def moving_average(data, window_size):
    """Calcula el promedio móvil de una lista de números."""
    if len(data) < window_size:
        return np.mean(data) if data else 0
    return np.mean(data[-window_size:])

def time_to_seconds(time_text):
    """Convierte el tiempo en formato XX:XX:XX a segundos."""
    parts = time_text.split(':')
    
    # Hay 3 partes y que ninguna está vacía
    if len(parts) == 3 and all(part.isdigit() for part in parts):
        hours, minutes, seconds = map(int, parts)
        return hours * 3600 + minutes * 60 + seconds
    return 0  # Si no está en el formato correcto, devolver 0

def read_speed_and_altitude_from_video(video_path):
    cap = cv2.VideoCapture(video_path)

    cap.set(cv2.CAP_PROP_POS_MSEC, 1085000)
    
    # Cuadrante Super Heavy
    # rect_start_x = int(0.8 * 270)  # Cambiar según el ancho del vídeo
    # rect_start_y = int(0.8 * 1135)  # Cambiar según el alto del vídeo
    # rect_width = 230  # Ancho del rectángulo
    # rect_height = 35  # Alto del rectángulo

    # Cuadrante StarShip
    rect_start_x = int(0.8 * 1750)  # Cambiar según el ancho del vídeo
    rect_start_y = int(0.8 * 1135)  # Cambiar según el alto del vídeo
    rect_width = 230  # Ancho del rectángulo
    rect_height = 35  # Alto del rectángulo

    # Definición de la región donde se espera que esté ALTITUDE
    altitude_rect_start_y = rect_start_y + rect_height  # Posición justo debajo de SPEED

    # Definición de la región donde se espera que esté el contador de tiempo
    time_rect_start_x = 905
    time_rect_start_y = 950
    time_rect_width = 155
    time_rect_height = 45

    speed_buffer = deque(maxlen=5)  # Mantiene los últimos 5 valores
    altitude_buffer = deque(maxlen=5)  # Mantiene los últimos 5 valores

    frame_counter = 0  # Contador de fotogramas

    # Crear un archivo CSV para almacenar los datos
    with open('telemetry_data.csv', mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Time', 'Speed', 'Altitude'])

        # Crear un archivo .xlsx para almacenar los datos
        workbook = Workbook()
        sheet = workbook.active
        sheet.append(['Time (seconds)', 'Speed', 'Altitude'])

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Solo procesar cada 10 fotogramas
            if frame_counter % 5 == 0:
                # Extrae las regiones donde se encuentran SPEED, ALTITUDE, y el contador de tiempo
                speed_region = frame[rect_start_y:rect_start_y + rect_height, rect_start_x:rect_start_x + rect_width]
                altitude_region = frame[altitude_rect_start_y:altitude_rect_start_y + rect_height, rect_start_x:rect_start_x + rect_width]
                time_region = frame[time_rect_start_y:time_rect_start_y + time_rect_height, time_rect_start_x:time_rect_start_x + time_rect_width]

                # Dibuja rectángulos sobre las regiones de interés
                cv2.rectangle(frame, (rect_start_x, rect_start_y), (rect_start_x + rect_width, rect_start_y + rect_height), (0, 255, 0), 2)
                cv2.rectangle(frame, (rect_start_x, altitude_rect_start_y), (rect_start_x + rect_width, altitude_rect_start_y + rect_height), (255, 0, 0), 2)
                cv2.rectangle(frame, (time_rect_start_x, time_rect_start_y), (time_rect_start_x + time_rect_width, time_rect_start_y + time_rect_height), (0, 0, 255), 2)

                # Limpia las imágenes antes de extraer texto
                cleaned_speed_region = cleanup(speed_region)
                cleaned_altitude_region = cleanup(altitude_region)
                cleaned_time_region = cleanup(time_region)

                # Realiza la extracción de texto en paralelo
                with ThreadPoolExecutor() as executor:
                    speed_future = executor.submit(extract_text, cleaned_speed_region)
                    altitude_future = executor.submit(extract_text, cleaned_altitude_region)
                    time_future = executor.submit(extract_text, cleaned_time_region)

                    speed_text = speed_future.result()
                    altitude_text = altitude_future.result()
                    time_text = time_future.result()

                # Limpia el texto detectado y extrae solo los números
                speed_numbers = re.findall(r'\d+', speed_text.replace('"', '').replace("'", '').strip())
                altitude_numbers = re.findall(r'\d+', altitude_text.replace('"', '').replace("'", '').strip())
                time_text = re.sub(r'[^0-9:]', '', time_text)

                print(f"Texto detectado en la región de tiempo: {time_text.strip()}")

                # Obtener valores detectados
                if speed_numbers:
                    speed_value = int(speed_numbers[0])  # Convertir a entero para el promedio
                    speed_buffer.append(speed_value)  # Añadir al buffer
                else:
                    speed_value = "No speed detected"

                if altitude_numbers:
                    altitude_value = int(altitude_numbers[0])  # Convertir a entero
                    altitude_buffer.append(altitude_value)  # Añadir al buffer
                else:
                    altitude_value = "No altitude detected"

                # Calcular promedios
                avg_speed = speed_value if isinstance(speed_value, int) else speed_value  # Usar valor detectado para la velocidad
                avg_altitude = int(moving_average(list(altitude_buffer), window_size=5))  # Convertir a entero
                
                time_in_seconds = time_to_seconds(time_text.strip())
                
                current_time = time_in_seconds  # Usar el tiempo en segundos
                # Guardar los datos en el CSV y en el archivo Excel
                csv_writer.writerow([current_time, speed_value if isinstance(speed_value, int) else speed_value, avg_altitude])
                sheet.append([current_time, speed_value if isinstance(speed_value, int) else speed_value, avg_altitude])

                # Muestra los valores detectados en el frame original
                cv2.putText(frame, f"Speed: {speed_value}", (rect_start_x, rect_start_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                cv2.putText(frame, f"Altitude: {avg_altitude}", (rect_start_x, altitude_rect_start_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

                # Mostrar el texto detectado en la región de tiempo
                cv2.putText(frame, f"Time: {time_in_seconds} seconds", (time_rect_start_x, time_rect_start_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            # Muestra el frame original con la detección
            cv2.imshow('Original Frame', frame)

            frame_counter += 1  # Incrementa el contador de fotogramas
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            # Comprobación para finalizar el programa 
            if time_in_seconds == 2343:
                print("Tiempo alcanzado: 2343 segundos. Deteniendo el programa.")
                break  # Salir del bucle

    cap.release()
    cv2.destroyAllWindows()

    # Guarda el archivo .xlsx
    workbook.save('telemetry_data.xlsx')

# Uso del programa
video_path = 'C:/Users/mateo/Desktop/python/projects/rockettelemetry/ift4.mp4'
read_speed_and_altitude_from_video(video_path)
