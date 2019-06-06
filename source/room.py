from datetime import datetime
from datetime import timedelta

class Room(object):
    def __init__(self, room_numer=1):
        self.booked_dates = []
        self.room_number = room_numer

    def is_available(self, checkin_date, checkout_date):
        room_is_available = True
        for requested_date in self.__get_dates_range(checkin_date, checkout_date):
            if not self.is_available_this_day(requested_date):
                room_is_available = False

        return room_is_available

    def is_available_this_day(self, date: datetime):
        return date not in self.booked_dates

    def book(self, date):
        self.booked_dates.append(date)

    def __str__(self):
        return "Chambre : " + str(self.room_number)

    def __get_dates_range(self, start_date, end_date):
        day_count = (end_date - start_date).days

        dates = []
        for n in range(day_count):
            dates.append(start_date + timedelta(n))

        return dates
