

from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 
import plotly.express as px
import pandas as pd
import json
import os


# ToDo: Separate in different files !!



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


################################################ INTEGRATION ##########################################################



#Dictionary for options dropdown
opts = {'alive':'Total alive births','fetal':'Total fetal deaths',
        'no_fetal':'Total non-fetal deaths','deaths':'Total deaths',
        'fetal_percapita':'Fetal deaths per capita','no_fetal_percapita':'Non-fetal deaths per capita',
        'alive_percapita':'Alive births per capita','deaths_percapita':'Deaths per capita',
        'prob_alive':'Probability: Alive','prob_fetal':'Probability: Fetal death',
        'prob_no_fetal':'Probability: Non fetal death' }

dropDownOptions = [{'label':opts[key],'value':key} for key in opts.keys()]

#Slider marks:
sliderMarks = {year:{'label':str(year),'style':{'color':'#212529'}} for year in range(2008,2018,2)}


#Ctrols
ddlDataToShow = dcc.Dropdown(id='whichData',options=dropDownOptions, value='alive_percapita',clearable=False)
slrAge = dcc.Slider(min=2008,max=2017,step=1,id='fig-slider',value=2017,marks = sliderMarks)

#Todo: Create ddl with departments and callback to change map from here
btnBack = html.Button('Back to Colombia', id='backButt', n_clicks=0)



filters = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label("Data to show"),
                ddlDataToShow
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Year"),
                slrAge
            ]
        ),
        dbc.FormGroup(
            [
                btnBack
            ]
        ),
    ],
    body=True,
)


#######################################################################################################################################


upperContent = dbc.Col([filters],width='auto')

# dbc.Container([filters,html.Hr()],className="h-50"),
 #               style={'width':'320px'})

menu = dbc.Nav(
            [
                dbc.NavLink("Overview", href="/page-1", id="page-1-link"),
                dbc.NavLink("Analytics", href="/page-2", id="page-2-link"),
                dbc.NavLink("Recomendations", href="/page-3", id="page-3-link"),
            ],
            vertical=True,
            pills=True,
        )

sidebar = upperContent

