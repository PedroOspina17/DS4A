import plotly.express as px
from Components import LoadData as d
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np


df_slice = d.perCapDptos[d.perCapDptos['year'] == 2017].sort_values(by="fetalRatio",ascending=True)



fig = make_subplots(rows=1, cols=1,vertical_spacing=0.1)

fig.append_trace(go.Bar(
    x= df_slice["fetalRatio"],y =df_slice["DPNOM"],#width=5,
    marker=dict(
        color='#c8dfed',
        line=dict(
            color='#156bcf',
            width=1)
    ),
    name='Household savings, percentage of household disposable income',
    orientation='h',
#     width = 5
), 1, 1)


fig.update_layout(
#     title='Household savings & net worth for eight OECD countries',
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=True,
        domain=[0, 0.85],
    ),
    
    xaxis=dict(
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
        domain=[0, 0.42],
    ),
    margin=dict(l=0, r=0, t=0, b=0),
    paper_bgcolor='white',
    plot_bgcolor='white',
)

annotations = []

y_s = np.round(df_slice["fetalRatio"]*100, decimals=2)
# y_nw = np.rint(y_net_worth)

# Adding labels
for yd, xd, pos in zip(y_s, df_slice["DPNOM"],df_slice["fetalRatio"]):
    
    # labeling the bar net worth
    annotations.append(dict(xref='x', yref='y',
                            y=xd, x=pos + 0.05,
                            text=str(yd) + '%',
                            font=dict(family='Arial', size=12,
                                      color='#7289ac'),
                            showarrow=False))

fig.update_layout(annotations=annotations)