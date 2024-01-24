#! /usr/bin/env python3
from rich import print
import json, requests, sys, os
APPID = "3613218da280231472c1d36b7dfd4b65"
os.system('clear')

#Compute location from the command line arguments.
if len(sys.argv) < 2 :
    print ('Usage: weather.py city_name,2-letter_country_code')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
url =f'http://api.openweathermap.org/data/2.5/weather?q={location}&APPID={APPID}'
response = requests.get(url)
response.raise_for_status()

#print(response.text)  
data = json.loads(response.text)
weather_info = round ( (float (data [ 'main']['temp']) - 273.15), 1 )
print (weather_info)
#print(json.dumps(data, indent=4))  
 