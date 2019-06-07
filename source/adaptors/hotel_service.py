from source.domain.hotel import Hotel
from source.domain.ports.rooms_repository import RoomsRepository


class HotelService(object):

    def __init__(self, rooms_repository: RoomsRepository):
        self.rooms_repository = rooms_repository

    def build_hotel(self):
        rooms = self.rooms_repository.load_rooms()

        return Hotel(rooms)