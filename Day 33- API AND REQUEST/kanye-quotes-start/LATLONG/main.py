import requests
from datetime import datetime
MY_LAT= 28.237988
MY_LONG= 83.995590


parameteers= {
    "lat":MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response= requests.get("https://api.sunrise-sunset.org/json", params=parameteers)
data= response.json()
print(data.split("T"))

time_now= datetime.now()
print(time_now)