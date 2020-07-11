import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import pandas as pd
import json 
import plotly.express as px
import dash_html_components as html
import dash_core_components as dcc


############### Load data
perCapDptos = pd.read_csv('./data/OutcomePerCapitaDptos.csv')
perCapDptos.cod_dpto = perCapDptos.cod_dpto.astype(str).str.zfill(2)

with open('../Data/GeoData/Dpto.json', 'r') as f:
    Dpto = json.loads(f.read())
###############

df_slice = perCapDptos[perCapDptos['year'] == 2017].groupby(['cod_dpto','DPNOM']).mean().reset_index()

mapFig = px.choropleth_mapbox(df_slice,
           locations='cod_dpto',
           color='alive',
           geojson=Dpto,
           zoom=4,
           mapbox_style="carto-positron",
           featureidkey = 'properties.DPTO_CCDGO',
           color_continuous_scale="PuRd",
           center={'lat':4,'lon':-75},
           hover_name='DPNOM',
           opacity=0.7)

mapFig.update_layout(margin={'l':0,'r':0,'t':10,'b':5},
                     paper_bgcolor="#2F4F4F",
                     font={'family':"Courier New, monospace",
                           'size':18,
                           'color':"#F0FFFF"})

fig = html.Div([
      dcc.Graph(figure=mapFig, id='mainMap')
               ], className="main-map")
