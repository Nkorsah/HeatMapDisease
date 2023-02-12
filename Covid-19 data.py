# Python Heatmap project
# api key: 52946c7f007449fdb3f2f6d27620027e
# Commands: https://apidocs.covidactnow.org/data-definitions

import covidactnow
import csv

api = covidactnow.User(api_key = '52946c7f007449fdb3f2f6d27620027e')



# Create list of the counties and FIPS codes
countiesFile = open('counties.csv', 'r')
countiesLines = countiesFile.readlines()
countiesList = []
countiesFIPS = []

# Append counties and FIPS codes to lists
for line in countiesLines:
    linelist = line.split(',')
    if linelist[2] == "PA":
        countiesList.append(linelist[3])
        countiesFIPS.append(linelist[6][24:29:])

#Create dictionary of County, long and lat

countyRisk = {}

for line in countiesLines:
     linelist = line.split(',')
     if linelist[2] == "PA":
          
          

with open('us_county_latlng.csv' , 'r') as file:
    fileLines = file.readlines()

    for line in fileLines:
        lineList = line.split(',')
        if lineList[0] in countiesFIPS:

            #Append the jawns the match into this file

            with open('complete.csv' , 'wb') as final:
                    writer = csv.writer(final)
                    data = lineList[0],lineList[1],lineList[2],lineList[3][:-2:]
                    print(data)
                    writer.writerow(data)


# Create csv with county name, longitude, latitude

    
#with open('us_county_latlng.csv' , 'r') as file:
   # lines = file.readlines()
    #for line in lines:
        #lineslist = lines.split(',')
       # if lineslist[0] == countiesFIPS:
