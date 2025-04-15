from util.db_conn_util import DBConnUtil
from entity.customer import Customer
from exception.authentication_exception import AuthenticationException

class CustomerService:
    def __init__(self, test_mode=False):
        self.test_mode = test_mode
        self.customers = [] if test_mode else None

    def register_customer(self, customer):
        if self.test_mode:
            self.customers.append(customer)
        else:
            try:
                conn = DBConnUtil.get_connection()
                cursor = conn.cursor()
                query = """
                    INSERT INTO Customer (
                        CustomerID, FirstName, LastName, Email, PhoneNumber,
                        Address, Username, Password, RegistrationDate
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """
                cursor.execute(query, (
                    customer.get_customer_id(),
                    customer.get_first_name(),
                    customer.get_last_name(),
                    customer.get_email(),
                    customer.get_phone_number(),
                    customer.get_address(),
                    customer.get_username(),
                    customer.get_password(),
                    customer.get_registration_date()
                ))
                conn.commit()
                conn.close()
            except Exception as e:
                raise Exception("Failed to register customer: " + str(e))

    def get_customer_by_username(self, username):
        if self.test_mode:
            for customer in self.customers:
                if customer.get_username() == username:
                    return customer
            raise AuthenticationException("Customer not found")
        else:
            try:
                conn = DBConnUtil.get_connection()
                cursor = conn.cursor()
                query = "SELECT * FROM Customer WHERE Username = ?"
                cursor.execute(query, (username,))
                row = cursor.fetchone()
                conn.close()

                if row:
                    return Customer(
                        customer_id=row[0],
                        first_name=row[1],
                        last_name=row[2],
                        email=row[3],
                        phone_number=row[4],
                        address=row[5],
                        username=row[6],
                        password=row[7],
                        registration_date=row[8]
                    )
                else:
                    raise AuthenticationException("Customer not found")

            except Exception as e:
                raise Exception("Failed to retrieve customer: " + str(e))

    def get_customer_by_id(self, customer_id):
        if self.test_mode:
            for customer in self.customers:
                if customer.get_customer_id() == customer_id:
                    return customer
            return None
        else:
            try:
                conn = DBConnUtil.get_connection()
                cursor = conn.cursor()
                query = "SELECT * FROM Customer WHERE CustomerID = ?"
                cursor.execute(query, (customer_id,))
                row = cursor.fetchone()
                conn.close()

                if row:
                    return Customer(
                        customer_id=row[0],
                        first_name=row[1],
                        last_name=row[2],
                        email=row[3],
                        phone_number=row[4],
                        address=row[5],
                        username=row[6],
                        password=row[7],
                        registration_date=row[8]
                    )
                else:
                    return None

            except Exception as e:
                raise Exception("Failed to retrieve customer: " + str(e))
