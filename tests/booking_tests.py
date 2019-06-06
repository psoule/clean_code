from source.hotel import Hotel
from source.room import Room
from datetime import datetime


def test_room_object_as_specified_floor():
    # Given

    # When
    room = Room()

    # Then
    assert room is not None


def test_hotel_has_specified_rooms():
    # Given
    room1 = Room()
    room2 = Room()
    room3 = Room()

    rooms_in_hotel = [room1, room2, room3]

    # When
    hotel = Hotel(rooms_in_hotel)

    # Then
    assert len(hotel.rooms) == 3
    assert [room1, room2, room3] == hotel.rooms


def test_room_availability():
    # Given
    room = Room()
    date = datetime.utcnow()

    # When
    availability = room.is_available_this_day(date)
    # Then
    assert availability is True


def test_room_booking():
    # Given
    date = datetime.utcnow()
    room = Room()
    room.book(date)

    # When
    availability = room.is_available_this_day(date)

    # Then
    assert availability is False


def test_room_is_available_at_04042019():
    # Given
    booked_date1 = datetime(2019, 4, 3)
    booked_date2 = datetime(2019, 4, 5)
    available_date = datetime(2019, 4, 4)

    room = Room()
    room.book(booked_date1)
    room.book(booked_date2)

    # When
    availability = room.is_available_this_day(available_date)

    # Then
    assert availability is True


def test_find_available_room():
    # Given
    room1 = Room()
    room2 = Room()

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
    room1 = Room()
    room2 = Room()
    room3 = Room()

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

    print(available_rooms)

    # Then
    assert len(available_rooms) == 2
    assert room2 in available_rooms
    assert room1 not in available_rooms
    assert room3 in available_rooms
