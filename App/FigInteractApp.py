#!/usr/bin/env python3

import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import json
import os
from dash.exceptions import PreventUpdate
from components import MapCharts

#Create the app
app = dash.Dash(__name__)



#Dictionary for options dropdown
opts = {'alive':'Total alive births','fetal':'Total fetal deaths',
        'no_fetal':'Total non-fetal deaths','deaths':'Total deaths',
        'fetal_percapita':'Fetal deaths per capita','no_fetal_percapita':'Non-fetal deaths per capita',
        'alive_percapita':'Alive births per capita','deaths_percapita':'Deaths per capita'}
dropDownOptions = [{'label':opts[key],'value':key} for key in opts.keys()]

#Slider marks:
sliderMarks = {year:{'label':str(year),'style':{'color':'#F0FFFF'}} for year in range(2008,2018,2)}

#Create Layout
app.layout =  html.Div([
                        html.Div([
                            html.Div(html.H1("Number of births per municipality", id='title'),className='main-title'),

                            html.Div([dcc.Dropdown(id='whichData',options=dropDownOptions, value='alive',clearable=False),
                                      MapCharts.fig,
                                      dcc.Slider(min=2008,max=2017,step=1,id='fig-slider',value=2017,marks = sliderMarks),
                                    ], className='main-figure'),

                            html.Div([html.Button('Back to Colombia', id='backButt', n_clicks=0)],className='resetButton')
                                ],className='map-container'),

                    ],className="t4-app")



######################################
############### Load data
perCapMunic = pd.read_csv('../App/data/OutcomePerCapitaMunic.csv')
perCapDptos = pd.read_csv('../App/data/OutcomePerCapitaDptos.csv')
perCapMunic.cod_dpto = perCapMunic.cod_dpto.astype(str).str.zfill(2)
perCapMunic.id_birth = perCapMunic.id_birth.astype(str).str.zfill(5)
perCapDptos.cod_dpto = perCapDptos.cod_dpto.astype(str).str.zfill(2)

with open('../Data/GeoData/Dpto.json', 'r') as f:
    Dpto = json.loads(f.read())
    
with open('../Data/GeoData/Municip.json', 'r') as f:
    Munic = json.loads(f.read())

######################## Callbacks

#Main map callback

## Variables to be set as global
currDptoData = 0     #Variable to hold data for only one dpto so query is faster when changing years. 
dptoMap = True       #Tell if we're currently at a full Colombia map

@app.callback(
    Output('mainMap','figure'),
    [Input('fig-slider','value'),Input('whichData','value'),Input('mainMap','clickData'),Input('backButt','n_clicks')],
    [State('mainMap','figure')])
def slider_interaction(year,PlotVariable,click,button,figure):
    global currDptoData,dptoMap

    #Tell which input was triggered
    ctx = dash.callback_context

    #If dpto was changed  redraw for this dpto.
    if ctx.triggered[0]['prop_id'] == 'mainMap.clickData':
        if dptoMap:  #and if a dpto (not a munic) was selected

            #Define new dpto 
            dpto = click['points'][0]['location']
            dptoMap = False # This is now a municipal map (not full Colombia)

            currDptoData = perCapMunic[perCapMunic['cod_dpto'] == dpto] 
            newData = currDptoData[(perCapMunic['year'] == year)]
    
            fig = px.choropleth_mapbox(newData,
                       locations='id_birth',
                       color=PlotVariable,
                       geojson=Munic,
                       zoom=4,
                       mapbox_style="carto-positron", 
                       featureidkey = 'properties.MPIO_CCNCT',
                       color_continuous_scale="PuRd",
                       center={'lat':4,'lon':-75},
                       hover_name='mpio_name',
                       opacity=0.5)
            fig.update_layout(margin={'l':0,'r':0,'t':10,'b':5},
                                 paper_bgcolor="#2F4F4F",
                                 font={'family':"Courier New, monospace",
                                       'size':18,
                                       'color':"#F0FFFF"})
            return fig

        #If click on municip, do nothing
        else:
            raise PreventUpdate
        
    #If year or data to plot (dropDown) are changed, then modify data (not map)
    elif ctx.triggered[0]['prop_id'] == 'fig-slider.value' or ctx.triggered[0]['prop_id'] == 'whichData.value':

        if figure['data']: #(if only year was changed), change only data
            if dptoMap: #If current map is departamental (full Colombia)
                newData = perCapDptos[perCapDptos['year'] == year]
            else:  #If map is a municipal one:
                newData = currDptoData[currDptoData['year'] == year]   #Use already sliced data for this dpto.
                
            figure['data'][0]['z'] = newData[PlotVariable]
            return figure

    #If back button is pressed, then reset the map
    elif ctx.triggered[0]['prop_id'] == 'backButt.n_clicks':
        dptoMap = True   #We're back to full Colombia
        return MapCharts.mapFig

    else:
        return figure

###################### End callbacks



#Initiate the server where the app will work
if __name__ == "__main__":
    app.run_server(debug=True)
