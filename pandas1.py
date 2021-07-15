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


s1 = pd.Series([1, 2, 3, 4], index =['a','b','c','d'])
s2 = pd.Series([10, 20, 30, 40], index =['a','b','c','d'])
s = pd.DataFrame({'A1':s1,'A2':s2})
print(s.describe())
s.info()

print(s)


#print(ventas.index)

#print(ventas.values)

#print(ventas.head())


#Método loc

print('loc[b] = ',s.loc['b'])

print('loc[[b],[c]] = ',s.loc[['b','c']])

print('loc[b:d] = ',s.loc['b':'d'])


#Método iloc


print('iloc[1:] = ',s.iloc[1:])
print('iloc[:1] = ',s.iloc[:1])


