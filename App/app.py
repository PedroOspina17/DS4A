#!/usr/bin/env python3

import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 
import plotly.express as px
import pandas as pd
import json
import os







#Create the app
# app = dash.Dash(__name__)
app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP]) #USING BOOTSTRAP'S CSS LIBRARY

########################################### Side bar #####################################################

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




########################################### Main section #####################################################

main_card = dbc.Card(
    [
        dbc.CardBody(html.P("Pregnancy outcomes history", className="card-text")),
        dbc.CardImg(src="/assets/images/mainGraph.png", bottom=True),
    ],
    className="ml-2",
    style={"width": "91%"},
)

bottom_card = dbc.Card(
    [
        dbc.CardBody(html.P("Pregnancy outcomes by department", className="card-text")),
        dbc.CardImg(src="/assets/images/map2.png", bottom=True),
    ],
    className="mt-4 ml-2",
    style={"width": "20rem"},
)



cards = dbc.Row([dbc.Col(bottom_card, width="auto"), dbc.Col(bottom_card, width="auto"), dbc.Col(bottom_card, width="auto")])

main = dbc.Col([main_card,cards], width="auto", className="mt-5")

########################################### Footer #####################################################
footer = html.Div("Team 4 -- Borns AI", className ="mx-auto font-weight-bold fot-italic mt-5 text-muted")
########################################### App layout #####################################################
app.layout =  html.Div([
    dbc.Row(
            [
                sidebar,
                main,
                footer
            ]
        )
    
],className="h-100")



# html.Div([
#                         html.Div([
#                             html.Div(html.H1("Number of births per municipality", id='title'),className='main-title'),
#                             html.Div(id='dd-output-container'),

#                             html.Div([html.Div([dcc.Dropdown(id='selectDpto',options=dropDownOptions, value='05'),
#                                                 dcc.Graph(figure=mapFig,id='main-figure'),
#                                                 html.Div(dcc.Slider(min=2008,max=2018,step=1,id='fig-slider',value=2018,
#                                                     marks = sliderMarks),
#                                                 className='slider')],
#                                             className='main-figure'),

#                                       html.Div([dcc.Graph(figure=mapFig,id='dummy')],className='main-figure')
#                             ],className='map-container'),

#                     ],className="t4-app")
#             ])




#Initiate the server where the app will work
if __name__ == "__main__":
    app.run_server(debug=True)
