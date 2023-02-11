# Python Heatmap project
# api key: 52946c7f007449fdb3f2f6d27620027e

import covidactnow

api = covidactnow.User(api_key = '52946c7f007449fdb3f2f6d27620027e')

washingtonInfectionRate = api.infRate('WA')
massachussettsVaxRate = api.vaxRate('MA')

print(f"{washingtonInfectionRate = }")
print(f"{massachussettsVaxRate = }")