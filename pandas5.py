#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 19:33:06 2021

@author: mauriciorestrepo
"""

import pandas as pd
import numpy as np

import requests


url = 'https://raw.githubusercontent.com/MRestrepo08/Pandas/main/Libro3.xlsx'


target_path = "Libro3.xlsx"

response = requests.get(url)
response.raise_for_status()    # Check that the request was successful
with open(target_path, "wb") as f:
    f.write(response.content)
print("Download ready.")

#Fix precision

pd.set_option('display.precision', 2)


#archivo = '/Users/mauriciorestrepo/Desktop/Python/python-course/Libro3.csv'


df = pd.read_excel('Libro3.xlsx')
print(df.head())
print(df.info())


#Guardar un excel

#df.to_excel('example.xlsx', sheet_name='Hoja1')


#Estadística básica


print(df.describe())

#Explorando


#Conteos, frecuencias


print(df['MODALIDAD'].value_counts())

print(df['NIVEL_DE_FORMACIÓN'].value_counts())

#Búsquedas en el dataset

current_decade = df[df["CAMPO_DETALLADO"] == 'Matemáticas']
print('Matemáticas = ',current_decade.shape)

print(df[
    (df["CAMPO_DETALLADO"] == 'Matemáticas') &
    (df["NIVEL_ACADÉMICO"] == 'Pregrado') &
    (df["SECTOR"] == 'Oficial') &
    (df["NÚMERO_CRÉDITOS"] > 138)
])

#Columnas. Crear una copia del dataset

df1 = df.copy()
print(df.shape)

#renombrar columnas

#renamed_df = df.rename(columns={"game_result": "result", "game_location": "location"})

#Eliminar columnas

df2 = df[
    (df["CAMPO_DETALLADO"] == 'Matemáticas') &
    (df["NIVEL_ACADÉMICO"] == 'Pregrado') &
    (df["SECTOR"] == 'Oficial') &
    (df["NÚMERO_CRÉDITOS"] > 138)
]  


#Guardar un excel

df2.to_excel('consulta.xlsx', sheet_name='Hoja1')


elim_columns = ["CÓDIGO_INSTITUCIÓN_PADRE", "CÓDIGO_INSTITUCIÓN", "ESTADO_INSTITUCIÓN", "PERIODICIDAD"]
df1.drop(elim_columns, inplace=True, axis=1)
print(df.shape)

#Crear nuevas columnas

df['COSTO_POR_CREDITOS'] = df.COSTO_MATRÍCULA_ESTUD_NUEVOS/df.NÚMERO_CRÉDITOS
print(df.shape)

#Tipos de datos

print(df.info())


####Formato

#df["date_game"] = pd.to_datetime(df["date_game"])
#df["game_location"] = pd.Categorical(df["game_location"])

#print(df.info())


#Pre-procesamiento. Datos faltantes


data_without_missing_columns = df1.dropna(axis=1)
print('Miss = ', data_without_missing_columns.shape)

#Visualización de los datos

#matplotlib inline

#df[df["fran_id"] == "Knicks"].groupby("year_id")["pts"].sum().plot()

df1['SECTOR'].value_counts().head(10).plot(kind="bar")