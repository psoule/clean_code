from datetime import timedelta

from source.room import Room
from typing import List


class Hotel(object):

    def __init__(self, rooms: List[Room]):
        self.rooms = rooms

    def find_available_room(self, requested_begining_date, requested_end_date=None):
        if requested_end_date is None:
            requested_end_date = requested_begining_date + timedelta(1)

        available_rooms = []
        for room in self.rooms:
            room_is_available = self.is_room_available(requested_begining_date, requested_end_date, room)

            if room_is_available:
                available_rooms.append(room)

        return available_rooms

    def is_room_available(self, requested_begining_date, requested_end_date, room):
        day_count = (requested_end_date - requested_begining_date).days

        room_is_available = True
        for requested_date in (requested_begining_date + timedelta(n) for n in range(day_count)):
            if not room.is_available(requested_date):
                room_is_available = False

        return room_is_available
