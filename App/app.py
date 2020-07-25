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



#Create the app
app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP]) #USING BOOTSTRAP'S CSS LIBRARY



####################################################### Layout ###################################################
footer = html.Div("Team 4 -- Borns AI", className ="mx-auto font-weight-bold fot-italic mt-5 text-muted")

app.layout =  html.Div([
    dbc.Col([
        dbc.Row(
                [
                    SidebarSection.sidebar,
                    MainSection.main,
                ]
            ), 
       footer])
    
],className="h-100")



###################################################### Callbacks ###################################################
## Update main map and map title
titleNamesDict = {value:label for value,label in SidebarSection.opts.items()}

currDptoData = 0     #Variable to hold data for only one dpto so query is faster when changing years. 
dptoMap = True       #Tell if we're currently at a full Colombia map
region = 'Colombia'  #Variable to hold region name (be it Colombia or a specific dpto)

@app.callback(
    [Output('mainMap','figure'),Output('mapFigTitle','children')],
    [Input('fig-slider','value'),Input('whichData','value'),Input('mainMap','clickData'),Input('backButt','n_clicks')],
    [State('mainMap','figure')])
def mapInteraction(year,PlotVariable,click,button,figure):
    global currDptoData,dptoMap,region

    #Tell which input was triggered
    ctx = dash.callback_context

    #If dpto was changed  redraw for this dpto.
    if ctx.triggered[0]['prop_id'] == 'mainMap.clickData':
        if dptoMap:  #and if a dpto (not a munic) was selected

            #Define region to update title
            region = click['points'][0]['hovertext']
            Title = "{0} in {1}, year {2}".format(titleNamesDict[PlotVariable],region,year)  

            
            #Define new dpto 
            dpto = click['points'][0]['location']
            dptoMap = False # This is now a municipal map (not full Colombia)

            currDptoData = d.perCapMunic[d.perCapMunic['cod_dpto'] == dpto] 
            newData = currDptoData[currDptoData['year'] == year]
    
            fig = px.choropleth_mapbox(newData,
                       locations='id_birth',
                       color=PlotVariable,
                       geojson=d.Munic,
                       zoom=4,
                       mapbox_style="carto-positron", 
                       featureidkey = 'properties.MPIO_CCNCT',
                       color_continuous_scale="PuRd",
                       center={'lat':4.3,'lon':-73},
                       hover_name='mpio_name',
                       opacity=0.5)
            fig.update_layout(margin={'l':0,'r':0,'t':10,'b':5},
                                 paper_bgcolor="white",
                                 coloraxis_colorbar = dict(title='',thickness=20),
                                 font={'family':"Courier New, monospace",
                                       'size':18,
                                       'color':"#212529"})
            return (fig,Title)

        #If click on municip, do nothing
        else:
            raise PreventUpdate
        
    #If year or data to plot (dropDown) are changed, then modify data (not map)
    elif ctx.triggered[0]['prop_id'] == 'fig-slider.value' or ctx.triggered[0]['prop_id'] == 'whichData.value':
        if figure['data']: #(if only year was changed), change only data
            if dptoMap: #If current map is departamental (full Colombia)
                newData = d.perCapDptos[d.perCapDptos['year'] == year]
            else:  #If map is a municipal one:
                newData = currDptoData[currDptoData['year'] == year]   #Use already sliced data for this dpto.
                
            figure['data'][0]['z'] = newData[PlotVariable]


            Title = "{0} in {1}, year {2}".format(titleNamesDict[PlotVariable],region,year)  
            return (figure,Title)

    #If back button is pressed, then reset the map
    elif ctx.triggered[0]['prop_id'] == 'backButt.n_clicks':
        dptoMap = True   #We're back to full Colombia

        region = 'Colombia'
        Title = "{0} in {1}, year {2}".format(titleNamesDict[PlotVariable],region,year)  

        return (MainSection.mainMap,Title)

    else:
        Title = "{0} in {1}, year {2}".format(titleNamesDict[PlotVariable],region,year)  
        return (figure,Title)
        
    

###################################################### Run the server #########################################################


#Initiate the server where the app will work
if __name__ == "__main__":
    app.run_server(host='0.0.0.0',port='8050',debug=True)
