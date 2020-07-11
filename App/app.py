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


######################## Callbacks

#Main map callback
@app.callback(
    Output('main-map','figure'),
    [Input('fig-slider','value'),Input('selectDpto','value')],
    [State('main-map','figure')])
def slider_interaction(year,dpto,figure):
    dpto = str(dpto).zfill(2)


    #Tell which input was triggered
    ctx = dash.callback_context
    #If dpto was changed, redraw for this dpto.
    if ctx.triggered[0]['prop_id'] == 'selectDpto.value':
        newData = perCapMunic[(perCapMunic['cod_dpto'] == dpto) & (perCapMunic['year'] == year)]

        fig = px.choropleth_mapbox(newData,
                   locations='id_birth',
                   color='count',
                   geojson=Munic,
                   zoom=4,
                   mapbox_style="carto-positron", 
                   featureidkey = 'properties.MPIO_CCNCT',
                   color_continuous_scale="PuRd",
                   center={'lat':4,'lon':-75},
                   #hover_name='mpio_name',
                   opacity=0.5)
        fig.update_layout(margin={'l':0,'r':0,'t':10,'b':5},
                             paper_bgcolor="#2F4F4F",
                             font={'family':"Courier New, monospace",
                                   'size':18,
                                   'color':"#F0FFFF"})
        return fig
        
    elif figure['data']: #Else (if only year was changed), change only data
        if dpto == None: #If current map is departamental
            newData = perCapDptos[perCapDptos['year'] == year]
        else:  #If map is a municipal one:
            newData = perCapMunic[(perCapMunic['cod_dpto'] == dpto) & (perCapMunic['year'] == year)]
            
        figure['data'][0]['z'] = newData['count']
        return figure

###################### End callbacks


#Initiate the server where the app will work
if __name__ == "__main__":
    app.run_server(debug=True)
