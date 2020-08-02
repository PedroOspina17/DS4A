
import plotly.express as px
from Components import LoadData as d


df_slice = d.perCapDptos[d.perCapDptos['year'] == 2017].groupby(['cod_dpto','DPNOM']).mean().reset_index()

fig = px.choropleth_mapbox(df_slice,
           locations='cod_dpto',
           color='alive_percapita',
           geojson=d.Dpto,
           zoom=4,
           mapbox_style="carto-positron",
           featureidkey = 'properties.DPTO_CCDGO',
           color_continuous_scale="PuRd",
           center={'lat':4.3,'lon':-73},
           hover_name='DPNOM',
           opacity=0.7)

fig.update_layout(margin={'l':0,'r':0,'t':0,'b':0},
                    coloraxis_colorbar = dict(title='',thickness=20),
                     paper_bgcolor="white",
                     font={'family':"Courier New, monospace",
                           'size':18,
                           'color':"#212529"})


