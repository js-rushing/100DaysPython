import datetime as dt


class FlightData:
    def __init__(self, data):
        self.data = data['data'][0]
        self.price = self.data['price']
        self.departure_airport = self.data['flyFrom']
        self.departure_city = self.data['cityFrom']
        self.arrival_airport = self.data['flyTo']
        self.arrival_city = self.data['cityTo']
        self.nights = self.data['nightsInDest']
        self.out_date_date = self.data['route'][0]['local_departure'].split("T")[0].split("-")
        self.out_date = dt.date(year=int(self.out_date_date[0]),
                                month=int(self.out_date_date[1]),
                                day=int(self.out_date_date[2]))
        self.in_date = (self.out_date + dt.timedelta(days=int(self.nights)))
        self.flight_dict = self.create_dict()

    def create_dict(self):
        flight_dict = {
            "price": self.price,
            "depAirport": self.departure_airport,
            "depCity": self.departure_city,
            "arrAirport": self.arrival_airport,
            "arrCity": self.arrival_city,
            "nights": self.nights,
            "outDate": self.out_date.strftime("%D"),
            "inDate": self.in_date.strftime("%D")
        }
        return flight_dict
