import pandas as pd
import json 

print("load data")
perCapMunic = pd.read_csv('../App/data/OutcomePerCapitaMunic.csv')
perCapDptos = pd.read_csv('../App/data/OutcomePerCapitaDptos.csv')
perCapMunic.cod_dpto = perCapMunic.cod_dpto.astype(str).str.zfill(2)
perCapMunic.id_birth = perCapMunic.id_birth.astype(str).str.zfill(5)
perCapDptos.cod_dpto = perCapDptos.cod_dpto.astype(str).str.zfill(2)

with open('../Data/GeoData/Dpto.json', 'r') as f:
    Dpto = json.loads(f.read())
    
with open('../Data/GeoData/Municip.json', 'r') as f:
    Munic = json.loads(f.read())

    

print("depto shape = ",perCapDptos.shape)
print("munic shape = ",perCapMunic.shape)