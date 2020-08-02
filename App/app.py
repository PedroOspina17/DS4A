

import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State, ClientsideFunction
import plotly.express as px
import plotly.graph_objects as go 
import pandas as pd
import json
import os
from Components import RecomendationsSection,AnalyticsSection,SidebarSection,OverviewSection
from Components import LoadData as Data
from Components import HorizontalBars

#Create the app
app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP]) #USING BOOTSTRAP'S CSS LIBRARY

####################################################### Layout ###################################################
# footer = html.Div("Team 4 -- Borns AI", className ="mx-auto font-weight-bold fot-italic mt-5 text-muted")
    

tab1_content = dbc.Card(
dbc.CardBody(
    [
        OverviewSection.component
        
    ]
),
className="mt-3",
)

tab2_content = dbc.Card(
    dbc.CardBody(
        [
           AnalyticsSection.component
        ]
    ),
    style={"margin-top":"3%"}
)

tab3_content = dbc.Card(
    dbc.CardBody(
        [
           RecomendationsSection.component
        ]
    ),
    className="mt-3",
)


tabs = dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="Overview"),
        dbc.Tab(tab2_content, label="Analytics"),
        dbc.Tab(tab3_content, label="Recomendations")
    ],
    className="header",
)

title = dbc.Container([ html.H1("Borns AI", className="ml-3 mt-3"),html.Hr()])
app.layout =  html.Div([tabs])

###################################################### Callbacks ###################################################

update_barfig = HorizontalBars.update_barfig

## Update main map, map title and right barplot
titleNamesDict = {value:label for value,label in SidebarSection.opts.items()}

currDptoData = 0     #Variable to hold data for only one dpto so query is faster when changing years. 
dptoMap = True       #Tell if we're currently at a full Colombia map
region = 'Colombia'  #Variable to hold region name (be it Colombia or a specific dpto)

@app.callback(
    [Output('mainMap','figure'),Output('mapFigTitle','children'),Output('barPlot','figure')],
    [Input('fig-slider','value'),Input('whichData','value'),Input('mainMap','clickData'),Input('backButt','n_clicks')],
    [State('mainMap','figure'),State('barPlot','figure')])
def mapInteraction(year,PlotVariable,click,button,mapPlot,barPlot):
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

            currDptoData = Data.perCapMunic[Data.perCapMunic['cod_dpto'] == dpto] 
            newData = currDptoData[currDptoData['year'] == year]
    
            mapfig = px.choropleth_mapbox(newData,
                       locations='id_resid',
                       color=PlotVariable,
                       geojson=Data.Munic,
                       zoom=4,
                       mapbox_style="carto-positron", 
                       featureidkey = 'properties.MPIO_CCNCT',
                       color_continuous_scale="PuRd",
                       center={'lat':4.3,'lon':-73},
                       hover_name='mpio_name',
                       opacity=0.5)
            mapfig.update_layout(margin={'l':0,'r':0,'t':10,'b':5},
                                 paper_bgcolor="white",
                                 coloraxis_colorbar = dict(title='',thickness=20),
                                 font={'family':"Courier New, monospace",
                                       'size':18,
                                       'color':"#212529"})


            barfig = update_barfig(newData,PlotVariable)

            return (mapfig,Title,barfig)

        #If click on municip, do nothing
        else:
            raise PreventUpdate
        
    #If year or data to plot (dropDown) are changed, then modify data (not map)
    elif ctx.triggered[0]['prop_id'] == 'fig-slider.value' or ctx.triggered[0]['prop_id'] == 'whichData.value':
        if mapPlot['data']: #(if only year was changed), change only data
            if dptoMap: #If current map is departamental (full Colombia)
                newData = Data.perCapDptos[Data.perCapDptos['year'] == year]
                barfig = update_barfig(newData,PlotVariable,y='DPNOM')

            else:  #If map is a municipal one:
                newData = currDptoData[currDptoData['year'] == year]   #Use already sliced data for this dpto.
                barfig = update_barfig(newData,PlotVariable)
                
            mapPlot['data'][0]['z'] = newData[PlotVariable]



            Title = "{0} in {1}, year {2}".format(titleNamesDict[PlotVariable],region,year)  
            return (mapPlot,Title,barfig)

    #If back button is pressed, then reset the map
    elif ctx.triggered[0]['prop_id'] == 'backButt.n_clicks':
        dptoMap = True   #We're back to full Colombia

        region = 'Colombia'
        Title = "{0} in {1}, year {2}".format(titleNamesDict[PlotVariable],region,year)  

        return (AnalyticsSection.mainMap,Title,AnalyticsSection.sideBars)

    else:
        Title = "{0} in {1}, year {2}".format(titleNamesDict[PlotVariable],region,year)  
        return (mapPlot,Title,barPlot)
        
    
###################################################### Run de app server ###################################################    
    
if __name__ == "__main__":
    app.run_server(host='0.0.0.0',port='8050',debug=True)
