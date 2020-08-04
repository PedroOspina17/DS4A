This file gives a description of the files composing the code base

- DataCleaning: Data cleaning for the principal dataset
- DataPrepForFE: Deals with the preparation of the data files for use in the front-end app.
- DB_create: Create the DB-RDS columns
- EDA_final: Exploratory Data Analysis. This notebook produces most of the barplots in the document (plus some extra that aren't discussed there)
- educacion: This notebook is for loading and cleaning an additional dataset that used when attempting to do predictions on time-series. (Education data)
- MergeDatasets: Merge the already cleaned datasets. (As they come in 3 different files for each year)
- SARIMATimeSeries: Train the SARIMA models presented in the document
- visualization_departments: Some static maps to be used in document and FE
- PreprocessingModels = This gets a random sample of the dataframe to work with. In addition to obtaining the numerical categories of the categorical variables.
- CorrelationsAndLogisticRegression = Obtains the correlation matrix and the logistic regression model with their respective coefficient graphs.
- RandomForest_DecisionTree = Obtains the correlation matrix and the ROC curve for decision tree and random forest, also obtain features importance using the random forest model.
- HT: Hypothesis tests and some EDA
- WorldData: Graphs with data from The WHO and The World Bank to compare Colombian situation to the rest of the world 
- ModelForInfantDeaths: In this notebook we try to merge the 2017 Births and Non Fetal Datasets and produce a logistic regression model