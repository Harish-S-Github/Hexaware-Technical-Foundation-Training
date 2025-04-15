from util.db_conn_util import DBConnUtil

class ReportGenerator:

    @staticmethod
    def generate_reservation_history():
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM Reservation ORDER BY StartDate DESC"
            cursor.execute(query)
            rows = cursor.fetchall()
            conn.close()

            print("\n--- Reservation History Report ---")
            for row in rows:
                print(f"ReservationID: {row[0]}, CustomerID: {row[1]}, VehicleID: {row[2]}, "
                      f"Start: {row[3]}, End: {row[4]}, TotalCost: ₹{row[5]}, Status: {row[6]}")
        except Exception as e:
            print("Error generating reservation history:", e)

    @staticmethod
    def generate_vehicle_utilization():
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            query = """
                SELECT VehicleID, COUNT(*) AS TotalReservations
                FROM Reservation
                GROUP BY VehicleID
                ORDER BY TotalReservations DESC
            """
            cursor.execute(query)
            rows = cursor.fetchall()
            conn.close()

            print("\n--- Vehicle Utilization Report ---")
            for row in rows:
                print(f"VehicleID: {row[0]}, Reservations: {row[1]}")
        except Exception as e:
            print("Error generating vehicle utilization report:", e)

    @staticmethod
    def generate_revenue_report():
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            query = """
                SELECT VehicleID, SUM(TotalCost) AS Revenue
                FROM Reservation
                GROUP BY VehicleID
                ORDER BY Revenue DESC
            """
            cursor.execute(query)
            rows = cursor.fetchall()
            conn.close()

            print("\n--- Revenue Report ---")
            for row in rows:
                print(f"VehicleID: {row[0]}, Revenue: ₹{row[1]:.2f}")
        except Exception as e:
            print("Error generating revenue report:", e)
