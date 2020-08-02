# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import dash_table
import pandas as pd
import lorem
import pathlib
from Components import MapCharts,SidebarSection,HorizontalBars

# Path
# BASE_PATH = pathlib.Path(__file__).parent.resolve()

# DATA_PATH = BASE_PATH.joinpath("Data").resolve()



# Colours
color_1 = "#003399"
color_2 = "#00ffff"
color_3 = "#002277"
color_b = "#F8F8FF"

def getHeader(headerTitle, headerSubtitle = None, headerSubtitleStyles = None):
	return html.Div( ## Header 
		[
			html.Div(
				[
					html.Div(
						[
							html.Div(
								html.Img(src="assets/ds4a2.png",className="ds4a-Logo")
							),
							html.Div(
								[
									
									html.H1(headerTitle),
									html.H3(headerSubtitle,style=headerSubtitleStyles) if headerSubtitle else None,
								],
								className="PageTitle",
							),
						],
						className="page-1c",
					)
				],
				className="page-1d",
			),
			html.Div(
				[
					html.H1(
						[
							html.Span("20", className="page-1e"),
							html.Span("20"),
							html.H5("BORN AI"),
						]
					),
				],
				className="page-1f",
			),
		],
		className="page-1g",
	)


component = html.Div(
    children=[
        html.Div(
            [
                html.Div( # Content page
                    [
                        html.Div( # Header
                            [
                                html.Div( #Blue bar
                                    [
                                        html.Div(
                                            [
                                                html.Div(
                                                    html.Img(
                                                        src="assets/dash-logo-new.png",
                                                        className="page-1a",
                                                    )
                                                ),
                                                html.Div(
                                                    [
                                                        
                                                        html.H1("BORN AI", className="greenTitle"),
                                                        html.H4("Analyzing borns in colombia."),
                                                    ],
                                                    className="page-1b",
                                                ),
                                            ],
                                            className="page-1c",
                                        )
                                    ],
                                    className="page-1d",
                                ),
                                html.Div( # Green bar
                                    [
                                        html.H1(
                                            [
                                                html.Span("20", className="page-1e"),
                                                html.Span("20"),
                                                html.H5("Data science for All"),
                                            ]
                                        ),
                                    ],
                                    className="page-1f",
                                ),
                            ],
                            className="page-1g",
                        ),
						################# Landing page
                        html.Div(
                            [
                                html.Div(
                                    [                                        
                                        html.Img(
                                                        src="assets/testLanding1.jpg",
                                                        className="landingIMG",
                                                    )
                                    ],
                                    className="",
                                ),
                            ],
                            className="landing",
                        ),						
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ),
		html.Div(
            [
                html.Div(
                    [
                        getHeader("TEAM 4"),
						################# Names section
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H6("Pedro N. Ospina", className="page-1h"),
                                        html.P("300-242-9195"),
                                        html.P("pedroospina17@gmail.com"),
                                    ],
                                    className="page-1i",
                                ),
                                html.Div(
                                    [
                                        html.H6("Andres C. Marulanda", className="page-1h"),
                                        html.P("497-234-2837r"),
                                        html.P("isw@vxogiqyds.umf"),
                                    ],
                                    className="page-1i",
                                ),
                                html.Div(
                                    [
                                        html.H6(
                                            "Melissa Aguilar", className="page-1h"
                                        ),
                                        html.P("913-823-9541"),
                                        html.P("rgd@hp.xji"),
                                    ],
                                    className="page-1i",
                                ),
                                html.Div(
                                    [
                                        html.H6("Angélica Rincon", className="page-1h"),
                                        html.P("248-865-2687"),
                                        html.P("mc@a.kur"),
                                    ],
                                    className="page-1i",
                                ),
                                html.Div(
                                    [
                                        html.H6("Jenny Lancheros", className="page-1h"),
                                        html.P("284-671-3721"),
                                        html.P("j@jdvwnqucm.etv"),
                                    ],
                                    className="page-1i",
                                ),
                                html.Div(
                                    [
                                        html.H6("Santiago Morales", className="page-1h"),
                                        html.P("284-671-3721"),
                                        html.P("j@jdvwnqucm.etv"),
                                    ],
                                    className="page-1i",
                                ),
                            ],
                            className="page-1j",
                        ),
						################# Items section
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H6(
                                            "Viverra, imperdiet, praesent pellentesque",
                                            className="page-1h",
                                        ),
                                        html.P(lorem.paragraph() * 2),
                                    ],
                                    className="page-1k",
                                ),
                                html.Div(
                                    [
                                        html.H6(
                                            "Facilisis mauris parturient, eget vitae",
                                            className="page-1h",
                                        ),
                                        html.P(lorem.paragraph() * 2),
                                    ],
                                    className="page-1l",
                                ),
                                html.Div(
                                    [
                                        html.H6(
                                            "A suspendisse mauris aliquam tincidunt hac",
                                            className="page-1h",
                                        ),
                                        html.P(lorem.paragraph() * 2),
                                    ],
                                    className="page-1m",
                                ),
                                html.Div(
                                    [
                                        html.H6(
                                            "A elementum lorem dolor aliquam nisi diam",
                                            className="page-1h",
                                        ),
                                        html.P(lorem.paragraph()),
                                    ],
                                    className="page-1l",
                                ),
                            ],
                            className="page-1n",
                        ),
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ),
        #################################################### Page 2 --- OVERVIEW - GLOBAL
        html.Div(
            [
                html.Div(
                    [
                        getHeader("OVERVIEW","Global comparison"),
                        html.Div( # Paragraph: ToDo
                            [
                                html.P("As of 2011, The World Health Organization (WHO for its acronym) estimates that about 4 million neonates die every year, and nearly 41% of all under-five child deaths are among newborn infants and specially babies in their first 28 days of life (neonates) [1]. Accordingly, perinatal (period between 20 weeks before, and 4 weeks after birth) and neonatal mortality is now a part of the 2030 agenda for Sustainable Development of the United Nations and is also one of the topics of interest to the Colombian Ministry of Health [2].", className="page-2b"),
                                html.P("This work is aimed to be a comprehensive analysis of different databases related to perinatal and neonatal death, as well as demographic, economic, social and geographic data for Colombia, that can help us understand which features may influence and contribute to said death rate in different locations in the country by looking for possible correlations that may constitute the first step to the search for solutions to this global health issue.", className="page-2c"),
                                html.P("Characterization of the social, economic, demographic and geological variables that can be correlated and may have an impact on the newborn and fetal death rates is of capital importance for the localization of the most affected regions, as well as for the identification of causal relationships between said factors and, upon inclusion of larger databases, identification and prediction of new significant factors, as well as the prediction of future outcomes. Such an analysis may eventually lead to the implementation of more specialized and well-designed social programs, as well as health campaigns, among other humanitarian initiatives.", className="page-2c"),
                            ],
                            className="page-3",
                        ),
                        html.Div( # Color conclusions and graphs:  ToDo
                            [
                                html.Div(
                                    [	
										html.Div(
											[
												html.Div(
													[
														html.H6(
															"Facilisis mauris parturient, eget vitae",
															className="page-1h",
														),
														html.P(lorem.paragraph()),
													],
													className="pink-item"
												),
												html.Div(
													[
														html.H6(
															"Facilisis mauris parturient, eget vitae",
															className="page-1h",
														),
														html.P(lorem.paragraph()),
													],
													className="blue-item"
												),
												html.Div(
													[
														html.H6(
															"Facilisis mauris parturient, eget vitae",
															className="page-1h",
														),
														html.P(lorem.paragraph()),
													],
													className="pink-item"
												),
												html.Div(
													[
														html.H6(
															"Facilisis mauris parturient, eget vitae",
															className="page-1h",
														),
														html.P(lorem.paragraph()*5),
													],
													className="blue-item"
												),
												
											], className="six columns"
										),
										html.Div(
											[
												dcc.Graph(figure=HorizontalBars.GeneralFig, id='OverviewGlobalBars',style={"height":"500px"}),
											],
											className="six columns"
										),
                                    ],
									className="row w-100"
								),								
                            ],
                            className="page-1n w-100",
                        ),
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ),
        ################## Page 3 - OEVRVIEW LOCAL
        html.Div(
            [
                html.Div(
                    [
                        getHeader("OVERVIEW", "Taking a look at Colombia's situation.",{"margin-left": "-130px"}),
                        html.Div( # Color conclusions and graphs:  ToDo
                            [
                                html.Div(
                                    [	
										html.Div(
											[
												html.Div(
													[
														html.H6(
															"Facilisis mauris parturient, eget vitae",
															className="page-1h",
														),
														html.P(lorem.paragraph()),
													],
													className="pink-item"
												),
												html.Div(
													[
														html.H6(
															"Facilisis mauris parturient, eget vitae",
															className="page-1h",
														),
														html.P(lorem.paragraph()),
													],
													className="blue-item"
												),
												html.Div(
													[
														html.H6(
															"Facilisis mauris parturient, eget vitae",
															className="page-1h",
														),
														html.P(lorem.paragraph()),
													],
													className="pink-item"
												),
												html.Div(
													[
														html.H6(
															"Facilisis mauris parturient, eget vitae",
															className="page-1h",
														),
														html.P(lorem.paragraph()*5),
													],
													className="blue-item"
												),
												
											], className="six columns"
										),
										html.Div(
											[
												dcc.Graph(figure=HorizontalBars.GeneralFig, id='OverviewGlobalBars2',style={"height":"500px"}),
											],
											className="six columns"
										),
                                    ],
									className="row w-100"
								),								
                            ],
                            className="page-1n w-100 mt-3",
                        ),
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ),
		################## Page 4 - IMPACT
        html.Div(
            [
                html.Div(
                    [
                        getHeader("IMPACT"),
                        html.Div( # JUST TEXT ??:  ToDo
                            [
                                html.Div(
                                    [											
										html.Div(
											[
												html.H6(
													"Facilisis mauris parturient, eget vitae",
													className="page-1h",
												),
												html.P(lorem.paragraph() * 3),
												html.P(lorem.paragraph()  * 2),
												html.P(lorem.paragraph()),
												html.P(lorem.paragraph()*5),
											],
											className=""
										),												
                                    ],
									className="row w-100"
								),								
                            ],
                            className="page-1n w-100 mt-3",
                        ),
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ),
        ################## Page 5 - EDA - Basic variables
        html.Div(
            [
                html.Div(
                    [
                        getHeader("Analysis", "Demographic variables I."),
                        html.Div( # Color conclusions and graphs:  ToDo
                            [
                                html.Div(
                                    [	
										html.Div(
											[
												html.Div(
													[
														html.H6(
															"Facilisis mauris parturient, eget vitae",
															className="page-1h",
														),
														html.P(lorem.paragraph()),
													],
													className="pink-item"
												),
												html.Div(
													[
														html.H6(
															"Facilisis mauris parturient, eget vitae",
															className="page-1h",
														),
														html.P(lorem.paragraph()),
													],
													className="blue-item"
												),
												html.Div(
													[
														html.H6(
															"Facilisis mauris parturient, eget vitae",
															className="page-1h",
														),
														html.P(lorem.paragraph()),
													],
													className="pink-item"
												),
												html.Div(
													[
														html.H6(
															"Facilisis mauris parturient, eget vitae",
															className="page-1h",
														),
														html.P(lorem.paragraph()*5),
													],
													className="blue-item"
												),
												
											], className="six columns"
										),
										html.Div(
											[
												html.Img(src="assets/fig1_col_bott.png",style={"width": "70%"})
											],
											className="six columns"
										),
                                    ],
									className="row w-100"
								),								
                            ],
                            className="page-1n w-100 mt-3",
                        ),
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ),
		################## Page 5 - EDA - Basic variables
        html.Div(
            [
                html.Div(
                    [
                        getHeader("Analysis", "Demographic variables I."),
                        html.Div( # Color conclusions and graphs:  ToDo
                            [
                                html.Div(
                                    [	
										
										html.Div(
											[
												html.Img(src="assets/fig1_col_top.png",style={"width": "70%"})
											],
											className="six columns"
										),
										html.Div(
											[
												html.Div(
													[
														html.H6(
															"Facilisis mauris parturient, eget vitae",
															className="page-1h",
														),
														html.P(lorem.paragraph()),
													],
													className="pink-item"
												),
												html.Div(
													[
														html.H6(
															"Facilisis mauris parturient, eget vitae",
															className="page-1h",
														),
														html.P(lorem.paragraph()),
													],
													className="blue-item"
												),
												html.Div(
													[
														html.H6(
															"Facilisis mauris parturient, eget vitae",
															className="page-1h",
														),
														html.P(lorem.paragraph()),
													],
													className="pink-item"
												),
												html.Div(
													[
														html.H6(
															"Facilisis mauris parturient, eget vitae",
															className="page-1h",
														),
														html.P(lorem.paragraph()*5),
													],
													className="blue-item"
												),
												
											], className="six columns"
										),
                                    ],
									className="row w-100"
								),								
                            ],
                            className="page-1n w-100 mt-3",
                        ),
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ),
		################## Page 5 - EDA - Basic variables
        html.Div(
            [
                html.Div(
                    [
                        getHeader("Analysis", "Demographic variables I."),
                        html.Div( # Color conclusions and graphs:  ToDo
                            [
                                html.Div(
                                    [	
										html.Div(
											[
												html.Div(
													[
														html.H6(
															"Facilisis mauris parturient, eget vitae",
															className="page-1h",
														),
														html.P(lorem.paragraph()),
													],
													className="pink-item"
												),
												html.Div(
													[
														html.H6(
															"Facilisis mauris parturient, eget vitae",
															className="page-1h",
														),
														html.P(lorem.paragraph()),
													],
													className="blue-item"
												),
												html.Div(
													[
														html.H6(
															"Facilisis mauris parturient, eget vitae",
															className="page-1h",
														),
														html.P(lorem.paragraph()),
													],
													className="pink-item"
												),
												html.Div(
													[
														html.H6(
															"Facilisis mauris parturient, eget vitae",
															className="page-1h",
														),
														html.P(lorem.paragraph()*5),
													],
													className="blue-item"
												),
												
											], className="six columns"
										),
										html.Div(
											[
												html.Img(src="assets/LogitCoeffs.png",style={"width": "70%"})
											],
											className="six columns"
										),
                                    ],
									className="row w-100"
								),								
                            ],
                            className="page-1n w-100 mt-3",
                        ),
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ),
		################## Page 5 - EDA - Basic variables
        html.Div(
            [
                html.Div(
                    [
                        getHeader("Analysis", "Demographic variables I."),
                        html.Div( # Color conclusions and graphs:  ToDo
                            [
                                html.Div(
                                    [	
										html.Div(
											[
												html.Img(src="assets/Maps.png",style={"width": "70%"})
											],
											className="six columns"
										),
										html.Div(
											[
												html.Div(
													[
														html.H6(
															"Facilisis mauris parturient, eget vitae",
															className="page-1h",
														),
														html.P(lorem.paragraph()),
													],
													className="pink-item"
												),
												html.Div(
													[
														html.H6(
															"Facilisis mauris parturient, eget vitae",
															className="page-1h",
														),
														html.P(lorem.paragraph()),
													],
													className="blue-item"
												),
												html.Div(
													[
														html.H6(
															"Facilisis mauris parturient, eget vitae",
															className="page-1h",
														),
														html.P(lorem.paragraph()),
													],
													className="pink-item"
												),
												html.Div(
													[
														html.H6(
															"Facilisis mauris parturient, eget vitae",
															className="page-1h",
														),
														html.P(lorem.paragraph()*5),
													],
													className="blue-item"
												),
												
											], className="six columns"
										),
                                    ],
									className="row w-100"
								),								
                            ],
                            className="page-1n w-100 mt-3",
                        ),
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ),
		################## Page 5 - EDA - Basic variables
        html.Div(
            [
                html.Div(
                    [
                        getHeader("Analysis", "Demographic variables I."),
                        html.Div( # Color conclusions and graphs:  ToDo
                            [
                                html.Div(
                                    [	
										html.Div(
											[
												html.Div(
													[
														html.H6(
															"Facilisis mauris parturient, eget vitae",
															className="page-1h",
														),
														html.P(lorem.paragraph()),
													],
													className="pink-item"
												),
												html.Div(
													[
														html.H6(
															"Facilisis mauris parturient, eget vitae",
															className="page-1h",
														),
														html.P(lorem.paragraph()),
													],
													className="blue-item"
												),
												html.Div(
													[
														html.H6(
															"Facilisis mauris parturient, eget vitae",
															className="page-1h",
														),
														html.P(lorem.paragraph()),
													],
													className="pink-item"
												),
												html.Div(
													[
														html.H6(
															"Facilisis mauris parturient, eget vitae",
															className="page-1h",
														),
														html.P(lorem.paragraph()*5),
													],
													className="blue-item"
												),
												
											], className="six columns"
										),
										html.Div(
											[
												html.Img(src="assets/fig1_col_bott.png",style={"width": "70%"})
											],
											className="six columns"
										),
                                    ],
									className="row w-100"
								),								
                            ],
                            className="page-1n w-100 mt-3",
                        ),
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ),
    ]
)