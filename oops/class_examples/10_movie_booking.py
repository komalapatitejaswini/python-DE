class MovieBooking:

    theatre = "PVR Cinemas"

    def __init__(self, customer_name, movie, seat_number):
        self.customer_name = customer_name
        self.movie = movie
        self.seat_number = seat_number

    def reserve_seat(self):
        return f"Seat {self.seat_number} Reserved"

    @classmethod
    def theatre_name(cls):
        return cls.theatre

    @staticmethod
    def cancellation():
        return "Cancellation allowed before 2 hours"

    @property
    def booking_status(self):
        return "Ticket Confirmed"

    def booking_details(self):
        return (
            f"Customer    : {self.customer_name}\n"
            f"Movie       : {self.movie}\n"
            f"Seat number : {self.reserve_seat()}\n"
            f"Theatre name: {self.theatre_name()}\n"
            f"Cancellation: {self.cancellation()}\n"
            f"Status      : {self.booking_status}"
        )

movie1 = MovieBooking("Tejaswini", "Devara","H12")

print(movie1.customer_name)
print(movie1.movie)
print(movie1.booking_details())