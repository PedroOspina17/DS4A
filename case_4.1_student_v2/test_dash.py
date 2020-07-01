import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import json

#Create the app
app = dash.Dash(__name__)


df = pd.read_csv('App/Data/superstore.csv', parse_dates=['Order Date', 'Ship Date'])
with open('App/Data/us.json') as geo:
    geojson = json.loads(geo.read())

with open('App/Data/states.json') as f:
    states_dict = json.loads(f.read())


df['State_abbr'] = df['State'].map(states_dict)


dff=df.groupby('State_abbr').sum().reset_index()

Map_Fig = px.choropleth_mapbox(dff,                         #Data
            locations='State_abbr',                   #Column containing the identifiers used in the GeoJSON file 
            color='Sales',                            #Column giving the color intensity of the region
            geojson=geojson,                          #The GeoJSON file
            zoom=3,                                   #Zoom
            mapbox_style="carto-positron",            #Mapbox style, for different maps you need a Mapbox account and a token
            center={"lat": 37.0902, "lon": -95.7129}, #Center
            color_continuous_scale="Viridis",         #Color Scheme
            opacity=0.5,                              #Opacity of the map
            )


Scatter_Fig = (px.scatter(df, x="Sales", y="Profit", color="Category", 
                          hover_data=['State','Sub-Category','Order ID','Product Name']))  

#Create Layout
app.layout = html.Div([
    html.H2("US Sales Map", id='title'), #Creates the title of the app
  
    dcc.Graph(figure=Map_Fig, id='main-figure'),
    dcc.Slider(min=0,max=1,marks={0:'US Map', 1:'Scatter Plot'},value=0,id='fig-slider',)
])

@app.callback(
    Output('main-figure','figure'),
    [Input('fig-slider','value')])
def slider_interaction(slider_val):
    if slider_val==0:
        fig=Map_Fig
    else:
        fig=Scatter_Fig

    return fig 

#Initiate the server where the app will work
if __name__ == "__main__":
    app.run_server(debug=True)