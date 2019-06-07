from typing import List

from source.domain.room import Room


class RoomsRepository(object):

    def load_rooms(self) -> List[Room]:
        raise NotImplementedError
