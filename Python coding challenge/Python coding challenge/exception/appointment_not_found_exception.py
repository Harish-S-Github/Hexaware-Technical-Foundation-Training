# exception/appointment_not_found_exception.py

class AppointmentNotFoundException(Exception):
    def __init__(self, message="Appointment not found in the database"):
        super().__init__(message)

