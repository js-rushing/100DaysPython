import requests
import json
import datetime as dt
from config import NUTRITIONIX_APP_ID, \
    NUTRITIONIX_API_KEY, \
    SHEETY_ENDPOINT, \
    SHEETY_BEARER_TOKEN, \
    WEIGHT, \
    HEIGHT, \
    GENDER, \
    AGE

nutritionix_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_params = {
 "query": "ran 3 miles and cycled 4 miles",
 "gender": GENDER,
 "weight_kg": int(WEIGHT * .4535924),
 "height_cm": int(HEIGHT * 2.54),
 "age": AGE
}
exercise_json = json.dumps(exercise_params)

nut_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "Content-Type": "application/json"
}

nut_res = requests.post(url=nutritionix_url, data=exercise_json, headers=nut_headers)
nut_res_json = (nut_res.json())


def get_sheety_data(obj):
    now = dt.datetime.now()
    dictionary = {
        "workout": {
            "date": f"{now.strftime('%d')}/{now.strftime('%m')}/{now.strftime('%Y')}",
            "time": f"{now.strftime('%H')}:{now.strftime('%M')}:{now.strftime('%S')}",
            "exercise": obj['name'].capitalize(),
            "duration": obj['duration_min'],
            "calories": obj['nf_calories']
        }
    }
    return json.dumps(dictionary)


sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"
}

for item in nut_res_json['exercises']:
    sheety_post_res = requests.post(url=SHEETY_ENDPOINT, data=get_sheety_data(item), headers=sheety_headers)
    print(sheety_post_res.text)
