import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import pandas as pd
import json 
import plotly.express as px
import dash_html_components as html
import dash_core_components as dcc
from Components import LoadData as d
print("Mapchart")
print("depto shape = ",d.perCapDptos.shape)
print("munic shape = ",d.perCapMunic.shape)
df_slice = d.perCapDptos[d.perCapDptos['year'] == 2017].groupby(['cod_dpto','DPNOM']).mean().reset_index()

fig = px.choropleth_mapbox(df_slice,
           locations='cod_dpto',
           color='alive_percapita',
           geojson=d.Dpto,
           zoom=4,
           mapbox_style="carto-positron",
           featureidkey = 'properties.DPTO_CCDGO',
           color_continuous_scale="PuRd",
           center={'lat':4,'lon':-75},
           hover_name='DPNOM',
           opacity=0.7)

fig.update_layout(margin={'l':0,'r':0,'t':0,'b':0},
                     paper_bgcolor="white",
                     font={'family':"Courier New, monospace",
                           'size':18,
                           'color':"#212529"})


