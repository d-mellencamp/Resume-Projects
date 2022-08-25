import re
import math
from geopy.geocoders import Nominatim
from datetime import date
import datetime
import time

# radius in kilometers
earth_radius = 6372800
# price per gallon
fuel_price = 2.46
# miles per gallon
mpg = 51

average_passengers = 230
current_day = date.today()


class Client:
    def __init__(self, name):
        self.name = name

    def client_info(self):
        print("Make sure to put the city last so the coordinates are accurate.")
        x = 0
        while x < 1:
            self.departing = input("Where are you departing from?(State|City) ").title().strip()
            location = Nominatim(user_agent="get_location")
            self.get_location = location.geocode(f"{self.departing}")
            if self.get_location is not None:
                x += 1
            else:
                pass
        y = 0
        while y < 1:
            self.arriving = input("Where would you like to go?(State|City) ").title().strip()
            location2 = Nominatim(user_agent="next_location")
            self.get_location2 = location2.geocode(f"{self.arriving}")
            if self.get_location2 is not None:
                y += 1
            else:
                pass

    def flight_date(self):
        while True:
            try:
                year, month, day = input("What day are you wanting to book a flight?(YYYY-MM-DD) ").split("-")
                flight_time = datetime.date(int(year), int(month), int(day))
            except ValueError:
                pass
            else:
                break
        if int(month) == 1:
            self.month_factor = .90
        else:
            self.month_factor = 1
        time_difference = flight_time - current_day
        print(time_difference)
        print(f"Departure-Date: {flight_time.strftime('%a, %b, %d, %Y')}")
        if int(str(time_difference)[0:2]) > 24:
            self.time_factor = .95
        else:
            self.time_factor = 1
        if flight_time.strftime("%a") == "Fri":
            self.day_factor = .90
        else:
            self.day_factor = 1

    def distance_calculation(self):
        lat1, lon1 = (self.get_location.latitude, self.get_location.longitude)
        lat2, lon2 = (self.get_location2.latitude, self.get_location2.longitude)
        phi1, phi2 = math.radians(lat1), math.radians(lat2)
        dphi = math.radians(lat2 - lat1)
        dlambda = math.radians(lon2 - lon1)

        a = math.sin(dphi / 2) ** 2 + \
            math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
        distance_km = 2 * earth_radius * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance_miles = 2 * earth_radius * math.atan2(math.sqrt(a), math.sqrt(1 - a)) * 0.621371
        distance_price_factor = (distance_miles / mpg * fuel_price)
        total = (distance_price_factor / average_passengers) * self.time_factor * self.month_factor * self.day_factor
        print(f"{self.name}, your ticket price should be ~ ${total:,.2f} (one-way|economy)")


client = Client(input("Name? "))
client.client_info()
client.flight_date()
client.distance_calculation()


