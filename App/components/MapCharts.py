
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction



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
