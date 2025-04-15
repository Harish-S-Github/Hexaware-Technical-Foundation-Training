import unittest
import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dao.vehicleservice import VehicleService
from entity.vehicle import Vehicle

class TestVehicleService(unittest.TestCase):

    def setUp(self):
        self.service = VehicleService(test_mode=True)
        self.vehicle = Vehicle(
            vehicle_id=101,
            model="Civic",
            make="Honda",
            year=2022,
            color="Red",
            registration_number="TN10XX1234",
            availability=True,
            daily_rate=45.0
        )
        self.service.add_vehicle(self.vehicle)

    def test_add_vehicle(self):
        self.assertEqual(len(self.service.vehicles), 1)

    def test_get_vehicle_by_id(self):
        vehicle = self.service.get_vehicle_by_id(101)
        self.assertIsNotNone(vehicle)
        self.assertEqual(vehicle.get_model(), "Civic")

    def test_get_available_vehicles(self):
        available = self.service.get_available_vehicles()
        self.assertEqual(len(available), 1)
        self.assertTrue(available[0].get_availability())

    def test_update_vehicle(self):
        self.vehicle.set_color("Blue")
        self.vehicle.set_daily_rate(50.0)
        self.service.update_vehicle(self.vehicle)
        updated = self.service.get_vehicle_by_id(101)
        self.assertEqual(updated.get_color(), "Blue")
        self.assertEqual(updated.get_daily_rate(), 50.0)

    def test_remove_vehicle(self):
        self.service.remove_vehicle(101)
        self.assertEqual(len(self.service.vehicles), 0)

if __name__ == '__main__':
    unittest.main()
