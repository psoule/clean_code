import pytest

from source.domain.hotel import Hotel
from source.domain.room import Room
from datetime import datetime


def test_hotel_has_specified_rooms():
    # Given
    room1 = Room(101, 2)
    room2 = Room(102, 2)
    room3 = Room(103, 2)

    rooms_in_hotel = [room1, room2, room3]

    # When
    hotel = Hotel(rooms_in_hotel)

    # Then
    assert len(hotel.rooms) == 3
    assert [room1, room2, room3] == hotel.rooms


def test_find_available_room():
    # Given
    room1 = Room(101, 2)
    room2 = Room(102, 2)

    rooms_in_hotel = [room1, room2]
    hotel = Hotel(rooms_in_hotel)

    booked_room1_date = datetime(2019, 5, 3)
    room1.book(booked_room1_date)

    # When
    available_rooms = hotel.find_available_rooms(booked_room1_date)

    # Then
    assert len(available_rooms) == 1
    assert room2 in available_rooms


def test_find_available_room_between_two_given_dates():
    # Given
    room1 = Room(101, 2)
    room2 = Room(102, 2)
    room3 = Room(103, 2)

    rooms_in_hotel = [room1, room2, room3]
    hotel = Hotel(rooms_in_hotel)

    begining_booking_date = datetime(2019, 5, 3)
    end_booking_date = datetime(2019, 5, 5)

    room1_booked_date = datetime(2019, 5, 3)
    room2_booked_date = datetime(2019, 5, 5)

    room1.book(room1_booked_date)
    room2.book(room2_booked_date)

    # When
    available_rooms = hotel.find_available_rooms(begining_booking_date, end_booking_date)

    # Then
    assert len(available_rooms) == 2
    assert room2 in available_rooms
    assert room1 not in available_rooms
    assert room3 in available_rooms


def test_find_available_room_with_capacity_superior_to_number_of_guests():
    # Given
    room1 = Room(101, 4)
    room2 = Room(102, 2)

    number_of_guests = 3

    rooms_in_hotel = [room1, room2]
    hotel = Hotel(rooms_in_hotel)

    checkin_date = datetime(2019, 5, 3)

    # When
    available_rooms = hotel.find_available_rooms(checkin_date, number_of_guests=number_of_guests)

    # Then
    assert available_rooms == [room1]


def test_checkin_range_is_greater_than_minimum_nights_stay():
    # Given
    room101 = Room(101, 2)
    number_of_guests = 1

    hotel = Hotel([room101])

    checkin_date = datetime(2019, 6, 5)
    checkout_date = datetime(2019, 6, 5)

    # When Then
    with pytest.raises(Exception):
        assert hotel.find_available_rooms(checkin_date, checkout_date, number_of_guests=number_of_guests)


