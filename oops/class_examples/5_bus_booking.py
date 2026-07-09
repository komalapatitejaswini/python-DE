class BusBooking:

    company = "APSRTC"

    def __init__(self, passenger, destination,seat_number):
        self.passenger = passenger
        self.destination = destination
        self.seat_number = seat_number

    def reserve_seat(self):
        return f"Seat {self.seat_number} Reserved"

    @classmethod
    def transport(cls):
        return cls.company

    @staticmethod
    def luggage_policy():
        return "20 kg luggage allowed"

    @property
    def ticket_status(self):
        return "Ticket Booked"

    def booking_details(self):
        return (
            f"Passenger       : {self.passenger}\n"
            f"Destination     : {self.destination}\n"
            f"seat number     : {self.reserve_seat()}\n"
            f"Company         : {self.transport()}\n"
            f"Luggage allowed : {self.luggage_policy()}\n"
            f"Status          : {self.ticket_status}"
        )

ticket1 = BusBooking("Tejaswini", "Bangalore","L2")

print(ticket1.passenger)
print(ticket1.destination)
print(ticket1.booking_details())
