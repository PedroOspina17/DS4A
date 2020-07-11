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


from Components import SidebarSection, MainSection 




#Create the app
# app = dash.Dash(__name__)
app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP]) #USING BOOTSTRAP'S CSS LIBRARY




footer = html.Div("Team 4 -- Borns AI", className ="mx-auto font-weight-bold fot-italic mt-5 text-muted")

app.layout =  html.Div([
    dbc.Row(
            [
                SidebarSection.sidebar,
                MainSection.main,
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
