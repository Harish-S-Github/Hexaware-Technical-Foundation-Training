from util.db_conn_util import DBConnUtil
from entity.reservation import Reservation
from exception.reservation_exception import ReservationException

class ReservationService:
    def __init__(self, test_mode=False):
        self.test_mode = test_mode
        self.reservations = [] if test_mode else None

    def create_reservation(self, reservation):
        if self.test_mode:
            self.reservations.append(reservation)
        else:
            try:
                conn = DBConnUtil.get_connection()
                cursor = conn.cursor()
                query = """
                    INSERT INTO Reservation (
                        ReservationID, CustomerID, VehicleID, StartDate,
                        EndDate, TotalCost, Status
                    ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """
                cursor.execute(query, (
                    reservation.get_reservation_id(),
                    reservation.get_customer_id(),
                    reservation.get_vehicle_id(),
                    reservation.get_start_date(),
                    reservation.get_end_date(),
                    reservation.get_total_cost(),
                    reservation.get_status()
                ))
                conn.commit()
                conn.close()
            except Exception as e:
                raise Exception("Failed to create reservation: " + str(e))

    def get_reservation_by_id(self, reservation_id):
        if self.test_mode:
            for r in self.reservations:
                if r.get_reservation_id() == reservation_id:
                    return r
            raise ReservationException("Reservation not found")
        else:
            try:
                conn = DBConnUtil.get_connection()
                cursor = conn.cursor()
                query = "SELECT * FROM Reservation WHERE ReservationID = ?"
                cursor.execute(query, (reservation_id,))
                row = cursor.fetchone()
                conn.close()

                if row:
                    return Reservation(
                        reservation_id=row[0],
                        customer_id=row[1],
                        vehicle_id=row[2],
                        start_date=row[3],
                        end_date=row[4],
                        total_cost=row[5],
                        status=row[6]
                    )
                else:
                    raise ReservationException("Reservation not found")

            except Exception as e:
                raise Exception("Failed to retrieve reservation: " + str(e))

    def get_reservations_by_customer_id(self, customer_id):
        if self.test_mode:
            return [r for r in self.reservations if r.get_customer_id() == customer_id]
        else:
            try:
                conn = DBConnUtil.get_connection()
                cursor = conn.cursor()
                query = "SELECT * FROM Reservation WHERE CustomerID = ?"
                cursor.execute(query, (customer_id,))
                rows = cursor.fetchall()
                conn.close()

                return [
                    Reservation(
                        reservation_id=row[0],
                        customer_id=row[1],
                        vehicle_id=row[2],
                        start_date=row[3],
                        end_date=row[4],
                        total_cost=row[5],
                        status=row[6]
                    )
                    for row in rows
                ]

            except Exception as e:
                raise Exception("Failed to get reservations: " + str(e))

    def update_reservation(self, reservation):
        if not self.test_mode:
            try:
                conn = DBConnUtil.get_connection()
                cursor = conn.cursor()
                query = """
                    UPDATE Reservation
                    SET StartDate = ?, EndDate = ?, TotalCost = ?, Status = ?
                    WHERE ReservationID = ?
                """
                cursor.execute(query, (
                    reservation.get_start_date(),
                    reservation.get_end_date(),
                    reservation.get_total_cost(),
                    reservation.get_status(),
                    reservation.get_reservation_id()
                ))
                conn.commit()
                conn.close()
            except Exception as e:
                raise Exception("Failed to update reservation: " + str(e))

    def cancel_reservation(self, reservation_id):
        if not self.test_mode:
            try:
                conn = DBConnUtil.get_connection()
                cursor = conn.cursor()
                query = "DELETE FROM Reservation WHERE ReservationID = ?"
                cursor.execute(query, (reservation_id,))
                conn.commit()
                conn.close()
            except Exception as e:
                raise Exception("Failed to cancel reservation: " + str(e))
