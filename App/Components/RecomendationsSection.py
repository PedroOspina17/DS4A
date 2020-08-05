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

def getHeader(headerTitle, headerSubtitle = None, headerTitleStyles = None,headerSubtitleStyles = None):
	return html.Div( ## Header template
		[
			html.Div(
				[
					html.Div(
						[
							html.Div(
								html.Img(src="assets/DS4A_colombia1.jpeg",className="ds4a-Logo")
							),
							html.Div(
								[
									
									html.H1(headerTitle,style=headerTitleStyles),
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
       
		################## MODEL - VARIABLES
        html.Div(
            [
                html.Div(
                    [
                        getHeader("PREDICTING A PREGNANCY OUTCOME",headerTitleStyles = {"margin-left": "-160px","margin-top": "-10px"}),
                        html.Div( # JUST TEXT ??:  ToDo
                            [
												html.Div(
													[
														html.Div(
															[
																html.P("The following models presented have the objective of knowing the forecast and probabilities that the result of the gestation process will be successful or not. ",style={"margin-top": "5%"}),
																html.P(["These models are the result of the combination of ",html.Span("6 features",className="important-yellow")," of the pregnancy process and the environment where it develops. "]),
																html.P("These characteristics are:"),
																html.Ul(
																	[
																		html.Li(" Number of pregnancies the mother has previously had."),
																		html.Li(" Multiplicity of pregnancy (type of pregnancy)."),
																		html.Li(" Type of access to social security."),
																		html.Li(" Department where the mother lives"),
																		html.Li(" Conditions of the mother's place of residence."),
																		html.Li(" Mother's education level.")
																	],className="coloredList",style={"margin-top": "5%"}
																)
															], className="seven columns"
														),
														html.Div(
															[
																html.Img(src="assets/ModelFeaturesPresentation.png",style={"width": "105%"}),
															], className="four columns"
														)
													],className="mt-lg-3"
												)
										# 	],
										# 	className=""
										# ),												
                                #     ],
								# 	className="row w-100"
								# ),		
                            ],
                            className="page-1n w-100 mt-lg-5",
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
                        getHeader("Logistic regression",headerTitleStyles = {"margin-left": "-34%","margin-top": "5%"}),
                        html.Div( # Color conclusions and graphs:  ToDo
                            [
                                html.Div(
                                    [	
										html.Div(
											[
												html.Div(
													[
														html.P("With the combination of each of the parameters mentioned above, we can find the probability that the result of the gestation process is successful or not. Which can help the mother with a low probability of a successful pregnancy, seek professional help to increase it."),
													],
													className="pink-item",style={"margin-top":"15%"}
												),
												html.Div(
													[
														html.P("The behavior of each of the characteristics mentioned above is observed in the figure on the right. Where the strongest shades of color for each characteristic show a greater probability that the pregnancy result will not be positive.Only the final combination of the probabilities of each characteristic will give us the total prediction of the model.")
													],
													className="blue-item",style={"margin-top":"15%"}
												),												
											], className="five columns"
										),
										html.Div(
											[												
												html.Img(src="assets/LogitCoeffs.png",style={"width": "100%","margin-top":"3%"})
											],
											className="seven columns"
										),
                                    ],
									className="row w-100 mt-5"
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
                        getHeader("Random forest",headerTitleStyles = {"margin-left": "-34%","margin-top": "5%"}),
                        html.Div( # Color conclusions and graphs:  ToDo
                            [
                                html.Div(
                                    [	
										
										html.Div(
											[
												html.Img(src="assets/FeaturesImportance.png",style={"width": "100%"})
											],
											className="eight columns"
										),
										html.Div(
											[
												html.Div(
													[														
														html.P("This predictive method gives us the importance of each of the characteristics when defining whether or not the pregnancy will be successful."),
													],
													className="pink-item",style={"margin-top":"9%"}
												),

												html.Div(
													[																												
														html.P("It can be seen that among this combination of characteristics the most important when defining the outcome of the pregnancy is multiplicity of the pregnancy, followed by the number of pregnancies that the mother has previously had"),
													],
													className="blue-item",style={"margin-top":"13%"}
												),
												
											], className="four columns"
										),
                                    ],
									className="row w-100",style={"margin-top":"6%"}
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
		################## Page 5 - SARIMA - 
        html.Div(
            [
                html.Div(
                    [
                        getHeader("Sarima", "Time series analysis."),
                        html.Div( # Color conclusions and graphs:  ToDo
                            [
                                html.Div(
                                    [	
										html.Div(
											[
												html.Div(
													[
														html.H6(
															"¡Predicting the future!",
															className="page-1h",
														),
														html.P("Based on data from the last 10 years, we were able to predict the number of births for the next 2 years."),
													],
													className="pink-item six columns",style={"margin-top": "5%"}
												),
												html.Div(
													[
														html.H6(
															"¿Why this could be useful?",
															className="page-1h",
														),
														html.P("This model assumes the world is the same every year, so events such as the COVID-19 pandemic are not expected. In this sense, these predictions serve as a baseline for assessing the effect of the pandemic on this variable."),
													],
													className="blue-item six columns",style={"margin-top": "5%"}
												),
												
												
												
											], className="w-100"
										),
										html.Div(
											[
												html.Img(src="assets/Sarima.png",style={"width": "100%","margin-top": "5%"})
											],
											className="w-100"
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
		################## Page 5 - CONCLUSIONS2- 
        html.Div(
            [
                html.Div(
                    [
                        getHeader("Conclusions2?", ""),
                        html.Div( # Color conclusions and graphs:  ToDo
                            [
                                html.Div(
                                    [	
										html.Div(
											[
												html.Div(
													[
														html.P("The problem at hand is heavily influenced by geography, and from the results of our models we infer that fetal deaths are systematically not being reported on peripheral and poor regions. There is also a great inequality between ethnicities which deserves a deeper analysis on its own."),
													],
													className="pink-item six columns",style={"margin-top": "5%"}
												),
												html.Div(
													[
														html.P("We showed that the pregnancy is heavily influenced by a number of variables, among which regional characteristics and social security are remarkable for their social implications."),
													],
													className="blue-item six columns",style={"margin-top": "5%"}
												),
												
												
											], className="w-100"
										),
										html.Div(
											[
												
												html.Div(
													[
														html.P("More time, domain knowledge and better data for infant deaths is needed in order to enrich this analysis, as well as including some other data like poverty levels, drinking-water access and a more detailed comparison to other countries."),
													],
													className="blue-item six columns",style={"margin-top": "5%"}
												),
												html.Div(
													[
														html.P("Future analyses shoud include a chapter about the impact of the COVID-19 pandemic on fetal and infant mortality rates in the country."),
													],
													className="pink-item six columns",style={"margin-top": "5%"}
												),
												
											], className="w-100"
										),
										html.Div(
											[
												html.Div(
													[														
														html.P("On the right hands, this work has the potential to help guide humanitarian initiatives and orient families on how to better take care of their offspring."),
													],
													className="pink-item six columns",style={"margin-top": "5%"}
												),
												
												
											], className="w-100"
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

		################## Page 5 - CONCLUSIONS2- 
        html.Div(
            [
                html.Div(
                    [
                        getHeader("¡THANKS!"),
                        html.Div( # Color conclusions and graphs:  ToDo
                            [
                                html.Div(
                                    [	
										html.Div(
											[
												html.Div(
													[
														html.H4("Lina M. Rincon",className="impotant-Blue",),
														html.P("Designer",className="impotant-yellow",),
														html.A("Behance",href="https://www.behance.net/linarincon",className="linkedin d-block"),
														html.A("LinkedIn",href="https://co.linkedin.com/in/lina-marcela-rincón-aguilera-29566886",className="linkedin d-block"),
													],
													className="pink-item six columns",style={"margin-top": "5%"}
												),
												html.Div(
													[
														html.H4("Natesh Pillai",className="impotant-Blue",),
														html.P("Program teacher",className="impotant-yellow",),
														html.A("LinkedIn",href="www.linkedin.com/in/pedro-nel-ospina-graciano",className="linkedin d-block"),
													],
													className="blue-item six columns",style={"margin-top": "5%"}
												),

											], className="w-100"
										),
										html.Div(
											[
												html.Div(
													[
														html.H4("Ana Lopez",className="impotant-Blue",),
														html.P("Teacher Assistant - Mentor",className="impotant-yellow",),
														html.A("LinkedIn",href="https://www.linkedin.com/in/amlopez81/",className="linkedin d-block"),
													],
													className="pink-item six columns",style={"margin-top": "5%"}
												),
												html.Div(
													[
														html.H4("Zachary H. Moore",className="impotant-Blue",),
														html.P("Teacher Assistant - Mentor",className="impotant-yellow",),
														html.A("LinkedIn",href="https://www.linkedin.com/in/zacharyhervieuxmoore/",className="linkedin d-block"),
													],
													className="blue-item six columns",style={"margin-top": "5%"}
												),
												
												
											], className="w-100"
										),
										html.Div(
											[
												
												html.Img(src="assets/ds4aCol.png",style={"width": "100%","margin-top": "5%"},className="six colums"),
												html.Img(src="assets/Mintic.png",style={"width": "100%","margin-top": "5%"},className="six colums")
												
											], className="w-100"
										),
                                    ],
									className="row w-100", style={"padding-left":"20%"}
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
