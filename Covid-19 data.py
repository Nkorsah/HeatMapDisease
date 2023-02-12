# Python Heatmap project
# api key: 52946c7f007449fdb3f2f6d27620027e
# Commands: https://apidocs.covidactnow.org/data-definitions

import covidactnow

api = covidactnow.User(api_key = '52946c7f007449fdb3f2f6d27620027e')


PAInfectionRate = api.infRate('PA')
massachussettsVaxRate = api.vaxRate('MA')

print(f"{PAInfectionRate = }")
# print(f"{massachussettRiskLevelsOverall = }")
file = open('counties.csv', 'r')
data = file.readlines()
#print(data)
counties = []
# finds the counties in PA
x = 0
for line in data:
    stuff = line.split(",")
    states = stuff[2]
    if states == "PA":
        counties.append(stuff[3])
        x += 1

print(counties)
print(x)
# make a new list for the info for each county we need
fileCounty = open('us_county_latlng.csv','r')

