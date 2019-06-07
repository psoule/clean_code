import json
from typing import List

from source.domain.ports.rooms_repository import RoomsRepository
from source.domain.room import Room


class JsonRoomsRepository(RoomsRepository):

    def __init__(self, json_path: str):
        super().__init__()
        self.json_path = json_path

    def load_rooms(self) -> List[Room]:
        rooms_data = self._read_json_file()
        rooms = []
        for room_data in rooms_data["rooms"]:
            rooms.append(Room(**room_data))

        return rooms

    def _read_json_file(self):
        with open(self.json_path, 'r') as input_file:
            rooms_data = json.load(input_file)

        return rooms_data
