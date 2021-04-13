travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]
# Do not change the code above

# todo: Write the function that will allow new country
# to be added to the travel_log.


def add_new_country(country, visits, cities):
    travel_log.append({"country": country, "visits": visits, "cities": cities})


# Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg", "Leningrad"])
print(travel_log)
