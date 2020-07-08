#!/usr/bin/env python3

import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import json
import os

######################### Load data
df = pd.read_csv('./data/year_outcome_count.csv',dtype={'year':int,'id_birth':str,'mpio_name':str,
                                                       'resultado_emb':'object','count':int}) 


df['dpto'] = df['id_birth'].apply(lambda x: x[:2])
df_ = df[df['resultado_emb'] == 'NACIDO_VIVO']

with open('../Data/GeoData/Municip.json', 'r') as f:
    munic = json.loads(f.read())

with open('../Data/GeoData/Dpto.json', 'r') as f:
    dpto = json.loads(f.read())

dptoCodeNames = pd.read_csv('../Data/GeoData/DptoCode_Names.csv')

########################## End loading data




#Create the app
app = dash.Dash(__name__)

#First map
dat = df_[(df_['dpto'] == '05') & (df_['year'] == 2018)]
mapFig=  px.choropleth_mapbox(dat,
           locations='id_birth',
           color='count',
           geojson=munic,
           zoom=6,
           mapbox_style="carto-positron", 
           featureidkey = 'properties.MPIO_CCNCT',
           color_continuous_scale="PuRd",
           center={'lat':6.5,'lon':-75},
           hover_name='mpio_name',
           opacity=0.7)

mapFig.update_layout(margin={'l':0,'r':0,'t':10,'b':5},
                     paper_bgcolor="#2F4F4F",
                     font={'family':"Courier New, monospace",
                           'size':18,
                           'color':"#F0FFFF"})

#Dropdown for departments dictionary
dropDownOptions = [{'label':dptoCodeNames.iloc[i].Name,'value':dptoCodeNames.iloc[i].code} for i in dptoCodeNames.index]

#Slider marks:
sliderMarks = {year:{'label':str(year),'style':{'color':'#F0FFFF'}} for year in range(2008,2019,2)}

#Create Layout
app.layout =  html.Div([
                        html.Div([
                            html.Div(html.H1("Number of births per municipality", id='title'),className='main-title'),
                            html.Div(id='dd-output-container'),

                            html.Div([html.Div([dcc.Dropdown(id='selectDpto',options=dropDownOptions, value='05'),
                                                dcc.Graph(figure=mapFig,id='main-figure'),
                                                html.Div(dcc.Slider(min=2008,max=2018,step=1,id='fig-slider',value=2018,
                                                    marks = sliderMarks),
                                                className='slider')],
                                            className='main-figure'),

                                      html.Div([dcc.Graph(figure=mapFig,id='dummy')],className='main-figure')
                            ],className='map-container'),

                    ],className="t4-app")
            ])


@app.callback(
    Output('main-figure','figure'),
    [Input('fig-slider','value'),Input('selectDpto','value')],
    [State('main-figure','figure')])
def slider_interaction(year,dpto,figure):
    dpto = str(dpto).zfill(2)
    newData = df_[(df_['dpto'] == dpto) & (df_['year'] == year)]

    #Tell which input was triggered
    ctx = dash.callback_context
    #If dpto was changed, redraw for this dpto.
    if ctx.triggered[0]['prop_id'] == 'selectDpto.value':

        fig = px.choropleth_mapbox(newData,
                   locations='id_birth',
                   color='count',
                   geojson=munic,
                   zoom=6,
                   mapbox_style="carto-positron", 
                   featureidkey = 'properties.MPIO_CCNCT',
                   color_continuous_scale="PuRd",
                   center={'lat':7,'lon':-73},
                   hover_name='mpio_name',
                   opacity=0.5)
        fig.update_layout(margin={'l':0,'r':0,'t':10,'b':5},
                             paper_bgcolor="#2F4F4F",
                             font={'family':"Courier New, monospace",
                                   'size':18,
                                   'color':"#F0FFFF"})
        return fig
        
    elif figure['data']: #Else, change only data
        figure['data'][0]['z'] = newData['count']
        return figure



#Initiate the server where the app will work
if __name__ == "__main__":
    app.run_server(debug=True)
