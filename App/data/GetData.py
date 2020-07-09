#! /usr/bin/env python3

import numpy as np
import geopandas as gpd
import pandas as pd
from sqlalchemy import create_engine, text

passw = '12345'
engine=create_engine(f'postgresql://team4:{passw}@ds4a-instance.c5zadjwjarvt.sa-east-1.rds.amazonaws.com/ds4afp', max_overflow=20)
def runQuery(sql):
    result = engine.connect().execution_options(isolation_level="AUTOCOMMIT").execute((text(sql)))
    return pd.DataFrame(result.fetchall(), columns=result.keys())

#Get data from DB
df = runQuery(
"""SELECT file_year AS year, id_birth ,resultado_emb, count(*) FROM eevv
GROUP BY file_year, resultado_emb, id_birth
""")

df['id_birth'] = df['id_birth'].apply(lambda x: str(x).zfill(5))

#GeoData: this contains names and codes
geo = gpd.read_file('../Data/GeoData/Municip.json')

#Create name column
df['mpio_name'] = df['id_birth'].copy().replace(geo['MPIO_CCNCT'].to_list(),geo['MPIO_CNMBR'].to_list())

df.to_csv('year_outcome_count.csv',index=False) #Save for later use 


######################### Load data
year_outcome_count_df = pd.read_csv('./data/year_outcome_count.csv',dtype={'year':int,'id_birth':str,'mpio_name':str,
                                                       'resultado_emb':'object','count':int}) 


year_outcome_count_df['dpto'] = year_outcome_count_df['id_birth'].apply(lambda x: x[:2])
year_outcome_count_df_ = year_outcome_count_df[year_outcome_count_df['resultado_emb'] == 'NACIDO_VIVO']

with open('../Data/GeoData/Municip.json', 'r') as f:
    munic = json.loads(f.read())

with open('../Data/GeoData/Dpto.json', 'r') as f:
    dpto = json.loads(f.read())

dptoCodeNames = pd.read_csv('../Data/GeoData/DptoCode_Names.csv')

########################## End loading data
