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
    return {'message': 'Bienvenido a la API de películas, por Carlos Sanchez'}


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
    franquicia_df = df[df['collection_name'].str.contains(franquicia, na=False)]

    cantidad = len(franquicia_df)

    ganancia_total = franquicia_df['revenue'].sum()
    ganancia_promedio = franquicia_df['revenue'].mean()

    return {'franquicia': franquicia, 'cantidad': cantidad, 'ganancia_total': ganancia_total, 'ganancia_promedio': ganancia_promedio}


@app.get('/peliculas_pais/{pais}')
async def peliculas_pais(pais):
    df = pd.read_csv('Dataset/df.csv')

    df = df.dropna(subset=['production_countries_names'])
    df = df.drop_duplicates()

    num_peliculas = 0
    for countries in df['production_countries_names']:
        if pais in countries:
            num_peliculas += 1

    return {'pais': pais, 'cantidad': num_peliculas}


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
    k = 10
    knn = NearestNeighbors(n_neighbors=k+1, algorithm='auto')
    knn.fit(generodf)
    indices = knn.kneighbors(generodf.loc[df['title'] == titulo])[1].flatten()
    recomendadas = list(df.iloc[indices]['title'])
    recomendadas = sorted(recomendadas, key=lambda x: df.loc[df['title'] == x]['vote_average'].values[0], reverse=True)[:5]
    return {'recomendacion': recomendadas}