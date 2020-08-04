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
                                        html.Img(src="assets/testLanding_v2.jpeg",className="landingIMG",)
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
														html.H6("Fetal mortality / Stillbirth:",className="subtitle-item"),
														html.P(["A stillbirth is the death or loss of a baby before or during delivery. It encompasses any death of a fetus after 20 weeks of gestation or 500 gm."]
																, className=""
															),
													],
													className="pink-item",style={"margin-top":"5%"}
												),
												html.Div(
													[
														html.H6("Neonate mortality:",className="subtitle-item"),
														html.P(["Neonatal mortality refers to death of a live-born baby within the first 28 days of life. Early neonatal mortality refers to the death of a live-born baby within the first seven days of life, while late neonatal mortality refers to death after 7 days until before 28 days."]
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
														html.H6("Perinatal mortality:",className="subtitle-item"),
														html.P(["Defined as the number of fetal deaths past 22 (or 28) completed weeks of pregnancy plus the number of deaths among live-born children up to 7 completed days of life."]
																, className=""
															),
													],
													className="blue-item",style={"margin-top":"5%","height":"88%","padding-top":"12%"}
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
													className="pink-item",style={"margin-top":"10%"}
												),	
												html.Div(
													[
														html.H6(
															"Facilisis mauris parturient, eget vitae",
															className="page-1h",
														),
														html.P(lorem.paragraph()),
													],
													className="blue-item",style={"margin-top":"10%"}
												),
												html.Div(
													[
														html.H6(
															"Facilisis mauris parturient, eget vitae",
															className="page-1h",
														),
														html.P(),
													],
													className="pink-item",style={"margin-top":"10%"}
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
									className="row w-100",style={"margin-top":"5%"}
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
												html.P("adadawd"),
											],
											className="pink-item",style={"margin-top":"10%"}
										),
										html.Div(
											[
												html.H6(
													"Facilisis mauris parturient, eget vitae",
													className="page-1h",
												),
												html.P("."),
											],
											className="blue-item",style={"margin-top":"10%"}
										),
										html.Div(
											[
												html.H6(
													"Facilisis mauris parturient, eget vitae",
													className="page-1h",
												),
												html.P("adadawd"),
											],
											className="pink-item",style={"margin-top":"10%"}
										),										
									],
									className="five columns",style={"margin-top":"3%"}
								),
								html.Div(
									[
										html.Img(src="assets/LinesVsIncomes.png",style={"width": "100%"}),
										html.Img(src="assets/LinesVsRegions.png",style={"width": "100%"})
									],
									className="seven columns",style={"margin-top":"3%"}
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
        ################## Page 5 - EDA - Basic variables I -- WEIGHT - RESID. AREA
        html.Div(
            [
                html.Div(
                    [
                        getHeader("Analysis", "Demographic variables I.",{"margin-left": "-70px"}),
                        html.Div( # Color conclusions and graphs:  ToDo
                            [
                                html.Div(
                                    [	
										html.Div(
											[
												html.Div(
													[
														html.H6(
															"Weight",
															className="page-1h",
														),
														html.P("We found that many of the infant deaths are related to underweight issues. This is an issue that must be addressed if we want to bring any help on this problem."),
														html.P("The weights for the fetal deaths are obviously very low, since this fetuses don’t reach their full development."),
													],
													className="pink-item",style={"margin-top":"10%"}
												),
												html.Div(
													[
														html.H6(
															"Residence area",
															className="page-1h",
														),
														html.P("Though fetal deaths are more likely to happen in cities, infant deaths are more likely to happen on rural than on urban locations."),
													],
													className="blue-item",style={"margin-top":"30%"}
												),
												
												
												
											], className="six columns"
										),
										html.Div(
											[
												html.Img(src="assets/Weight.png",style={"width": "70%"}),
												html.Img(src="assets/Race.png",style={"width": "70%"})
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
		################## Page 5 - EDA - Basic variables II. MOTHER'S AGE
        html.Div(
            [
                html.Div(
                    [
                        getHeader("Analysis", "Demographic variables II.",{"margin-left": "-70px"}),
                        html.Div( # Color conclusions and graphs:  ToDo
                            [
                                html.Div(
                                    [	
										html.Div(
											[
												html.Div(
													[
														html.H6(
															"Mother's Age",
															className="page-1h",
														),
														html.P("Looking at mother’s age, we found that the probability of a successful birth decreases with the age of the mother, so that older women tend to have lower chances of giving birth."),
													],
													className="pink-item",style={"margin-top":"20%"}
												),
												html.Div(
													[
														html.P("This conclusion also applies to newborns from older moms, their chances of surviving is not as good as that of younger moms (around 25 years old), but the difference is not as striking."),
													],
													className="blue-item",style={"margin-top":"15%"}
												),
											], className="five columns"
										),
										html.Div(
											[
												html.Img(src="assets/MothersAge.png",style={"width": "100%"})
											],
											className="seven columns"
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
		################## Page 6 - EDA - Basic variables III. PARENTS AGE DIST
        html.Div(
            [
                html.Div(
                    [
                        getHeader("Analysis", "Demographic variables III.",{"margin-left": "-70px"}),
                        html.Div( # Color conclusions and graphs:  ToDo
                            [
                                html.Div(
                                    [	
										
										html.Div(
											[
												html.Div(
													[
														html.H6(
															"Mother's age",
															className="page-1h",
														),
														html.P("Though the influence of the father was not assessed on this work, an interesting trend was found: fathers tend to (and can) be older, while mothers are tightly concentrated between 20 and 30 years old."),
													],
													className="pink-item six columns"
												),
												html.Div(
													[
														html.H6(
															"¿Public healt issue?",
															className="page-1h",
														),
														html.P("An issue is spotted here, we have way too many mothers below 20 years old. Future work should focus on the influence this variable has on pregnancy."),
													],
													className="blue-item six columns",
													# style = {"margin-top": "26%"}
												),
												
												
												
											], className="",style={"margin-top": "5%"}
										),
										html.Div(
											[
												html.Img(src="assets/ParentsAgeDist.png",style={"width": "60%","margin-top": "5%", "margin-left": "21%"})
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
		################## Page 7 - EDA - Basic variables IV - Race - cultural, Residence area
        html.Div(
            [
                html.Div(
                    [
                        getHeader("Analysis", "Demographic variables IV.",{"margin-left": "-70px"}),
                        html.Div( # Color conclusions and graphs:  ToDo
                            [
                                html.Div(
                                    [	
										html.Div(
											[
												html.Div(
													[
														html.H6(
															"Race / Cultural identification",
															className="page-1h",
														),
														html.P("While exploring the racial and cultural identification of the baby, we found that these categories behave very differently in terms of infant mortality."),														
													],
													className="pink-item",style={"margin-top": "15%"}
												),
												html.Div(
													[
														html.H6(
															"Residence area",
															className="page-1h",
														),
														html.P("We found that indigenous, rom, and raizal people are more likely to have infant deaths than other races, while ‘None’ was found to have the lowest rate. This may suggest a heavy racial/cultural discrimination within the country or be a consequence of different habits among cultures."),
													],
													className="blue-item",style={"margin-top": "15%"}
												),
												
												
												
											], className="six columns"
										),
										html.Div(
											[
												html.Img(src="assets/fig5_mod.png",style={"width": "100%"})
											],
											className="six columns"
										),
                                    ],
									className="row w-100",style={"margin-top": "3%"}
								),								
                            ],
                            className="page-1n w-100 mt-3"
                        ),
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ),
		################## Page 5 - EDA - - Basic variables V - Death time and proba by time
        html.Div(
            [
                html.Div(
                    [
                        getHeader("Analysis", "Demographic variables V.",{"margin-left": "-70px"}),
                        html.Div( # Color conclusions and graphs:  ToDo
                            [
                                html.Div(
                                    [	
										html.Div(
											[
												html.Div(
													[
														html.H6(
															"Neonate's death probability base on time",
															className="page-1h",
														),
														html.P("A death is most likely to occur in the first moments of life, and this likelihood decays very rapidly as the age increases."),
														html.P("We should take special care of our children as they grow up, but the first week and half year are the most important times!"),
													],
													className="pink-item six columns"
												),
												html.Div(
													[
														html.H6(
															"Neonate's deaths time",
															className="page-1h",
														),
														html.P("If we ask ourselves: at what age do the newborns die (if they do)? We found that most of the deaths occur between 1-5 months, and 1-6 days."),
													],
													className="blue-item six columns"
												),
												
																								
												
											]
										),
										html.Div(
											[
												html.Img(src="assets/deathProb.png", className="six columns",style={"width": "30%","margin-top": "2%","margin-left": "10%"}),
												html.Img(src="assets/AgeRange.png", className="six columns",style={"width": "32%","margin-top": "2%","margin-left": "20%"}),
												
											],
											className="w-100"
										),
                                    ],
									className="row w-100",style={"margin-top": "3%"}
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
		################## Page 5 - EDA - Basic variables VI - Colombian maps
        html.Div(
            [
                html.Div(
                    [
                        getHeader("Analysis", "Demographic variables VI.",{"margin-left": "-70px"}),
                        html.Div( # Color conclusions and graphs:  ToDo
                            [
                                html.Div(
                                    [	
										html.Div(
											[
												html.Div(
													[
														
														html.P("Regarding to the geographical information, different behaviours are expected from different departments given the great economic and cultural differences that exist between them."),
														html.P("Here it is possible to observe those differences reflected in the ratios for fetal and non fetal deaths per department."),
													],
													className="pink-item",style={"margin-top": "5%"}
												),
												html.Div(
													[
														
														html.P("Rural departments located on the peripheries, show a dramatic non-fetal death rate as compared to the central, more urban departments. Fetal deaths reports, on the other hand, seems to be mainly located in the central regions."),
													],
													className="blue-item",style={"margin-top": "10%"}
												),
												html.Div(
													[
														
														html.P("The different behaviour between the fetal and non fetal reports could be explained accounting for people being obligated to report a non-fetal death since, legally, this corresponds already to a person, while fetal deaths can more easily be unreported, especially in rural areas."),
													],
													className="pink-item",style={"margin-top": "10%"}
												),
												
												
											], className="eight columns"
										),
										html.Div(
											[
												html.Img(src="assets/fetal_nonfetal_vertical.png",style={"width": "60%"})
											],
											className="four columns"
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
