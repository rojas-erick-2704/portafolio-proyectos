# Proyecto: Extracción de datos meteorológicos de la API de OpenWeather

  

Este proyecto consiste en extraer datos meteorológicos de la API de OpenWeather, una vez extraídos se cortan y se separan los datos que queremos utilizar, que en este caso son la humedad y la temperatura, de los que no queremos. La temperatura se convierte de Fahrenheit a Celsius y se envían a InfluxDB, la cual es una base de datos de series de tiempo. Posteriormente, los datos son enviados a Grafana para ser visualizados en un dashboard.

## Proceso

### Extracción de datos

Los datos meteorológicos son obtenidos a través de la API de OpenWeather.
Se extrae la información necesaria, en este caso la temperatura y la humedad.

  
### Conversión de temperatura
La temperatura obtenida de la API está en grados Fahrenheit, por lo que es necesario convertirla a grados Celsius para su mejor comprensión y visualización.


### Envío de datos a InfluxDB
InfluxDB es una base de datos de series de tiempo que nos permite almacenar, visualizar y analizar datos en tiempo real.
Se envían los datos de temperatura y humedad a InfluxDB mediante el uso de su API.


### Visualización de datos en Grafana
Grafana es una plataforma de visualización y análisis de datos en tiempo real.
Se crea un dashboard en Grafana para visualizar los datos de temperatura y humedad en tiempo real, los cuales se obtienen de InfluxDB.


### Conclusiones
Este proyecto es un ejemplo básico de cómo utilizar APIs para extraer y procesar datos, y cómo enviarlos a una base de datos de series de tiempo como InfluxDB para su posterior visualización en un dashboard en Grafana. A partir de este proyecto se pueden agregar más funcionalidades y ampliarlo para adaptarlo a necesidades específicas.


### Imágenes
La siguiente es una imagen de cómo se podría ver un Dashboard en Grafana recibiendo la información del clima de San José, Costa Rica: 

![Dashboard en Grafana mostrando el clima de San José, Costa Rica](https://github.com/rojas-erick-2704/proyectos/blob/98dcfcf42ae94af674848354a635645f2dd9f09b/ETL_Weather/Imagenes/DashboardWeatherSanJose.PNG)
