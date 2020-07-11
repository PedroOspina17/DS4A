

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
        dcc.Graph(figure=mainMap, id='mainMap')
    ],
    className="ml-2",
    style={"width": "35rem",'height':'auto'},
)

secundary_card2 = dbc.Card(
    [
        dbc.CardBody(html.P("Stats", className="card-text")),
        dbc.CardImg(src="/assets/images/Stats2.png"),
        dbc.CardImg(src="/assets/images/Stats3.png"),
    ],
    className="mt-4 ml-2",
    style={"width": "20rem",'height':'auto'},
)

rightCol = dbc.Col([secundary_card2],width='auto')
main = dbc.Row([mainMap_card,rightCol],className='mt-5')

