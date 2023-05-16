<p align=center><img src=https://assets.soyhenry.com/logos/LOGO-HENRY-04.png><p>

# PROYECTO INDIVIDUAL N°1 - DATA ENGINEER

## *Desarrollado por Carlos Sanchez para el bootcamp de Henry * 


#### Problemática:
- **Elaboracion** de 6 funciones con objetivos especificos y creacion de un modelo de Machine Learnig que hace una recomendacion de las 5 peliculas mas similares, todo este desarrollo, desde extraccion de los datos hasta la creacion del modelo (**Data engineering**), proyecto solicitado por nuestro empleador que provee servicios de agregación de plataformas de streaming, utilizamos un [dataset](https://github.com/CASA27/MLOPs) para realizar las **transformaciones requeridas** y posteriormente **poner a disposición los datos** mediante la elaboración y ejecución de una **API** puesta en produccion en la plataforma de alojamiento web para aplicaciones llamada Render [API](https://proyecto-vesv.onrender.com)

#### Rol del desarrollador:
- Data engineer

<hr> 

### Proceso de "ETL" (Extract, transform, load) en VisualStudioCode - Python:

`EXTRACCIÓN DE DATOS`


1. Importación de la librería pandas para el manejo de los dataframes
2. Ingesta de datos (Archivos .csv provisto por nuestro empleador)
3. Análisis exploratorio del dataset para conocer sus características principales
   
`TRANSFORMACIONES`

+ Desanidar algunos campos, como **`belongs_to_collection`**, **`production_companies`** y otros que contienen en sus filas, diccionarios y listas, para poder ser utilizados y unirlo al nuevo dataset y faciliten la creacion de la API

+ Los valores nulos de los campos **`revenue`**, **`budget`** deben ser rellenados por el número **`0`**.
  
+ Los valores nulos del campo **`release date`** deben eliminarse.

+ De haber fechas, deberán tener el formato **`AAAA-mm-dd`**, además deberán crear la columna **`release_year`** donde extraerán el año de la fecha de estreno.

+ Crear la columna con el retorno de inversión, llamada **`return`** con los campos **`revenue`** y **`budget`**, dividiendo estas dos últimas **`revenue / budget`**, cuando no hay datos disponibles para calcularlo, deberá tomar el valor **`0`**.

+ Eliminar las columnas que no serán utilizadas, **`video`**,**`imdb_id`**,**`adult`**,**`original_title`**,**`vote_count`**,**`poster_path`** y **`homepage`**.

9.  Exportar CSV final (df) con todas las transformaciones

##### *Nota: La extracción de datos así como las respectivas transformaciones pueden verse desarrolladas en el archivo [ETL.ipynb]( https://github.com/amysler/Proyecto_individual_data_engineer-Henry_bootcamp-DTS06/blob/main/ETL.ipynb)*
  
  <hr> 

### Desarrollo de las consultas solicitadas:

`CONSULTAS A REALIZAR`

+ Se ingresa el mes y la consulta debe retornar la cantidad de peliculas que se estrenaron ese mes (nombre del mes, en str, ejemplo 'enero') historicamente'''

+ Se ingresa el dia y la consulta debe retornar la cantidad de peliculas que se estrenaron ese dia (de la semana, en str, ejemplo 'lunes') historicamente'''

+ Se ingresa la franquicia, y la consulta debe retornr la cantidad de peliculas, ganancia total y promedio'''

+ Se ingresas el pais y la consulta debe retornar la cantidad de peliculas producidas en el mismo'''

+ Si ingresa la productora y la consulta debe retorn la ganancia total y la cantidad de peliculas que produjeron'''

+ Se ingresas la pelicula y la consulta debe retornar la inversion, la ganancia, el retorno y el año en el que se lanzo'''

+ Se ingresas la pelicula y la consulta debe retornar la inversion, la ganancia, el retorno y el año en el que se lanzo'''


+ `Sistema de Recomendacion de Peliculas` → Se ingresa un nombre de pelicula y la consulta te recomienda las similares en una lista de 5 valores'''


Se desarrolla el código de las funciones que responden a las consultas solicitadas por el cliente

##### *Nota: El desarrolo de las consultas se encuentra alojado en el archivo [main.py](https://github.com/CASA27/MLOPs/blob/main/main.py)*

<hr>

### Proceso de puesta a disposición los datos utilizando FastAPI (framework que permite construir APIs con Python) y realizar el deploy: 
1. Generación de archivo [main.py](https://github.com/amysler/Proyecto_individual_data_engineer-Henry_bootcamp-DTS06/blob/main/main.py) (donde desarrollar el script) y otro [requirements.txt](https://github.com/amysler/Proyecto_individual_data_engineer-Henry_bootcamp-DTS06/blob/main/requirements.txt) (donde alojar los requerimientos para la API)
2. Importación de las librerías a utilizar
3. Declaración de la creación de la API 
4. Desarrollo de las consultas con formato:
   
```ruby
@app.get('/retorno/{pelicula}')
async def retorno(pelicula):
```

5. Creacion de una cuenta en [Render](https://render.com)
6. Creacion de la interfaz con los parametros indicados 
7. Se valida la url generada en Render y se realizan las respectivas consultas

<hr>

### Instrucciones para la utilización de la api puesta en produccion: 

*Ingrese a la [API](https://proyecto-vesv.onrender.com)
+ Coloque al final de la url, /docs para ingresar a la aplicacion 
+ Empiece con las consultas que desee 
+ Ejemplo si desea consultar la cantidad de peliculas que se estrenaron en un determinado mes, das click en GET /peliculas_mes/{mes Pelicula Mes} → le aparece en lado superior derecho de su pantalla un boton llamado Try it out 
+ Das click ahi y se habilita el campo para colocar el mes a consultar 
+ Colocas el mes
+ Le das Execute y la app te mostrara abajo en Responses → Response body, la respuesta con la siguiente sintaxis → 
{
  "mes": "enero",
  "cantidad": 5912
}
+ En las demas consultas, realizas el mismo procedimiento para solicitar la informacion

<hr> 

#### [Link a video explicativo confeccionado para equipo de data analytics](https://www.youtube.com/watch?v=WUqeqOXOoeg "Proyecto Individual data engineer - Henry bootcamp")

<hr> 

#### Tecnologías utilizadas:
- Visual studio code
- Python
- Render
- FastApi
- Uvicorn
- Pandas library

  
<img src="https://visualstudio.microsoft.com/wp-content/uploads/2019/06/vs-code-responsive-01.svg" width="50"/><img src="https://www.python.org/static/community_logos/python-logo.png" width="150"/><img src="https://techcrunch.com/wp-content/uploads/2019/10/render-logo-wordmark.png?w=764" width="150"/><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" width="150"/><img src="https://raw.githubusercontent.com/tomchristie/uvicorn/master/docs/uvicorn.png" width="80"/><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/1920px-Pandas_logo.svg.png" width="150"/>