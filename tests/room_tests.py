from datetime import datetime

from source.room import Room


def test_room_availability():
    # Given
    room = Room(101, 2)
    date = datetime.utcnow()

    # When
    availability = room.is_available_this_day(date)
    # Then
    assert availability is True


def test_room_booking():
    # Given
    date = datetime.utcnow()
    room = Room(101, 2)
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

    room = Room(101, 2)
    room.book(booked_date1)
    room.book(booked_date2)

    # When
    availability = room.is_available_this_day(available_date)

    # Then
    assert availability is True