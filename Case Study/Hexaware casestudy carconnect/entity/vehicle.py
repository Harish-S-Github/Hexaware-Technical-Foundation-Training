class Vehicle:
    def __init__(self, vehicle_id=None, model="", make="", year=0, color="", registration_number="", availability=True, daily_rate=0.0):
        self.vehicle_id = vehicle_id
        self.model = model
        self.make = make
        self.year = year
        self.color = color
        self.registration_number = registration_number
        self.availability = availability
        self.daily_rate = daily_rate

    # Getters
    def get_vehicle_id(self):
        return self.vehicle_id

    def get_model(self):
        return self.model

    def get_make(self):
        return self.make

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_registration_number(self):
        return self.registration_number

    def get_availability(self):
        return self.availability

    def is_available(self):  # ✅ added for compatibility with DAO
        return self.availability

    def get_daily_rate(self):
        return self.daily_rate

    # Setters
    def set_vehicle_id(self, vehicle_id):
        self.vehicle_id = vehicle_id

    def set_model(self, model):
        self.model = model

    def set_make(self, make):
        self.make = make

    def set_year(self, year):
        self.year = year

    def set_color(self, color):
        self.color = color

    def set_registration_number(self, registration_number):
        self.registration_number = registration_number

    def set_availability(self, availability):
        self.availability = availability

    def set_daily_rate(self, daily_rate):
        self.daily_rate = daily_rate
