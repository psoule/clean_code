from source.date_utils import add_days
from source.room import Room
from typing import List, Optional
from datetime import datetime


class Hotel(object):

    def __init__(self, rooms: List[Room]):
        self.rooms = rooms

    def find_available_rooms(self, checkin_date: datetime, checkout_date: Optional[datetime]=None, number_of_guests=1) -> List[Room]:
        if checkout_date is None:
            checkout_date = add_days(checkin_date, 1)

        available_rooms = self.__get_available_rooms(checkin_date, checkout_date, number_of_guests)

        return available_rooms

    def __get_available_rooms(self, checkin_date: datetime, checkout_date: datetime, number_of_guests) -> List[Room]:
        available_rooms = []
        for room in self.rooms:
            if room.room_capacity < number_of_guests:
                continue

            room_is_available = room.is_available(checkin_date, checkout_date)

            if room_is_available:
                available_rooms.append(room)

        return available_rooms

