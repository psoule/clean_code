from datetime import datetime


class Room(object):
    def __init__(self, room_numer=1):
        self.booked_dates = []
        self.room_number = room_numer

    def is_available(self, date: datetime):
        return date not in self.booked_dates

    def book(self, date):
        self.booked_dates.append(date)

    def __str__(self):
        return "Chambre : " + str(self.room_number)
