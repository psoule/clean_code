from datetime import datetime

from source.utils.date_utils import DATE_FORMAT
from source.domain.hotel import Hotel
from source.domain.room import Room


def init_hotel():
    room1 = Room(101)
    room2 = Room(102)
    room3 = Room(103)

    booked_date = datetime(2019, 6, 4)
    room2.book(booked_date)

    rooms_in_hotel = [room1, room2, room3]
    hotel = Hotel(rooms_in_hotel)
    return hotel


def main():
    print("Bienvenue à l'Hotel Cuzco")
    hotel = init_hotel()

    beginning_date = input("Date d'arrivée dans l'hotel : ")
    beginning_date = datetime.strptime(beginning_date, DATE_FORMAT)
    end_date = input("Date de sortie dans l'hotel : ")
    end_date = datetime.strptime(end_date, DATE_FORMAT)

    available_rooms = hotel.find_available_rooms(beginning_date, end_date)

    for room in available_rooms:
        print(room)


main()