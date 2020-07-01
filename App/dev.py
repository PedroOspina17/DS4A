#!/usr/bin/env python3

import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import json
from sqlalchemy import create_engine, text

engine=create_engine('postgresql://team4:pass@ds4a-instance.c5zadjwjarvt.sa-east-1.rds.amazonaws.com/ds4afp', max_overflow=20)
def runQuery(sql):
    result = engine.connect().execution_options(isolation_level="AUTOCOMMIT").execute((text(sql)))
    return pd.DataFrame(result.fetchall(), columns=result.keys())


#Create the app
app = dash.Dash(__name__)

with open('../Data/GeoData/Municip.json', 'r') as f:
    geojson = json.loads(f.read())

#Load data

df = runQuery(
"""SELECT file_year, id_birth ,resultado_emb, count(*) FROM eevv
GROUP BY file_year, resultado_emb, id_birth
""")
df['dpto'] = df['id_birth'].apply(lambda x: x[:2])
df_ = df[df['resultado_emb'] == 'NACIDO_VIVO']

#First map
def figmap_munic(year,dpto='05'):
    dat = df_[(df_['dpto'] == dpto) & (df_['file_year'] == year)]

    return px.choropleth_mapbox(dat,
           locations='id_birth',
           color='count',
           geojson=geojson,
           zoom=6,
           mapbox_style="carto-positron", 
           featureidkey = 'properties.MPIO_CCNCT',
           color_continuous_scale="PuRd",
           center={'lat':7,'lon':-73},
           opacity=0.5)

#Create Layout
app.layout = html.Div([
    html.H2("Number of births per municipe", id='title'), #Creates the title of the app

    dcc.Slider(min=2008,max=2018,step=1,id='fig-slider',value=0,
                marks={2008:'2008',2010:'2010',2012:'2012',2014:'2014',2016:'2016',2018:'2018'}),
    dcc.Graph(figure=figmap_munic(2018,'05'), id='main-figure')
])


@app.callback(
    Output('main-figure','figure'),
    [Input('fig-slider','value')])
def slider_interaction(slider_val):
    return figmap_munic(slider_val,dpto='05')


#Initiate the server where the app will work
if __name__ == "__main__":
    app.run_server(debug=True)
