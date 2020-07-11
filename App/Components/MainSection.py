

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
    style={"width": "99%"},
)


secundary_card = dbc.Card(
    [
        dbc.CardBody(html.P("Pregnancy outcomes by department", className="card-text")),
        dbc.CardImg(src="/assets/images/map2.png", bottom=True),
    ],
    className="mt-4 ml-2",
    style={"width": "20rem"},
)



bottom_card = dbc.Row([dbc.Col(secundary_card, width="auto"), dbc.Col(secundary_card, width="auto"), dbc.Col(secundary_card, width="auto")])

main = dbc.Col([mainMap_card,bottom_card], width="auto", className="mt-5")
