import os
from datetime import datetime
from unittest.mock import MagicMock

from source.adapters.hotel_service import HotelService
from source.adapters.json_rooms_repository import JsonRoomsRepository
from source.domain.booking import Booking
from source.domain.ports.rooms_repository import RoomsRepository
from source.utils.date_utils import DATE_FORMAT
from source.domain.hotel import Hotel
from source.domain.room import Room


def test_find_available_rooms():
    # Given
    checkin_date = datetime.strptime('2019-02-21', DATE_FORMAT)
    checkout_date = datetime.strptime('2019-02-23', DATE_FORMAT)
    number_of_guests = 2

    room_101 = Room(101, room_capacity=2)
    room_102 = Room(102, room_capacity=4)
    room_103 = Room(103, room_capacity=1)
    room_104 = Room(104, room_capacity=2)

    hotel_cuzco = Hotel([room_101, room_102, room_103, room_104])

    booked_room_102_date = datetime(2019, 2, 21)
    room_102.book(booked_room_102_date)

    booked_room_104_date = datetime(2019, 2, 7)
    room_104.book(booked_room_104_date)

    # When
    available_rooms = hotel_cuzco.find_available_rooms(checkin_date, checkout_date, number_of_guests)

    # Then
    assert available_rooms == [room_101, room_104]


def test_book_a_room_for_3_nights():
    # Given
    to_booked_room_number = 102
    number_of_guests = 4
    checkin_date = datetime(2019, 6, 1)
    checkout_date = datetime(2019, 6, 5)

    booking = Booking(to_booked_room_number, number_of_guests, checkin_date, checkout_date)

    room_101 = Room(101, room_capacity=2)
    room_102 = Room(102, room_capacity=4)

    hotel_cuzco = Hotel([room_101, room_102])

    # When
    hotel_cuzco.book_room(booking)

    # Then
    assert not room_102.is_available_this_day(datetime(2019, 6, 3))
    assert room_102.is_available_this_day(datetime(2019, 5, 31))
    assert room_102.is_available_this_day(datetime(2019, 6, 5))


def test_build_hotel():
    # Given
    room_101 = Room(101, room_capacity=2)
    room_102 = Room(102, room_capacity=4)

    rooms_repo = MagicMock()
    rooms_repo.load_rooms = MagicMock()
    rooms_repo.load_rooms.return_value = [room_101, room_102]

    hotel_service = HotelService(rooms_repo)

    # When
    hotel = hotel_service.build_hotel()

    # Then
    assert hotel.rooms == [room_101, room_102]


def test_rooms_repository_load_rooms():
    # Given
    json_rooms = {
        "rooms":
            [
                {
                    "room_number": 101,
                    "room_capacity": 2
                },
                {
                    "room_number": 102,
                    "room_capacity": 4
                }
            ]
    }
    json_rooms_repository = JsonRoomsRepository('')
    json_rooms_repository._read_json_file = MagicMock()
    json_rooms_repository._read_json_file.return_value = json_rooms

    # Then
    loaded_rooms = json_rooms_repository.load_rooms()

    # When
    assert len(loaded_rooms) == 2
