from fastapi import FastAPI
import pandas as pd
import numpy as np
import sklearn
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import randomized_svd
import uvicorn
import re


app = FastAPI()

df = pd.read_csv("Dataset/movies_dataset_trabajado.csv")

@app.get("/")
def read_root():
    return{"Hola!": "Bienvenido!"}

@app.get("/Peliculas_mes/{mes}")
def peliculas_mes(mes):
    '''Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes 
    (nombre del mes, en str, ejemplo 'enero') historicamente'''
    # Creamos un diccionario con los meses y su numero correspondiente
    meses = {'enero': 1.0, 'febrero': 2.0, 'marzo': 3.0, 'abril': 4.0, 'mayo': 5.0, 'junio': 6.0, 'julio': 7.0, 'agosto': 8.0,
             'septiembre': 9.0, 'octubre': 10.0, 'noviembre': 11.0, 'diciembre': 12.0}
    # Controlamos que el mes ingresado sea correcto
    if mes not in meses.keys():
        return ("Mes incorrecto! Debe ingresar un mes valido, por ejemplo: enero, febrero, marzo, etc.")
    # Filtramos por mes
    df_movies = df[df['release_month'] == meses[mes]]
    # Contamos la cantidad de peliculas
    cantidad = df_movies.shape[0]
    return {'mes': mes, 'cantidad': cantidad}

@app.get("/Peliculas_dia/{dia}")
def peliculas_dia(dia:str):
    '''Se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrenaron ese dia 
    (de la semana, en str, ejemplo 'lunes') historicamente'''
    # Creamos un diccionario con los dias y su numero correspondiente
    dias = {'lunes': 0.0, 'martes': 1.0, 'miercoles': 2.0, 'jueves': 3.0, 'viernes': 4.0, 'sabado': 5.0, 'domingo': 6.0}
    # Controlamos que el dia ingresado sea correcto
    if dia not in dias.keys():
        return ("Dia incorrecto! Debe ingresar un dia valido, por ejemplo: lunes, martes, miercoles, etc.")
    # Filtramos por dia
    df_movies = df[df['release_dayofweek'] == dias[dia]]
    # Contamos la cantidad de peliculas 
    cantidad = df_movies.shape[0]
    return {'dia': dia, 'cantidad': cantidad}

@app.get("/Franquicia/{franquicia}")
def franquicia(franquicia: str):
    '''Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio'''
    # Convertimos la franquicia a minusculas por si un usuario lo escribe en mayusculas
    franquicia = franquicia.lower()
    # Filtramos por franquicia
    df_movies = df[df['belongs_to_collection'] == franquicia]
    # Contamos la cantidad de peliculas
    cantidad = df_movies.shape[0]
    # Sumamos las ganancias
    ganancia_total = df_movies['revenue'].sum()
    # Calculamos la ganancia promedio
    ganancia_promedio = df_movies['revenue'].mean()
    return {'franquicia': franquicia, 'cantidad': cantidad, 'ganancia_total': ganancia_total,
            'ganancia_promedio': ganancia_promedio}

@app.get("/peliculas_pais/{pais}")
def peliculas_pais(pais:str):
    '''Se ingresa el pais y la funcion retorna la cantidad de peliculas que se estrenaron en el mismo 
    (nombre del pais, en str, ejemplo 'Argentina') historicamente'''
    # Convertimos el pais a minusculas por si un usuario lo escribe en mayusculas
    pais = pais.lower()
    # Filtramos por pais
    df_movies = df[df['production_countries'] == pais]
    # Contamos la cantidad de peliculas
    cantidad = df_movies.shape[0]
    return {'pais': pais, 'cantidad': cantidad}

@app.get("/productoras/{productora}")
def productoras(productora:str):
    '''Ingresas la productora, retornando la ganancia total y la cantidad de peliculas que produjeron'''
    #eliminamos los espacios en blanco al principio y al final
    productora = productora.strip()
    #Convertimos la productora a minusculas por si un usuario lo escribe en mayusculas
    productora = productora.lower()
    # Filtramos por productora
    df_movies = df[df['production_companies'] == productora]
    # Contamos la cantidad de peliculas
    cantidad = df_movies.shape[0]
    # Sumamos las ganancias
    ganancia_total = df_movies['revenue'].sum()
    return {'productora': productora, 'ganancia_total': ganancia_total, 'cantidad': cantidad}

@app.get("/retorno/{pelicula}")
def retorno(pelicula:str):
    #filtramos por pelicula
    df_movies = df[df['title'] == pelicula]
    #calculamos la inversion
    inversion = df_movies['budget'].sum()
    #calculamos la ganancia
    ganancia = df_movies['revenue'].sum()
    #calculamos el retorno
    retorno = ganancia/inversion
    #calculamos el año
    anio = df_movies['release_year'].mean()
    return {'pelicula':pelicula, 'inversion':inversion, 'ganacia':ganancia,'retorno':retorno, 'anio':anio}


# Recomendacion de peliculas
# Vectorización de los títulos
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['title'])

# Descomposición en valores singulares aleatorios (randomized SVD)
u, s, vt = randomized_svd(X, n_components=100)

# Cálculo de la similitud de coseno
def cosine_similarities(x, y):
    return np.dot(x, y.T)


# Recomendación de títulos similares
@app.get("/get_recomendacion/{title}")
def get_recommendacion(title):
    # Vectorización del título de entrada
    title_vec = vectorizer.transform([title])

    # Reducción de dimensionalidad del título de entrada
    title_vec_reduced = title_vec.dot(vt.T)

    # Cálculo de la similitud de coseno
    sim = cosine_similarities(title_vec_reduced, u.dot(np.diag(s)))

    # Ordenamiento de los títulos según su similitud de coseno
    sim_scores = list(enumerate(sim[0]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Recomendación de títulos similares
    sim_scores = sim_scores[1:6]
    indices = [i[0] for i in sim_scores]
    titles = df.iloc[indices]['title']

    return {'recomendacion':titles.tolist()}

