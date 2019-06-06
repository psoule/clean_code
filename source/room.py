from datetime import datetime

from source.date_utils import get_dates_range


class Room(object):
    def __init__(self, room_number, room_capacity):
        self.__booked_dates = []
        self.room_number = room_number
        self.room_capacity = room_capacity

    def is_available(self, checkin_date: datetime, checkout_date: datetime) -> bool:
        for requested_date in get_dates_range(checkin_date, checkout_date):
            if not self.is_available_this_day(requested_date):
                return False
        return True

    def is_available_this_day(self, date: datetime) -> bool:
        return date not in self.__booked_dates

    def book(self, date: datetime):
        self.__booked_dates.append(date)

    def __str__(self):
        return "Chambre : " + str(self.room_number)
