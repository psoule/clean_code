from source.room import Room
from typing import List
from datetime import timedelta

class Hotel(object):

    def __init__(self, rooms: List[Room]):
        self.rooms = rooms

    def find_available_rooms(self, checkin_date, checkout_date=None):
        if checkout_date is None:
            checkout_date = self.__add_days(checkin_date, 1)

        available_rooms = self.__get_available_rooms(checkin_date, checkout_date)

        return available_rooms

    def __get_available_rooms(self, checkin_date, checkout_date):
        available_rooms = []
        for room in self.rooms:
            room_is_available = room.is_available(checkin_date, checkout_date)

            if room_is_available:
                available_rooms.append(room)

        return available_rooms

    def __add_days(self, date, number_days):
        return date + timedelta(number_days)
