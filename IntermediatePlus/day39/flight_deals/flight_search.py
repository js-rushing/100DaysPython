import requests
import datetime as dt
from config import TEQUILA_API_KEY, TEQUILA_URL
from flight_data import FlightData
from notification_manager import NotificationManager


class FlightSearch:
    def __init__(self, city_obj):
        self.city_obj = city_obj
        self.city = self.city_obj['city']
        self.iata_code = self.get_iata_code()

    def get_iata_code(self):
        iata_url = f"{TEQUILA_URL}/locations/query"
        iata_params = {
            "term": self.city,
            "limit": 1
        }
        headers = {
            "apikey": TEQUILA_API_KEY,
            "accept": "application/json"
        }

        iata_res = requests.get(url=iata_url, headers=headers, params=iata_params)
        data = iata_res.json()
        return data['locations'][0]['code']

    def search_flights(self):
        date_now = dt.datetime.now()
        search_url = f"{TEQUILA_URL}/v2/search"
        search_headers = {
            "apikey": TEQUILA_API_KEY,
            "accept": "application/json"
        }
        search_params = {
            "fly_from": "LON",
            "fly_to": self.city_obj['iataCode'],
            "date_from": date_now.strftime("%d/%m/%Y"),
            "date_to": (date_now + dt.timedelta(days=(6*30))).strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "GBP",
            "flight_type": "round",
            "one_for_city": 1
        }
        search_res = requests.get(url=search_url, headers=search_headers, params=search_params)
        search_data = search_res.json()
        if len(search_data['data']) > 0:
            flight_data_result = FlightData(search_data)
        else:
            flight_data_result = None
        if flight_data_result:
            if flight_data_result.price < self.city_obj['lowestPrice']:
                text_message = NotificationManager(flight_data_result.flight_dict)
                text_message.send_text()
            else:
                print("No Deal")
