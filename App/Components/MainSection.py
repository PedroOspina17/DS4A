

from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 
import plotly.express as px
import pandas as pd
import json
import os
from Components import MapCharts


mainMap = MapCharts.fig


mainMap_card = dbc.Card(
    [
        dbc.CardBody(html.Div('Alive births per capita in Colombia, year 2017',id='mapFigTitle', className="card-text")),
        dcc.Graph(figure=mainMap, id='mainMap',className="h-100"    )
    ],
    className="ml-2 h-100 p-5"    
)

secundary_card2 = dbc.Card(
    [
        dbc.CardBody(html.P("Stats", className="card-text")),
        dbc.Row([dbc.CardImg(src="/assets/images/Stats2.png")],className='ml-5', style={"width": "90%"}),
        dbc.Row([dbc.CardImg(src="/assets/images/Stats3.png")],className='mt-5 ml-5', style={"width": "90%"}),
    ],
    className="ml-2 h-100 p-5"
)

leftCol = dbc.Col([mainMap_card],width='6')
rightCol = dbc.Col([secundary_card2])
main = dbc.Col([dbc.Row([leftCol,rightCol])],className='mt-1')

