import dash



#Dropdown for departments dictionary
dropDownOptions = [{'label':dptoCodeNames.iloc[i].Name,'value':dptoCodeNames.iloc[i].code} for i in dptoCodeNames.index]

#Slider marks:
sliderMarks = {year:{'label':str(year),'style':{'color':'#F0FFFF'}} for year in range(2008,2019,2)}
