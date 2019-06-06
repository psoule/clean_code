from source.room import Room
from typing import List
from datetime import timedelta

class Hotel(object):

    def __init__(self, rooms: List[Room]):
        self.rooms = rooms

    def find_available_room(self, requested_begining_date, requested_end_date=None):
        if requested_end_date is None:
            requested_end_date = requested_begining_date + timedelta(1)

        available_rooms = []
        for room in self.rooms:
            room_is_available = room.is_available(requested_begining_date, requested_end_date)

            if room_is_available:
                available_rooms.append(room)

        return available_rooms
