class Appointment:
    def __init__(self, appointmentId=None, patientId=None, doctorId=None, appointmentDate=None, description=None):
        self.appointmentId = appointmentId
        self.patientId = patientId
        self.doctorId = doctorId
        self.appointmentDate = appointmentDate
        self.description = description

    # Getter methods
    def get_appointment_id(self):
        return self.appointmentId

    def get_patient_id(self):
        return self.patientId

    def get_doctor_id(self):
        return self.doctorId

    def get_appointment_date(self):
        return self.appointmentDate

    def get_description(self):
        return self.description

    # Setter methods
    def set_appointment_id(self, appointmentId):
        self.appointmentId = appointmentId

    def set_patient_id(self, patientId):
        self.patientId = patientId

    def set_doctor_id(self, doctorId):
        self.doctorId = doctorId

    def set_appointment_date(self, appointmentDate):
        self.appointmentDate = appointmentDate

    def set_description(self, description):
        self.description = description

    def __str__(self):
        return f"Appointment ID: {self.appointmentId}, Patient ID: {self.patientId}, Doctor ID: {self.doctorId}, Date: {self.appointmentDate}, Description: {self.description}"
