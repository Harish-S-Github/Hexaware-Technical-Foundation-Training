class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone_number, address, username, password, registration_date):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.username = username
        self.password = password
        self.registration_date = registration_date

    def get_customer_id(self):
        return self.customer_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def get_phone_number(self):
        return self.phone_number

    def get_address(self):
        return self.address

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_registration_date(self):
        return self.registration_date

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_email(self, email):
        self.email = email

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_address(self, address):
        self.address = address

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def set_registration_date(self, registration_date):
        self.registration_date = registration_date

    def authenticate(self, password):
        return self.password == password
