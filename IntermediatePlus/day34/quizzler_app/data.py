import requests

params = {
    "amount": 10,
    "type": "boolean",
    "difficulty": "medium",
}

res = requests.get("https://opentdb.com/api.php", params=params)

question_data = res.json()['results']
