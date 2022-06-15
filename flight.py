import csv
import codecs

def GetAirportCode():
    with open('airportCodes.txt', encoding='utf8') as f:
        airportCodes = f.readlines()
        new_list = [str.strip(element) for element in airportCodes]
    return new_list

def GetAirportName():
    with open('airportCityNames.txt', encoding='utf8') as f:
        airportCityNames = f.readlines()
        for name in airportCityNames:
            name.replace("\n", "")
    return airportCityNames
