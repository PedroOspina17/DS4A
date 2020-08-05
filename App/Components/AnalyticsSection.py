

from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 
import plotly.express as px
import pandas as pd
import json
import os
from Components import MapCharts,SidebarSection,HorizontalBars


mainMap = MapCharts.fig
sideBars = HorizontalBars.fig

mainMap_card = dbc.Card(
    [
        dbc.CardBody(
        [html.Div('Alive births per capita in Colombia, year 2017',id='mapFigTitle', className="bigTitles"),
        dcc.Graph(figure=mainMap, id='mainMap',style={"height":"500px"})])
    ],
    className="ml-1 h-100 p-3"    
)

secundary_card2 = dbc.Card(
    [
        dbc.CardBody(
        [html.Div('Top 15',id='barPlotTitle', className="bigTitles"),
        dcc.Graph(figure=sideBars, id='barPlot',style={"height":"500px"})])
        
    ],
    className="ml-1 h-100 pl-3"
)

leftCol = dbc.Col([mainMap_card],width='5')
rightCol = dbc.Col([secundary_card2],width='4')


component = dbc.Row([SidebarSection.sidebar,leftCol,rightCol])
