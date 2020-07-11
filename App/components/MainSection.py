

from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 
import plotly.express as px
import pandas as pd
import json
import os


mainMap = dbc.CardImg(src="/assets/images/mainGraph.png", bottom=True)


mainMap_card = dbc.Card(
    [
        dbc.CardBody(html.P("Pregnancy outcomes history", className="card-text")),
        mainMap,
    ],
    className="ml-2",
    style={"width": "91%"},
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