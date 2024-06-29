import csv
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from platformdirs import user_downloads_dir

def leer_csv(filepath):
    # with open(filepath, newline='') as csvfile: # Lectura normal
    #     reader = csv.reader(csvfile)
    #     for row in reader:
    #         print(', '.join(row))
    df = pd.read_csv(filepath) # Lectura optimizada y mejorada con pandas
    return df

def select_path():
    path = filedialog.askopenfilename(title = "Select file",filetypes = (("CSV Files","*.csv"),("All","*.*")))
    tk.Tk().withdraw()
    
    return path

def menu(csv):
    print("\n--- Lector de archivos CSV ---")
    print("1. Estadísticas básicas del CSV")
    print("2. Filtrar por condición")
    print("3. Mostrar los datos ordenados")
    print("4. Calcular media de columna")
    print("5. Contar valores únicos")
    print("6. Crear gráfica")
    print("7. Salir")

    opcion = int(input("Escoge una opción: "))
    while True:
        match opcion:
            case 1:
                print(csv.describe())
            case 2:
                datos = ordenar_datos(csv)
                print(f"\n{datos}")
            case 3:
                media, columna = calcular_media(csv)
                print(f"\nLa media de la columna {columna} es {media}")
            case 4:
                datos = contar_valores_unicos(csv)
                print(f"\n{datos}")
            case 5:
                crear_grafica(csv)
            case 6:
                print("\nSaliendo...")
                break

def get_columna(csv):
    index_columna = int(input(f"\nSelecciona una columna, existen {csv.shape[1]}: "))
    columna = csv.columns[index_columna]

    return columna

def crear_grafica(csv):
    columna = get_columna(csv)
    tipo = int(input("Selecciona el tipo de gráfica histograma o barras (1/2): "))
    match tipo:
        case 1:
            csv[columna].hist()
            plt.xlabel(columna)
            plt.ylabel('Frecuencia')
            plt.title(f'Histograma de {columna}')
            plt.show()
        case 2:
            csv[columna].value_counts().plot(kind='bar')
            plt.xlabel(columna)
            plt.ylabel('Frecuencia')
            plt.title(f'Gráfica de barras de {columna}')
            plt.show()

def contar_valores_unicos(csv):
    columna = get_columna(csv)

    return csv[columna].value_counts()

def calcular_media(csv):
    columna = get_columna(csv)

    return csv[columna].mean(), columna

def ordenar_datos(csv):
    columna = get_columna(csv)

    ord = int(input("Datos de manera ascendente o descendente (1/2): "))

    if ord == 1:
        return csv.sort_values(by=columna, ascending=True)
    else:
        return csv.sort_values(by=columna, ascending=False)

if __name__ == "__main__":
    menu(leer_csv(select_path()))