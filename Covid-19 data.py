# Python Heatmap project
# api key: 52946c7f007449fdb3f2f6d27620027e
# Commands: https://apidocs.covidactnow.org/data-definitions

import covidactnow

api = covidactnow.User(api_key = '52946c7f007449fdb3f2f6d27620027e')


PAInfectionRate = api.infRate('PA')
massachussettsVaxRate = api.vaxRate('MA')

print(f"{PAInfectionRate = }")
print(f"{massachussettsVaxRate = }")
#print(actuals.cases)

#iso1:us#iso2:us-ok#fips:40133

countiesFile = open('counties.csv', 'r')
countiesLines = countiesFile.readlines()
countiesList = []
countiesFIPS = []


for line in countiesLines:
    #print(line[9:11])
    linelist = line.split()
    print(linelist[1])
    if linelist[2] == "PA":
        print("True")
        countiesList.append(line[3])
        countiesFIPS.append(line[5[-1:-5]])

print(countiesList, countiesFIPS)




    
#with open('us_county_latlng.csv' , 'r') as file:
   # lines = file.readlines()
    #for line in lines:
        #lineslist = lines.split(',')
       # if lineslist[0] == countiesFIPS:
