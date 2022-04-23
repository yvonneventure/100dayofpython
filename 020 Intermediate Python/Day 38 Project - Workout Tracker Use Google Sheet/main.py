ENDPOINT="https://trackapi.nutritionix.com/v2/natural/exercise"
API_Key="af3eff5f4c31b97d6685d0f1410fb5b5"
API_ID="1d51e05e"

heads={
    "x-app-id":API_ID,
    "x-app-key" : API_Key,
}
params={
    "query": "I ran 3 kilos",
}
import datetime
import requests
response=requests.post(url=ENDPOINT,json=params,headers=heads)
result=response.json()
print(result)

SHEETY="https://api.sheety.co/6e836f5a587a97a40c865d7bc1fe52fc/workoutTacker/workouts"


today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=SHEETY,json=sheet_inputs)

    print(sheet_response.text)