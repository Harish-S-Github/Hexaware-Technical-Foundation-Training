# entity/patient.py

class Patient:
    def __init__(self, patientId=None, firstName=None, lastName=None, dateOfBirth=None, gender=None, contactNumber=None, address=None):
        self.__patientId = patientId
        self.__firstName = firstName
        self.__lastName = lastName
        self.__dateOfBirth = dateOfBirth
        self.__gender = gender
        self.__contactNumber = contactNumber
        self.__address = address

    # Default constructor
    def __str__(self):
        return f"Patient ID: {self.__patientId}, Name: {self.__firstName} {self.__lastName}, DOB: {self.__dateOfBirth}, Gender: {self.__gender}, Contact: {self.__contactNumber}, Address: {self.__address}"

    # Getters and Setters
    def get_patient_id(self):
        return self.__patientId

    def set_patient_id(self, patientId):
        self.__patientId = patientId

    def get_first_name(self):
        return self.__firstName

    def set_first_name(self, firstName):
        self.__firstName = firstName

    def get_last_name(self):
        return self.__lastName

    def set_last_name(self, lastName):
        self.__lastName = lastName

    def get_date_of_birth(self):
        return self.__dateOfBirth

    def set_date_of_birth(self, dateOfBirth):
        self.__dateOfBirth = dateOfBirth

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_contact_number(self):
        return self.__contactNumber

    def set_contact_number(self, contactNumber):
        self.__contactNumber = contactNumber

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    # Method to print all member variables and values
    def print_all_details(self):
        print(f"Patient ID: {self.__patientId}")
        print(f"First Name: {self.__firstName}")
        print(f"Last Name: {self.__lastName}")
        print(f"Date of Birth: {self.__dateOfBirth}")
        print(f"Gender: {self.__gender}")
        print(f"Contact Number: {self.__contactNumber}")
        print(f"Address: {self.__address}")
