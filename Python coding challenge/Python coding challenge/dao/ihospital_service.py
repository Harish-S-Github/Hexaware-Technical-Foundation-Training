# dao/ihospital_service.py

from abc import ABC, abstractmethod
from entity.appointment import Appointment
from typing import List

class IHospitalService(ABC):

    @abstractmethod
    def get_appointment_by_id(self, appointmentId: int) -> Appointment:
        pass

    @abstractmethod
    def get_appointments_for_patient(self, patientId: int) -> List[Appointment]:
        pass

    @abstractmethod
    def get_appointments_for_doctor(self, doctorId: int) -> List[Appointment]:
        pass

    @abstractmethod
    def schedule_appointment(self, appointment: Appointment) -> bool:
        pass

    @abstractmethod
    def update_appointment(self, appointment: Appointment) -> bool:
        pass

    @abstractmethod
    def cancel_appointment(self, appointmentId: int) -> bool:
        pass
