# Importamos las librerías necesarias para el análisis de datos y visualización
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Leemos el archivo CSV que contiene los datos de las misiones espaciales
df = pd.read_csv('C:/Users/mateo/Escritorio/python/projects/rocket_dataset/mission_launches.csv')
# Mostramos las primeras 10 filas del DataFrame para tener una idea general de los datos
df.head(10)

# Mostramos información general del DataFrame como el número de filas, columnas, tipos de datos y memoria utilizada
df.info()

# Eliminamos las columnas 'Unnamed: 0.1' y 'Unnamed: 0' que son irrelevantes para el análisis
df.drop(['Unnamed: 0.1','Unnamed: 0'], axis=1, inplace=True)
df.info()

# Convertimos la columna 'Date' a tipo datetime, manejando errores y estableciendo la zona horaria UTC
df['Date'] = pd.to_datetime(df['Date'], utc=True, errors='coerce')
df.info()

# Eliminamos las comas en la columna 'Price' y la convertimos a tipo float para poder realizar cálculos numéricos
df['Price'] = df['Price'].str.replace(',','').astype('float')
df.info()

# Rellenamos los valores nulos en la columna 'Price' con el valor promedio de la misma columna
df['Price'].fillna(df['Price'].mean(), inplace=True)
df.info()

# Eliminamos las filas donde la columna 'Date' es nula, ya que las fechas son cruciales para el análisis
df = df.dropna(subset='Date')
df.info()

# Extraemos el año de la columna 'Date' y lo almacenamos en una nueva columna llamada 'Year'
year = df['Date'].dt.year
df['Year'] = year
df.head(10)

# Extraemos el mes de la columna 'Date' y lo almacenamos en una nueva columna llamada 'Month'
month = df['Date'].dt.month
df['Month'] = month
df.head(10)

# Extraemos el país desde la columna 'Location', asumiendo que el país es el último elemento después de una coma
country = df['Location'].apply(lambda ctry: ctry.split(',')[-1].strip())
df['Country'] = country
df.head(10)

# Visualizamos la cantidad de misiones por país utilizando un gráfico de barras
y = df['Country'].value_counts().values
plt.bar(df['Country'].value_counts().index, y, color=plt.cm.viridis(y / max(y)))
plt.xticks(rotation = 45, ha = 'right')
plt.xlabel('Country')
plt.ylabel('Number of missions');

# Visualizamos la cantidad de misiones por organización utilizando un gráfico de barras
y = df['Organisation'].value_counts().values
plt.figure(figsize = (17,5))
plt.bar(df['Organisation'].value_counts().index, y, color=plt.cm.viridis(y / max(y)))
plt.xticks(rotation = 45, ha = 'right')
plt.xlabel('Organisation')
plt.ylabel('Number of missions');

# Visualizamos la cantidad de misiones por año utilizando un gráfico de barras
y = df.groupby('Year').size().values
plt.figure(figsize = (17,5))
plt.bar(df.groupby('Year').size().index, y, color=plt.cm.viridis(y / max(y)))
plt.xlabel('Year')
plt.ylabel('Number of missions');

# Visualizamos la cantidad de misiones por mes utilizando un gráfico de barras
y = df.groupby('Month').size().values
plt.bar(df.groupby('Month').size().index, y, color=plt.cm.viridis(y / max(y)))
plt.xlabel('Month')
plt.ylabel('Number of missions');

# Visualizamos el precio promedio de las misiones por año utilizando un gráfico de líneas
plt.figure(figsize = (12,5))
plt.plot(df.groupby('Year')['Price'].mean().index, df.groupby('Year')['Price'].mean().values, linestyle='-', marker='o')
plt.xlabel('Year')
plt.ylabel('Average Price');

# Visualizamos el estado de las misiones utilizando un gráfico de pastel
plt.figure(figsize = (8,8))
wedges, texts, autotexts = plt.pie(df['Mission_Status'].value_counts().values, labels=df['Mission_Status'].value_counts().index, autopct='%i%%', explode=[0,0.2,0.4,0.6], shadow=True, pctdistance=0.85)

# Ocultamos los textos para mejorar la legibilidad del gráfico
for text in texts:
    text.set_visible(False)

# Añadimos una leyenda para el gráfico de pastel
plt.legend(title="Mission-Status", bbox_to_anchor=(1, 0, 0.5, 1))

# Centramos los textos que indican los porcentajes en el gráfico de pastel
for autotext in autotexts:
    autotext.set_horizontalalignment('center')

# Creamos una tabla pivot que cuenta el número de misiones por año y estado de la misión
data_ms = df.pivot_table(index='Year', columns='Mission_Status', aggfunc='size', fill_value=0)
data_ms

# Visualizamos el número de misiones por año y estado de la misión utilizando un gráfico de líneas
plt.figure(figsize = (10,8))
plt.plot(data_ms["Success"].index,
         data_ms["Success"],
         color='g', label='Success')
plt.plot(data_ms["Failure"].index,
         data_ms["Failure"],
         color='r',
         label='Failure')
plt.plot(data_ms["Partial Failure"].index,
         data_ms["Partial Failure"],
         color='y', 
         label='Partial Failure',)
plt.plot(data_ms["Prelaunch Failure"].index, 
         data_ms["Prelaunch Failure"], 
         color='black', 
         label='Prelaunch Failure')
plt.xlabel("Year")
plt.ylabel("Number of Launches")
plt.legend()