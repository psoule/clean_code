from datetime import datetime
from datetime import timedelta

class Room(object):
    def __init__(self, room_numer=1):
        self.booked_dates = []
        self.room_number = room_numer

    def is_available(self, checkin_date, checkout_date):
        day_count = (checkout_date - checkin_date).days

        room_is_available = True
        for requested_date in (checkin_date + timedelta(n) for n in range(day_count)):
            if not self.is_available_this_day(requested_date):
                room_is_available = False

        return room_is_available

    def is_available_this_day(self, date: datetime):
        return date not in self.booked_dates

    def book(self, date):
        self.booked_dates.append(date)

    def __str__(self):
        return "Chambre : " + str(self.room_number)
