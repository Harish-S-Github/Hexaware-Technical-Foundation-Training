import unittest
import sys
import os
from datetime import datetime

# Add root directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dao.reservationservice import ReservationService
from entity.reservation import Reservation

class TestReservationService(unittest.TestCase):

    def setUp(self):
        self.service = ReservationService(test_mode=True)
        self.reservation = Reservation(
            reservation_id=201,
            customer_id=1,
            vehicle_id=101,
            start_date="2024-04-10",
            end_date="2024-04-12",
            total_cost=0.0,
            status="pending"
        )
        self.reservation.calculate_total_cost(daily_rate=50.0)
        self.service.create_reservation(self.reservation)

    def test_create_reservation(self):
        self.assertEqual(len(self.service.reservations), 1)

    def test_get_reservation_by_id(self):
        r = self.service.get_reservation_by_id(201)
        self.assertIsNotNone(r)
        self.assertEqual(r.get_customer_id(), 1)

    def test_get_reservations_by_customer_id(self):
        results = self.service.get_reservations_by_customer_id(1)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].get_vehicle_id(), 101)

    def test_update_reservation(self):
        self.reservation.set_status("confirmed")
        self.reservation.set_end_date("2024-04-13")
        self.reservation.calculate_total_cost(daily_rate=50.0)
        self.service.update_reservation(self.reservation)

        updated = self.service.get_reservation_by_id(201)
        self.assertEqual(updated.get_status(), "confirmed")
        self.assertEqual(updated.get_end_date(), "2024-04-13")

    def test_cancel_reservation(self):
        self.service.cancel_reservation(201)
        self.assertEqual(len(self.service.reservations), 0)

if __name__ == '__main__':
    unittest.main()
