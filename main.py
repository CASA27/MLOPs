from fastapi import FastAPI
import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Leer el archivo CSV de películas
df = pd.read_csv('Dataset/df.csv')


# Creamos una instancia del framework FastAPI

app = FastAPI()

#http://127.0.0.1:8000

# Definimos los endpoints

@app.get('/')
async def root():
    return {'message': 'Bienvenido a la API de películas'}


@app.get('/peliculas_mes/{mes}')
async def peliculas_mes(mes):
       
    meses = {
        'enero': 'January',
        'febrero': 'February',
        'marzo': 'March',
        'abril': 'April',
        'mayo': 'May',
        'junio': 'June',
        'julio': 'July',
        'agosto': 'August',
        'septiembre': 'September',
        'octubre': 'October',
        'noviembre': 'November',
        'diciembre': 'December'
    }
    
    df = pd.read_csv('Dataset/df.csv')
    df = df.dropna(subset=['release_date'])
    
    df['release_date'] = pd.to_datetime(df['release_date'])
    df_mes = df[df['release_date'].dt.month_name() == meses[mes].capitalize()]
    respuesta = len(df_mes)
    
    return {'mes': mes, 'cantidad': respuesta}

@app.get('/peliculas_dia/{dia}')
async def peliculas_dia(dia):
    dias = {
    'lunes': 'Monday',
    'martes': 'Tuesday',
    'miércoles': 'Wednesday',
    'miercoles': 'Wednesday',
    'jueves': 'Thursday',
    'viernes': 'Friday',
    'sábado': 'Saturday',
    'sabado': 'Saturday',
    'domingo': 'Sunday'
    }
    df = pd.read_csv('Dataset/df.csv')
    df = df.dropna(subset=['release_date'])
    df['release_date'] = pd.to_datetime(df['release_date'])

    df_dia = df[df['release_date'].dt.day_name() == dias[dia].capitalize()]
    
    respuesta = len(df_dia)
    
    return {'dia': dia, 'cantidad': respuesta}
    


@app.get('/franquicia/{franquicia}')
async def franquicia(franquicia):
    # Filtramos las películas de la franquicia especificada
    franquicia_df = df[df['collection_name'].str.contains(franquicia, na=False)]

    # Obtenemos la cantidad de películas en la franquicia
    cantidad = len(franquicia_df)

    # Calculamos la ganancia total y promedio de la franquicia
    ganancia_total = franquicia_df['revenue'].sum()
    ganancia_promedio = franquicia_df['revenue'].mean()

    # Retornamos la información de la franquicia
    return {'franquicia': franquicia, 'cantidad': cantidad, 'ganancia_total': ganancia_total, 'ganancia_promedio': ganancia_promedio}


@app.get('/peliculas_pais/{pais}')
async def peliculas_pais(pais):
    
    df = pd.read_csv('Dataset/df.csv')
    # Eliminamos todas las filas del df que contienen valores faltantes o (NaN) en la columna 'production_countries_names'.
    df = df.dropna(subset=['production_countries_names'])
    # Elimina las filas duplicadas del df
    df = df.drop_duplicates()
    
    num_movies = 0
   
    for countries in df['production_countries_names']:      
        if pais in countries:
                num_movies += 1
             
    return num_movies


@app.get('/productoras/{productora}')
async def productoras(productora):

    df = pd.read_csv('Dataset/df.csv')
    df = df.dropna(subset=['production_companies_names'])

    mask = df['production_companies_names'].apply(lambda x: productora in x)
    df_filtered = df[mask]

    ganancia_total = df_filtered['revenue'].sum()
    cantidad = len(df_filtered)

    return {'productora': productora, 'ganancia_total': int(ganancia_total), 'cantidad': cantidad}

@app.get('/retorno/{pelicula}')
async def retorno(pelicula):
    
    df = pd.read_csv('Dataset/df.csv')
    df = df.dropna(subset=['return'])
    
    datos_pelicula = df.loc[df['title'] == pelicula]
    inversion = datos_pelicula['budget'].values[0]
    ganancia = datos_pelicula['revenue'].values[0]
    retorno = datos_pelicula['return'].values[0]
    anio = datos_pelicula['release_year'].values[0]
    

    return {'pelicula': pelicula, 'inversion': inversion, 'ganancia': ganancia, 'retorno': retorno, 'anio': anio}
    
    
@app.get('/recomendacion/{titulo}')
async def recomendacion(titulo):
    generodf = df['genre_names'].str.get_dummies('|')
    # Establecemos la cantidad de recomendaciones a devolver.
    k = 10  
    # Inicializamos un modelo KNN con un número de vecinos iguales a k+1
    knn = NearestNeighbors(n_neighbors=k+1, algorithm='auto') 
    # Entrenamos el modelo KNN utilizando el DataFrame de géneros
    knn.fit(generodf)
    # Indices de las películas más similares al títle utilizando el modelo KNN.
    indices = knn.kneighbors(generodf.loc[df['title'] == titulo])[1].flatten()
    # Guardamos los títulos de las películas recomendadas en una lista.
    recomendadas = list(df.iloc[indices]['title'])
    recomendadas = sorted(recomendadas, key=lambda x: df.loc[df['title'] == x]['vote_average'].values[0], reverse=True)
    # Para Almacenar as peliculas mas recomendadas
    recomendaciones = []
    # Ciclo por para iterar por las primeras 5 peliculas
    for pelicula in recomendadas[:5]: 
        score = df.loc[df['title'] == pelicula]['vote_average'].values[0]
        genres = df.loc[df['title'] == pelicula]['genre_names'].values[0]
        gen_str = ', '.join(genres).replace(',', '')
        recomendaciones.append(f"-{pelicula}  | Generos: {gen_str} | Puntaje: {score} |")
    return recomendaciones