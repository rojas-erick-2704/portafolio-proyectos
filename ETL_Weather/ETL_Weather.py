#Para Saber la latitud y longitud de consulta, se puede consultar en la pagina: 
##https://www.latlong.net/
import requests 
import pandas as pd
from pandas.io.json import json_normalize
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import time

#Credenciales para enviar los datos a Influxdb
token = "Token con acceso de escritura generado en Influx"
org = "Nombre de la organizacion que creó en Influx"
bucket = "Nombre del bucket que creó en Influx"


# URL a la que se hacen las solicitudes
base_url = "https://api.openweathermap.org/data/2.5/weather?"
# Key que se nos proporciona cuando nos registramos en https://openweathermap.org/  
api_key = "Key de la API solicitada en OpenWeather"
# Latitud del lugar de consulta
lat = "9.928557"
# Longitud del lugar de consulta
lon = "-84.084189"
# URL de consulta completa
complete_url = base_url + "lat=" + lat + "&lon=" + lon + "&appid=" + api_key

# Esta es la variable donde vamos a guardar la informacion del clima
weather_SanJose = None


def  kelvinToCelsius (fahrenheit):
    """
        Método que recibe la temperatura en grados fahrenheit y los convierte a Celsius 
        
        Argumentos:
            fahrenheit: temperatura a convertir en Celcius 
        Retorna: 
            float: temperatura convertida a grados celcius
        Autor:
            Erick Rojas Zúñiga 
    """
    return float(fahrenheit) - 273.15

#Se establece una conexión con la base de datos de InfluxDB, utilizando los parámetros indicados en la url, token y org.
with InfluxDBClient(url="Direccion IP del servidor influx", token=token, org=org, timeout=30_000) as client:
    #Se crea un objeto de la API de escritura de InfluxDB, el cual permite escribir los datos en la base de datos. 
    # Se utiliza el parámetro write_options para indicar que se desea realizar una escritura síncrona.
    write_api = client.write_api(write_options=SYNCHRONOUS)
    while True:
        # Se realiza la solicitud a la API de OpenWeather
        response = requests.get(complete_url)
        # El código 200 nos permite saber si la respuesta tuvo éxito
        if response.status_code == 200:
            weather_SanJose = response.json()
            # Extraemos la información que vamos a necesitar, en este caso temperatura y humedad
            general_Information =  weather_SanJose['main']
            # Convertimos la temperatura a Celcius
            temp_Celcius = kelvinToCelsius(general_Information["temp"])
            # Se crea un objeto Point de InfluxDB, que representa el valor de temperatura.
            temp = Point("Temperature").tag("location", "San José").field("temperature", str(temp_Celcius))
            # Se crea un objeto Point de InfluxDB, que representa el valor de humedad.
            humi = Point("Humidity").tag("location", "San José").field("humidity", str(general_Information["humidity"]))
            # Se escribe los valores de temperatura y humedad en la base de datos de InfluxDB
            write_api.write(bucket=bucket, record=[temp,humi])
            #Se espera un segundo antes de volver a ejecutar el código.
            time.sleep(1)
        else:
            # En caso de que la solicitud no tenga éxito, se muestra un mensaje de error en la consola.
            print("Hubo un error al realizar la solicitud")
    
