# exception/patient_number_not_found_exception.py

class PatientNumberNotFoundException(Exception):
    def __init__(self, message="Patient number not found in the database"):
        # Initialize with a custom message
        self.message = message
        super().__init__(self.message)
