import requests
from config import SHEETY_URL, ENVIRONMENT
from flight_search import FlightSearch


class DataManager:
    def __init__(self):
        if ENVIRONMENT == "Production":
            # USE THIS FOR PRODUCTION
            self.data = requests.get(url=f"{SHEETY_URL}/flights").json()
        else:
            # USE THIS FOR DEVELOPMENT
            self.data = {
                'flights': [
                    {'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2},
                    {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3},
                    {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4},
                    {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5},
                    {'city': 'Instanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6},
                    {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7},
                    {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8},
                    {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9},
                    {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10}
                ]
            }
        self.flights = self.data['flights']
        self.cities = [city['city'] for city in self.flights]
        self.iata_codes = [iata['iataCode'] for iata in self.flights]
        self.prices = [price['lowestPrice'] for price in self.flights]
        self.temp_iata_list = []

    def fill_iata_column(self):
        if self.iata_codes[0] == "":
            for flight in self.flights:
                fs = FlightSearch(flight)
                index = self.cities.index(flight['city']) + 2
                iata_data = {
                    "flight": {
                        "iataCode": f"{fs.iata_code}"
                    }
                }
                if ENVIRONMENT == "Production":
                    iata_res = requests.put(url=f"{SHEETY_URL}/flights/{index}", json=iata_data)
                    print(iata_res.text)
                else:
                    pass
            if ENVIRONMENT != "Production":
                print(f"Env: {ENVIRONMENT}")
            self.update_data()

    def update_data(self):
        if ENVIRONMENT == "Production":
            # PRODUCTION
            self.data = requests.get(url=SHEETY_URL).json()
        else:
            # DEVELOPMENT
            self.data = {
                'flights': [
                    {'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2},
                    {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3},
                    {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4},
                    {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5},
                    {'city': 'Instanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6},
                    {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7},
                    {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8},
                    {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9},
                    {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10}
                ]
            }
        self.flights = self.data['flights']
        self.cities = [city['city'] for city in self.flights]
        self.iata_codes = [iata['iataCode'] for iata in self.flights]
        self.prices = [price['lowestPrice'] for price in self.flights]
