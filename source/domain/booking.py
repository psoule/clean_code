import datetime


class Booking(object):
    def __init__(self, room_number: int, number_of_guests: int, checkin_date: datetime, checkout_date: datetime):
        self.room_number = room_number
        self.number_of_guests = number_of_guests
        self.checkin_date = checkin_date
        self.checkout_date = checkout_date
