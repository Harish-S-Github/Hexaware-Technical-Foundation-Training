class ReservationException(Exception):
    def __init__(self, message="Reservation conflict or error."):
        super().__init__(message)
