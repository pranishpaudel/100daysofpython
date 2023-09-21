import requests
from twilio.rest import Client


account_sid = 'AC735f488486c5e456149dc6d676e5da3a'
auth_token = '4f3901e93275285aeb13e3271353045a'


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


will_rain= False

for weather_time in range (0,13):

    curr_time= weather_dataa(weather_time)
    if curr_time <700:
        print(f"It will rain at {weather_time} whose value is {curr_time}")
        will_rain= True

if will_rain== True:
    print("Bring an umbrella")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_='+13147206151',
    body='Bring umbrella',
    to='+9779741786403'
    )

    print(message.sid)














    
