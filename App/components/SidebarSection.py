

from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 
import plotly.express as px
import pandas as pd
import json
import os

# ToDo: Separate in different files !!
title = dbc.Container([ html.H1("Borns AI", className="ml-3 mt-3"),html.Hr()])


filters = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label("X variable"),
                dcc.Dropdown(
                    id="x-variable",
                    options=[
                        {"label": "option {}".format(col), "value": col} for col in range(10)
                    ],
                    value=1,
                ),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Y variable"),
                dcc.Dropdown(
                    id="y-variable",
                    options=[
                        {"label": "option {}".format(col), "value": col} for col in range(10)
                    ],
                    value=1,
                ),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("temp filter"),
                dbc.Input(id="cluster-count", type="number", value=3),
            ]
        ),
    ],
    body=True,
)

upperContent = dbc.Row(dbc.Col(
    dbc.Container([filters,html.Hr()],className="h-50")
    , width="auto"))



menu = dbc.Row(dbc.Col(
    dbc.ListGroup([
        dbc.ListGroupItem("Active item", active=True),
        dbc.ListGroupItem("Item 2"),
        dbc.ListGroupItem("Item 3"),
    ]), width="auto")
,className="h-50 ml-4")


sidebar = dbc.Col([title,upperContent,menu], width=2)

