#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 10:20:26 2021

@author: mauriciorestrepo
"""

import pandas as pd
import numpy as np

df1= pd.DataFrame(np.arange(9).reshape(3,3),
                  index = ['a','b','d'],
                  columns= ['A','B','C'])
print(df1)

df2= pd.DataFrame(np.arange(12).reshape(4,3),
                  index = ['a','b','c','e'],
                  columns= ['A','C','D'])
print(df2)

df3 = pd.concat([df1,df2], sort = False)

print(df3)

df4 = pd.concat([df1,df2], axis = 1, sort = False)

print(df4)
