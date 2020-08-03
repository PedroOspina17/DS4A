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
								[
									html.Img(src="assets/DS4A_colombia1.jpeg",className="ds4a-Logo")
								]
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
							html.Span("20", className="page-1e",style={"font-size": "4.2rem"}),
							html.Span("20",style={"font-size": "4.2rem"}),
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
                                                html.Span("20", className="page-1e",style={"font-size": "4.2rem"}),
                                                html.Span("20",style={"font-size": "4.2rem"}),
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
                                        html.Img(src="assets/testLanding_v2.png",className="landingIMG",)
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
						################# Profiles section
                        html.Div(
                            [
								html.Div(
                                    [
										html.Div(
											[
												html.Div(
													[
														html.Img(src="assets/manCircle.png",className="profile-padge",),
													],
													className="px-5 four columns",
												),
												html.Div(
													[
														html.H4("Pedro N. Ospina",className="page-1h font-weight-bold"),
														html.Span("Ing. Sistemas",className="d-block font-weight-bold"),
														html.Span("300-242-9195",className="d-block"),
														html.Span("pedroospina17@gmail.com",className="d-block"),
													],
													className="blue-item columns eight",
												),
											],
											className="w-100 d-inline-block mt-5",
										),
										html.Div(
											[
												html.Div(
													[
														html.Img(src="assets/womanCircle.png",className="profile-padge",),
													],
													className="px-5 four columns",
												),
												html.Div(
													[
														html.H4("Melissa Aguilar",className="page-1h font-weight-bold"),
														html.Span("Ing. Física",className="d-block font-weight-bold"),
														html.Span("913-823-9541",className="d-block"),
														html.Span("melaguilarza@gmail.com",className="d-block"),
													],
													className="pink-item columns eight",
												),
											],
											className="w-100 d-inline-block mt-5",
										),
										html.Div(
											[
												html.Div(
													[
														html.Img(src="assets/manCircle.png",className="profile-padge",),
													],
													className="px-5 four columns",
												),
												html.Div(
													[
														html.H4("Andres C. Marulanda",className="page-1h font-weight-bold"),
														html.Span("Químico",className="d-block font-weight-bold"),
														html.Span("913-823-9541",className="d-block"),
														html.Span("acamilo.marulanda@udea.edu.co",className="d-block"),
													],
													className="blue-item columns eight",
												),
											],
											className="w-100 d-inline-block mt-5",
										),																			
									], className="six columns",
								),
								html.Div(
                                    [
										html.Div(
											[
												html.Div(
													[
														html.Img(src="assets/womanCircle.png",className="profile-padge",),
													],
													className="px-5 four columns",
												),
												html.Div(
													[
														html.H4("Angélica Rincon",className="page-1h font-weight-bold"),
														html.Span("Matemática",className="d-block font-weight-bold"),
														html.Span("913-823-9541",className="d-block"),
														html.Span("barincon23@gmail.com",className="d-block"),
													],
													className="pink-item columns eight",
												),
											],
											className="w-100 d-inline-block mt-5",
										),
										html.Div(
											[
												html.Div(
													[
														html.Img(src="assets/manCircle.png",className="profile-padge",),
													],
													className="px-5 four columns",
												),
												html.Div(
													[

														html.H4("Santiago Morales",className="page-1h font-weight-bold"),
														html.Span("Físico",className="d-block font-weight-bold"),
														html.Span("913-823-9541",className="d-block"),
														html.Span("santiagomoralessaldarriaga@gmail.com",className="d-block"),
													],
													className="blue-item columns eight",
												),
											],
											className="w-100 d-inline-block mt-5",
										),
										html.Div(
											[
												html.Div(
													[
														html.Img(src="assets/womanCircle.png",className="profile-padge",),
													],
													className="px-5 four columns",
												),
												html.Div(
													[
														html.H4("Jenny Lancheros",className="page-1h font-weight-bold"),
														html.Span("Admistradora - Estadistica",className="d-block font-weight-bold"),
														html.Span("913-823-9541",className="d-block"),
														html.Span("jlanch14@hotmail.com",className="d-block"),
													],
													className="pink-item columns eight",
												),
											],
											className="w-100 d-inline-block mt-5",
										),
										
										
									], className="six columns",
								)
                            ],
                            className="page-1n w-100",
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
                        getHeader("CONTEXT","Definitions"),
                        html.Div( # Color conclusions and graphs:  ToDo
                            [
                                html.Div(
                                    [	
										html.Div(
											[
												html.Div(
													[
														html.H6("Stillbirth:",className="subtitle-item"),
														html.P(["Stillbirth definition"]
																, className=""
															),
													],
													className="pink-item",style={"margin-top":"5%"}
												),
												html.Div(
													[
														html.H6("Neonate:",className="subtitle-item"),
														html.P(["Neonate definition"]
																, className=""
															),
													],
													className="blue-item",style={"margin-top":"5%"}
												),
												
												
											], className="six columns"
										),
										html.Div(
											[
												html.Div(
													[
														html.H6("Infant:",className="subtitle-item"),
														html.P(["Stillbirth definition"]
																, className=""
															),
													],
													className="pink-item",style={"margin-top":"5%"}
												),
												html.Div(
													[
														html.H6("perinatal:",className="subtitle-item"),
														html.P(["Neonate definition"]
																, className=""
															),
													],
													className="blue-item",style={"margin-top":"5%"}
												),																						
											],
											className="six columns"
										),
										html.Div(
											[
												html.Img(src="assets/BabyTimes.png",style={"width": "90%","margin-left":"10%","margin-top":"2%"})												
											],
											className="ten columns"
										)
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
		#################################################### Page 2 --- OVERVIEW - GLOBAL
        html.Div(
            [
                html.Div(
                    [
                        getHeader("OVERVIEW","Global comparison"),
                        html.Div( # Color conclusions and graphs:  ToDo
                            [
                                html.Div(
                                    [	
										html.Div(
											[
												html.Div(
													[
														html.P(["As of 2011, The World Health Organization (WHO for its acronym) estimates that about ",html.Span("4 million",className="important-yellow"), " neonates die every year, and nearly 41% of all under-five child deaths are among newborn infants and specially babies in their first 28 days of life (neonates) [1]."]
																, className="page-2b"
															),
													],
													className="pink-item",style={"margin-top":"10%"}
												),
												html.Div(
													[
														html.P(" ."
																, className="page-2c"
															),
													],
													className="blue-item",style={"margin-top":"10%"}
												),

												html.Div(
													[
														html.P([html.Span("BOY DIE MORE THAN GIRLS ?",className="important-blue"),".... Some useful dates... Numbers: ",html.Span("28.9",className="important-pink")," for every 1000 births",""]
																, className="page-2c"
															),
													],
													className="pink-item",style={"margin-top":"10%"}
												),
																							
												
											], className="six columns"
										),
										html.Div(
											[
												# dcc.Graph(figure=HorizontalBars.GeneralFig, id='OverviewGlobalBars',style={"height":"500px"}),
												html.Img(src="assets/InfantMortalityNumbers.png",style={"width": "70%"}),
												html.Img(src="assets/AmericasNumbers.png",style={"width": "100%"})
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
														html.P(".", className="page-2c"),
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
														html.P(),
													],
													className="pink-item"
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
												html.P(lorem.paragraph()),
												html.P("adadawd"),
												html.P(lorem.paragraph()),
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
												html.Img(src="assets/fig1_col_top.png",style={"width": "48%"})
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
													className="blue-item",
													style = {"margin-top": "26%"}
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
												
												
											], className="six columns"
										),
										html.Div(
											[
												html.Img(src="assets/LogitCoeffs.png",style={"width": "100%"})
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
												html.Img(src="assets/Maps.png",style={"width": "94%"})
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
														html.P(lorem.paragraph()),
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
