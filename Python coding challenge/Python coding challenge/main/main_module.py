# mainmod/main_module.py
import sys
import os

# Adding the root directory to sys.path to resolve imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dao.hospital_service_impl import HospitalServiceImpl
from entity.appointment import Appointment
from exception.database_connection_exception import DatabaseConnectionException
from exception.patient_number_not_found_exception import PatientNumberNotFoundException
from exception.appointment_not_found_exception import AppointmentNotFoundException

def main():
    hospital_service = HospitalServiceImpl()

    while True:
        print("\nHospital Management System")
        print("1. Get Appointment by ID")
        print("2. Get Appointments for Patient")
        print("3. Get Appointments for Doctor")
        print("4. Schedule Appointment")
        print("5. Update Appointment")
        print("6. Cancel Appointment")
        print("7. Exit")

        choice = input("Please select an option (1-7): ")

        if choice == "1":
            try:
                appointmentId = int(input("Enter appointment ID: "))
                appointment = hospital_service.get_appointment_by_id(appointmentId)
                if appointment:
                    print(f"Appointment Found: ID: {appointment.appointmentId}, Patient ID: {appointment.patientId}, Doctor ID: {appointment.doctorId}, Date: {appointment.appointmentDate}, Description: {appointment.description}")
                else:
                    print(f"No appointment found with ID {appointmentId}")
            except AppointmentNotFoundException as e:
                print(f"Error: {e}")
            except DatabaseConnectionException as e:
                print(f"Database error: {e}")

        elif choice == "2":
            try:
                patientId = int(input("Enter patient ID: "))
                appointments = hospital_service.get_appointments_for_patient(patientId)
                if appointments:
                    for appointment in appointments:
                        print(f"Appointment ID: {appointment.appointmentId}, Doctor ID: {appointment.doctorId}, Date: {appointment.appointmentDate}, Description: {appointment.description}")
                else:
                    print(f"No appointments found for patient with ID {patientId}")
            except PatientNumberNotFoundException as e:
                print(f"Error: {e}")
            except DatabaseConnectionException as e:
                print(f"Database error: {e}")

        elif choice == "3":
            try:
                doctorId = int(input("Enter doctor ID: "))
                appointments = hospital_service.get_appointments_for_doctor(doctorId)
                if appointments:
                    for appointment in appointments:
                        print(f"Appointment ID: {appointment.appointmentId}, Patient ID: {appointment.patientId}, Date: {appointment.appointmentDate}, Description: {appointment.description}")
                else:
                    print(f"No appointments found for doctor with ID {doctorId}")
            except DatabaseConnectionException as e:
                print(f"Database error: {e}")

        elif choice == "4":
            try:
                patientId = int(input("Enter patient ID: "))
                doctorId = int(input("Enter doctor ID: "))
                appointmentDate = input("Enter appointment date (YYYY-MM-DD): ")
                description = input("Enter description: ")

                appointment = Appointment(patientId=patientId, doctorId=doctorId, appointmentDate=appointmentDate, description=description)
                result = hospital_service.schedule_appointment(appointment)

                if result:
                    print("Appointment scheduled successfully.")
                else:
                    print("Failed to schedule the appointment.")
            except DatabaseConnectionException as e:
                print(f"Database error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

        elif choice == "5":
            try:
                appointmentId = int(input("Enter appointment ID: "))
                patientId = int(input("Enter patient ID: "))
                doctorId = int(input("Enter doctor ID: "))
                appointmentDate = input("Enter appointment date (YYYY-MM-DD): ")
                description = input("Enter description: ")

                appointment = Appointment(appointmentId=appointmentId, patientId=patientId, doctorId=doctorId, appointmentDate=appointmentDate, description=description)
                result = hospital_service.update_appointment(appointment)

                if result:
                    print("Appointment updated successfully.")
                else:
                    print("Failed to update the appointment.")
            except DatabaseConnectionException as e:
                print(f"Database error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

        elif choice == "6":
            try:
                appointmentId = int(input("Enter appointment ID to cancel: "))
                result = hospital_service.cancel_appointment(appointmentId)
                if result:
                    print("Appointment canceled successfully.")
                else:
                    print("Failed to cancel the appointment.")
            except DatabaseConnectionException as e:
                print(f"Database error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

        elif choice == "7":
            print("Exiting the system...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
