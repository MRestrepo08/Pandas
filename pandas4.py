#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 10:20:26 2021

@author: mauriciorestrepo
"""

import pandas as pd
import numpy as np

import requests

download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
target_csv_path = "nba_all_elo.csv"

response = requests.get(download_url)
response.raise_for_status()    # Check that the request was successful
with open(target_csv_path, "wb") as f:
    f.write(response.content)
print("Download ready.")

#Fix precision

pd.set_option('display.precision', 2)

nba = pd.read_csv("nba_all_elo.csv")
print(nba.head())
print(nba.info())

#Basic statistics

print(nba.describe())

#Exploring

##Counts, frecuencies

print(nba['team_id'].value_counts())

print(nba['fran_id'].value_counts())

#Searching

current_decade = nba[nba["year_id"] > 2010]
print('2010 = ',current_decade.shape)

print(nba[
    (nba["_iscopy"] == 0) &
    (nba["pts"] > 100) &
    (nba["opp_pts"] > 100) &
    (nba["team_id"] == "BLB")
])

#Columns. Copy the dataset

df = nba.copy()
print(df.shape)

#Columns rename

renamed_df = df.rename(columns={"game_result": "result", "game_location": "location"})

#Drop columns


elo_columns = ["elo_i", "elo_n", "opp_elo_i", "opp_elo_n"]
df.drop(elo_columns, inplace=True, axis=1)
print(df.shape)

#Create new columns

df['Diferencia'] = df.pts - df.opp_pts
print(df.shape)

#Data Type

print(df.info())


####Format

df["date_game"] = pd.to_datetime(df["date_game"])
df["game_location"] = pd.Categorical(df["game_location"])

print(df.info())


#Pre-procesing. Missing Data


data_without_missing_columns = nba.dropna(axis=1)
print('Miss = ', data_without_missing_columns.shape)

#Data visualization

matplotlib inline

nba[nba["fran_id"] == "Knicks"].groupby("year_id")["pts"].sum().plot()

nba["fran_id"].value_counts().head(10).plot(kind="bar")
