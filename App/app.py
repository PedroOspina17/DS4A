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
from dash.exceptions import PreventUpdate
from Components import LoadData as d
from Components import MainSection,SidebarSection 


print("StartApp")

#Create the app
app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP]) #USING BOOTSTRAP'S CSS LIBRARY



####################################################### Layout ###################################################
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



###################################################### Callbacks ###################################################


currDptoData = 0     #Variable to hold data for only one dpto so query is faster when changing years. 
dptoMap = True       #Tell if we're currently at a full Colombia map

@app.callback(
    Output('mainMap','figure'),
    [Input('fig-slider','value'),Input('whichData','value'),Input('mainMap','clickData'),Input('backButt','n_clicks')],
    [State('mainMap','figure')])
def slider_interaction(year,PlotVariable,click,button,figure):
    global currDptoData,dptoMap
    print("call1")
#     print(MainSection.mainMap)
    #Tell which input was triggered
    ctx = dash.callback_context
    print(ctx.triggered)
    #If dpto was changed  redraw for this dpto.
    if ctx.triggered[0]['prop_id'] == 'mainMap.clickData':
        print("call4")
        if dptoMap:  #and if a dpto (not a munic) was selected

            #Define new dpto 
            dpto = click['points'][0]['location']
            dptoMap = False # This is now a municipal map (not full Colombia)

            currDptoData = d.perCapMunic[d.perCapMunic['cod_dpto'] == dpto] 
            newData = currDptoData[(d.perCapMunic['year'] == year)]
    
            fig = px.choropleth_mapbox(newData,
                       locations='id_birth',
                       color=PlotVariable,
                       geojson=d.Munic,
                       zoom=4,
                       mapbox_style="carto-positron", 
                       featureidkey = 'properties.MPIO_CCNCT',
                       color_continuous_scale="PuRd",
                       center={'lat':4,'lon':-75},
                       hover_name='mpio_name',
                       opacity=0.5)
            fig.update_layout(margin={'l':0,'r':0,'t':10,'b':5},
                                 paper_bgcolor="white",
                                 font={'family':"Courier New, monospace",
                                       'size':18,
                                       'color':"#F0FFFF"})
            return fig

        #If click on municip, do nothing
        else:
            raise PreventUpdate
        
    #If year or data to plot (dropDown) are changed, then modify data (not map)
    elif ctx.triggered[0]['prop_id'] == 'fig-slider.value' or ctx.triggered[0]['prop_id'] == 'whichData.value':
        print("call3")
        if figure['data']: #(if only year was changed), change only data
            if dptoMap: #If current map is departamental (full Colombia)
                newData = d.perCapDptos[d.perCapDptos['year'] == year]
            else:  #If map is a municipal one:
                newData = currDptoData[currDptoData['year'] == year]   #Use already sliced data for this dpto.
                
            figure['data'][0]['z'] = newData[PlotVariable]
            return figure

    #If back button is pressed, then reset the map
    elif ctx.triggered[0]['prop_id'] == 'backButt.n_clicks':
        print("call2")
        dptoMap = True   #We're back to full Colombia
        return MainSection.mainMap

    else:
        return figure
        
    
###################################################### Run the server #########################################################


#Initiate the server where the app will work
if __name__ == "__main__":
    app.run_server(debug=True)