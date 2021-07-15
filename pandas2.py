#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 10:20:26 2021

@author: mauriciorestrepo
"""



import pandas as pd
import numpy as np
#archivo = '/Users/mauriciorestrepo/Desktop/Python/python-course/Programas Matemáticas.xlsx'
#df = pd.read_excel(archivo, sheet_name='Programas')
#print(df)


s = pd.DataFrame({
    'A1':[1, 2, 3, 4, 5],
    'A2':[10, 20, 30, 40, 50],
    'A3':['No', 'Si', 'Si', 'No', 'No']},
    index = ['Ene','Feb','Mar','Abr','May'])

print(s)

print(s.describe())

s.info()




#print(ventas.index)

#print(ventas.values)

#print(ventas.head())


#Método loc

print('loc[Ene] = ',s.loc['Ene'])

print('loc[[Ene],[Feb]] = ',s.loc[['Ene','Feb']])

print('loc[Ene:Abr] = ',s.loc['Ene':'Abr'])


#Método iloc


print('iloc[0] = ',s.iloc[0])
print('iloc[1] = ',s.iloc[1])

print('iloc[3] = ',s.iloc[3])
print('iloc[3:] = ',s.iloc[3:])
print('iloc[1:3] = ',s.iloc[1:3])