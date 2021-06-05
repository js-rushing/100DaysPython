from data_manager import DataManager
from flight_search import FlightSearch

sheety = DataManager()

sheety.fill_iata_column()

for flight in sheety.data['flights']:
    fs = FlightSearch(flight)
    fs.search_flights()
