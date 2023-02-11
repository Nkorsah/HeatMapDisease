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
data = open('counties.csv', 'r')

