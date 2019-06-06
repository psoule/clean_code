from source.booking import Booking
from source.date_utils import add_days, get_dates_range
from source.room import Room
from typing import List, Optional
from datetime import datetime


class Hotel(object):
    MINIMUM_NIGHTS_STAY = 1

    def __init__(self, rooms: List[Room]):
        self.rooms = rooms

    def book_room(self, booking: Booking):
        dates_range = get_dates_range(booking.checkin_date, booking.checkout_date)
        room = self.find_room_by_number(room_number=booking.room_number)
        for date in dates_range:
            room.book(date)

    def find_available_rooms(self, checkin_date: datetime, checkout_date: Optional[datetime]=None, number_of_guests=1) -> List[Room]:
        if checkout_date is None:
            checkout_date = add_days(checkin_date, self.MINIMUM_NIGHTS_STAY)
        elif (checkout_date - checkin_date).days < self.MINIMUM_NIGHTS_STAY:
            raise ValueError("You must have at least {} nights".format(self.MINIMUM_NIGHTS_STAY))

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

    def find_room_by_number(self, room_number: int) -> Optional[Room]:
        for room in self.rooms:
            if room.room_number == room_number:
                return room
        return None
