import unittest
import sys
import os

# Ensure project root is on path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dao.customerservice import CustomerService
from entity.customer import Customer

class TestCustomerService(unittest.TestCase):

    def setUp(self):
        self.service = CustomerService(test_mode=True)
        self.customer = Customer(
            customer_id=1,
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            phone_number="9876543210",
            address="123 Street",
            username="john_doe",
            password="pass123",
            registration_date="2024-01-01"
        )
        self.service.register_customer(self.customer)

    def test_register_customer(self):
        self.assertEqual(len(self.service.customers), 1)

    def test_authenticate_success(self):
        customer = self.service.get_customer_by_username("john_doe")
        self.assertTrue(customer.authenticate("pass123"))

    def test_authenticate_failure(self):
        customer = self.service.get_customer_by_username("john_doe")
        self.assertFalse(customer.authenticate("wrongpass"))

    def test_get_customer_by_id(self):
        customer = self.service.get_customer_by_id(1)
        self.assertIsNotNone(customer)
        self.assertEqual(customer.get_first_name(), "John")

if __name__ == '__main__':
    unittest.main()
