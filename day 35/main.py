import requests

OWM_ENDPOINT= "https://api.openweathermap.org/data/2.5/onecall"
API_KEY= "419af21a0f4c404bed756a44151dd652"

weather_params= {
    "lat" :28.237988,
    "lon": 83.995590,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
}

answer= requests.get(OWM_ENDPOINT, params= weather_params)
answer.raise_for_status()
weather_data= answer.json()
weather_data_hourly= weather_data["hourly"]



def weather_dataa(weather_time):
    initial_val= weather_data_hourly[weather_time]["weather"][0]["id"]
    return initial_val

for weather_time in range (0,13):

    curr_time= weather_dataa(weather_time)
    if curr_time <700:
        print(f"It will rain at {weather_time} whose value is {curr_time}")






    
