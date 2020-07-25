import pandas as pd
import json 

perCapMunic = pd.read_csv('../App/Data/OutcomePerCapitaMunic.csv')
perCapDptos = pd.read_csv('../App/Data/OutcomePerCapitaDptos.csv')
perCapMunic.cod_dpto = perCapMunic.cod_dpto.astype(str).str.zfill(2)
perCapMunic.id_birth = perCapMunic.id_birth.astype(str).str.zfill(5)
perCapDptos.cod_dpto = perCapDptos.cod_dpto.astype(str).str.zfill(2)

with open('../App/Data/Dpto.json', 'r') as f:
    Dpto = json.loads(f.read())
    
with open('../App/Data/Municip.json', 'r') as f:
    Munic = json.loads(f.read())

