import requests
from datetime import datetime
Neuro_API_KEY= "b6aba59d9518c46f1ef2741f75beae2d"
Neuro_AppID= "4486f973"
GENDER= "male"
WEIGHT= "70"
HEIGHT= "160"
AGE= "19"

Neuro_ENDPOINT= "https://trackapi.nutritionix.com/v2/natural/exercise"
Sheety_ENDPOINT= "https://api.sheety.co/d0b1efc67d18564e79bd6d0ed95fa049/opppp/workouts"



Neuro_text= input("Tell about your exercise?")
Neuro_header= {
    "x-app-id": "4486f973",
    "x-app-key": "b6aba59d9518c46f1ef2741f75beae2d",
}

Neuro_params= {
     "query":Neuro_text,
 "gender":GENDER,
 "weight_kg": WEIGHT,
 "height_cm":HEIGHT,
 "age":AGE,
}

response = requests.post(url=Neuro_ENDPOINT, json= Neuro_params, headers= Neuro_header)
result = response.json()

################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

all_exercise= []
constt= 0

for exercise in result["exercises"]:
    sheet_inputs={
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    all_exercise.append(sheet_inputs)
    constt+=1

sheety_header= {
    "Authorization": "Bearer 342sad343#fdscfdsdf",
}

for insa in range (0, constt):
    
    sheet_response = requests.post(Sheety_ENDPOINT, json=all_exercise[insa],headers=sheety_header)

# print(sheet_response.text)