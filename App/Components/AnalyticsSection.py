

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
        [html.Div('Alive births per capita in Colombia, year 2017',id='mapFigTitle', className="card-text"),
        dcc.Graph(figure=mainMap, id='mainMap',style={"height":"500px"})])
    ],
    className="ml-1 h-100 p-3"    
)

secundary_card2 = dbc.Card(
    [
        dcc.Graph(figure=sideBars, id='sideBars',style={"height":"500px"})
        
    ],
    className="ml-1 h-100 pl-3"
)

leftCol = dbc.Col([mainMap_card],width='6')
rightCol = dbc.Col([secundary_card2])
main = dbc.Col([dbc.Row([leftCol,rightCol],className="h-75")])


# side = dbc.Col([dbc.Row([])],className='mt-1')

component = dbc.Row([SidebarSection.sidebar,main])