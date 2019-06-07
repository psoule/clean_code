from datetime import datetime
from abc import ABC
from typing import Optional

from source.domain.booking import Booking


class IHotel(ABC):

    def book_room(self, booking: Booking):
        raise NotImplementedError

    def find_available_rooms(self, checkin_date: datetime, checkout_date: Optional[datetime], number_of_guests: int):
        raise NotImplementedError


