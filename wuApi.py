#Weather api
import os
import wuInput
import json
import urllib.parse
import urllib.request

API_KEY = os.environ["WU_API_KEY"]
BASE_URL = 'http://api.wunderground.com/api/'
FORECAST_URL = BASE_URL + API_KEY + '/forecast10day/q/'


def build_url(city:str,state:str)->str:
    '''takes in a list of locations and returns the string url...url has json map info'''
    city = city.split()
    city = '_'.join(city) + '.json'
    return FORECAST_URL + state + '/' + city


def get_result(url: str)->dict:
    '''this will recieve the json text'''
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)
    finally:
        if response != None:
            response.close()


def parse(json: dict):
    rWeather = {}
    allWeather = {}
    for x in range(len(json["forecast"]["simpleforecast"]["forecastday"])):
        extended_date = json["forecast"]["simpleforecast"]["forecastday"][x]["date"]["pretty"]
        split_date = extended_date.split()
        date = ' '.join(split_date[-3:])
        conditions = json["forecast"]["simpleforecast"]["forecastday"][x]["conditions"]
        high = json["forecast"]["simpleforecast"]["forecastday"][x]["high"]["fahrenheit"]
        low = json["forecast"]["simpleforecast"]["forecastday"][x]["low"]["fahrenheit"]
        #print(date)
        #print(conditions)
        print()
        if 'thunder' in conditions.lower():
            rWeather[date] = [conditions,high,low]
        allWeather[date] = [conditions, high, low]
    #return rWeather
    return allWeather
        
    
