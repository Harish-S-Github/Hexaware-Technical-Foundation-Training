from dao.ihospital_service import IHospitalService
from entity.appointment import Appointment
from util.db_conn_util import DBConnUtil
from exception.database_connection_exception import DatabaseConnectionException
from typing import List

class HospitalServiceImpl(IHospitalService):
    def __init__(self):
        self.connection = DBConnUtil.get_connection()

    def get_appointment_by_id(self, appointmentId: int) -> Appointment:
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Appointment WHERE appointmentId = ?"
            cursor.execute(query, (appointmentId,))
            row = cursor.fetchone()
            if row:
                return Appointment(
                    appointmentId=row[0],
                    patientId=row[1],
                    doctorId=row[2],
                    appointmentDate=row[3],
                    description=row[4]
                )
            return None
        except Exception as e:
            raise DatabaseConnectionException(f"Error fetching appointment by ID: {str(e)}")

    def get_appointments_for_patient(self, patientId: int) -> List[Appointment]:
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Appointment WHERE patientId = ?"
            cursor.execute(query, (patientId,))
            rows = cursor.fetchall()
            appointments = []
            for row in rows:
                appointments.append(Appointment(
                    appointmentId=row[0],
                    patientId=row[1],
                    doctorId=row[2],
                    appointmentDate=row[3],
                    description=row[4]
                ))
            return appointments
        except Exception as e:
            raise DatabaseConnectionException(f"Error fetching appointments for patient: {str(e)}")

    def get_appointments_for_doctor(self, doctorId: int) -> List[Appointment]:
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Appointment WHERE doctorId = ?"
            cursor.execute(query, (doctorId,))
            rows = cursor.fetchall()
            appointments = []
            for row in rows:
                appointments.append(Appointment(
                    appointmentId=row[0],
                    patientId=row[1],
                    doctorId=row[2],
                    appointmentDate=row[3],
                    description=row[4]
                ))
            return appointments
        except Exception as e:
            raise DatabaseConnectionException(f"Error fetching appointments for doctor: {str(e)}")

    def schedule_appointment(self, appointment: Appointment) -> bool:
        try:
            cursor = self.connection.cursor()
            query = """
            INSERT INTO Appointment (patientId, doctorId, appointmentDate, description)
            VALUES (?, ?, ?, ?)
            """
            cursor.execute(query, (appointment.get_patient_id(), appointment.get_doctor_id(), appointment.get_appointment_date(), appointment.get_description()))
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            raise DatabaseConnectionException(f"Error scheduling appointment: {str(e)}")

    def update_appointment(self, appointment: Appointment) -> bool:
        try:
            cursor = self.connection.cursor()
            query = """
            UPDATE Appointment
            SET patientId = ?, doctorId = ?, appointmentDate = ?, description = ?
            WHERE appointmentId = ?
            """
            cursor.execute(query, (appointment.get_patient_id(), appointment.get_doctor_id(), appointment.get_appointment_date(), appointment.get_description(), appointment.get_appointment_id()))
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            raise DatabaseConnectionException(f"Error updating appointment: {str(e)}")

    def cancel_appointment(self, appointmentId: int) -> bool:
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM Appointment WHERE appointmentId = ?"
            cursor.execute(query, (appointmentId,))
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            raise DatabaseConnectionException(f"Error canceling appointment: {str(e)}")
