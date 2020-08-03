import plotly.express as px
from Components import LoadData as d
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np


df_slice = d.perCapDptos[d.perCapDptos['year'] == 2017].sort_values(by="fetalRatio",ascending=True)



fig = go.Figure(go.Bar(
    x= df_slice["fetalRatio"],y =df_slice["DPNOM"],
    orientation = 'h',
    marker=dict(
        color='#03AEA4',
        line=dict(
            color='#044D6E',
            width=1)
    ),
))


fig.update_layout(
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=True,
        domain=[0, 0.9],
    ),
    
    xaxis=dict(
        zeroline=False,
        showline=False,
        showticklabels=False,
        showgrid=True,
        domain=[0, 0.95],
    ),
    margin=dict(l=0, r=0, t=0, b=0),
    paper_bgcolor='white',
    plot_bgcolor='white',
)

annotations = []

y_s = np.round(df_slice["fetalRatio"]*100, decimals=2)

# Adding labels
for yd, xd, pos in zip(y_s, df_slice["DPNOM"],df_slice["fetalRatio"]):
    
    # labeling the bar net worth
    annotations.append(dict(xref='x', yref='y',
                            y=xd, x=pos + 0.03,
                            text=str(yd) + '%',
                            font=dict(family='Arial', size=12,
                                      color='#044D6E'),
                            showarrow=False))

fig.update_layout(annotations=annotations)

######################### General - Overview


toplotGeneral = d.perCapDptos.groupby("DPNOM")["fetalRatio"].mean().reset_index().sort_values(by="fetalRatio",ascending=True)

GeneralFig = make_subplots(rows=1, cols=1,vertical_spacing=0.1)

GeneralFig.append_trace(go.Bar(
    x= toplotGeneral["fetalRatio"]*1000,y =toplotGeneral["DPNOM"],#width=5,
    marker=dict(
        color='#03AEA4',
        line=dict(
            color='#044D6E',
            width=1)
    ),
    name='Household savings, percentage of household disposable income',
    orientation='h',
#     width = 5
), 1, 1)




GeneralFig.update_layout(
#     title='Household savings & net worth for eight OECD countries',
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=True,        
    ),
    
    xaxis=dict(
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,        
    ),
    margin=dict(l=0, r=0, t=0, b=0),
    paper_bgcolor='white',
    plot_bgcolor='white',
)

annotations = []


GeneralFig.update_layout(
    shapes=[
        dict(type="line", xref="x", yref="y",
            x0=12.2, y0=toplotGeneral["DPNOM"].iloc[0], x1=12.2, y1=toplotGeneral["DPNOM"].iloc[-1], line_width=3, line_color="#F8A528"),
            ])

y_s = np.round(toplotGeneral["fetalRatio"]*1000, decimals=2)
# y_nw = np.rint(y_net_worth)

# Adding labels
for xd,pos in zip( toplotGeneral["DPNOM"],y_s):    
    # labeling the bar net worth
    annotations.append(dict(xref='x', yref='y',
                            y=xd, x=pos + 10,
                            text=str(pos),
                            font=dict(family='Arial', size=12,
                                      color='#044D6E'),
                            showarrow=False))

GeneralFig.update_layout(annotations=annotations)

#Update function
def update_barfig(newData,PlotVariable,y='mpio_name'):
    
    barsData = (newData.sort_values(by=PlotVariable,ascending=False).iloc[:20]
                .sort_values(by=PlotVariable))
    
    barfig = go.Figure(go.Bar(
        x = barsData[PlotVariable],
        y = barsData[y],
        orientation = 'h',
        marker=dict(
            color='#03AEA4',
            line=dict(
				color='#044D6E',
				width=1)
        ),
    ))
    
    barfig.update_layout(
        yaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=True,
            domain=[0, 0.9],
        ),
        
        xaxis=dict(
            zeroline=False,
            showline=False,
            showticklabels=False,
            showgrid=True,
            domain=[0.3, 0.95],
        ),
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor='white',
        plot_bgcolor='white',
    )
    
    annotations = []
    
    y_s = np.round(barsData[PlotVariable], decimals=2)
    
    # Adding labels
    for yd, xd, pos in zip(y_s, barsData[y],barsData[PlotVariable]):
        
        # labeling the bar net worth
        annotations.append(dict(xref='x', yref='y',
                                y=xd, x=pos + 0.4 ,
                                text=str(yd) ,
                                font=dict(family='Arial', size=12,
                                          color='#044D6E'),
                                showarrow=False))
    
    barfig.update_layout(annotations=annotations)
    return barfig

