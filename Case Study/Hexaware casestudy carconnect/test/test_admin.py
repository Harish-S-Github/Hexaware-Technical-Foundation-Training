import unittest
import sys
import os

# ✅ Add root path for imports (points to the main project directory)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dao.adminservice import AdminService
from entity.admin import Admin

class TestAdminService(unittest.TestCase):

    def setUp(self):
       
        self.service = AdminService(test_mode=True)
        self.admin = Admin(
            admin_id=1,
            first_name="Alice",
            last_name="Smith",
            email="alice@example.com",
            phone_number="9876543210",
            username="admin01",
            password="adminpass",
            role="super admin",
            join_date="2024-01-01"
        )
        self.service.register_admin(self.admin)

    def test_register_admin(self):
        self.assertEqual(len(self.service.admins), 1)

    def test_authenticate_success(self):
        admin = self.service.get_admin_by_username("admin01")
        self.assertTrue(admin.authenticate("adminpass"))

    def test_authenticate_failure(self):
        admin = self.service.get_admin_by_username("admin01")
        self.assertFalse(admin.authenticate("wrongpass"))

    def test_get_admin_by_id(self):
        admin = self.service.get_admin_by_id(1)
        self.assertIsNotNone(admin)
        self.assertEqual(admin.get_first_name(), "Alice")

if __name__ == '__main__':
    unittest.main()
