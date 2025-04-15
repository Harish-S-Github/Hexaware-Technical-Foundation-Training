from util.db_conn_util import DBConnUtil
from entity.vehicle import Vehicle
from exception.vehicle_not_found_exception import VehicleNotFoundException

class VehicleService:
    def __init__(self, test_mode=False):
        self.test_mode = test_mode
        self.vehicles = [] if test_mode else None

    def add_vehicle(self, vehicle):
        if self.test_mode:
            self.vehicles.append(vehicle)
        else:
            try:
                conn = DBConnUtil.get_connection()
                cursor = conn.cursor()
                query = """
                    INSERT INTO Vehicle (
                        VehicleID, Model, Make, Year, Color,
                        RegistrationNumber, Availability, DailyRate
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """
                cursor.execute(query, (
                    vehicle.get_vehicle_id(),
                    vehicle.get_model(),
                    vehicle.get_make(),
                    vehicle.get_year(),
                    vehicle.get_color(),
                    vehicle.get_registration_number(),
                    vehicle.is_available(),
                    vehicle.get_daily_rate()
                ))
                conn.commit()
                conn.close()
            except Exception as e:
                raise Exception("Failed to add vehicle: " + str(e))

    def get_vehicle_by_id(self, vehicle_id):
        if self.test_mode:
            for v in self.vehicles:
                if v.get_vehicle_id() == vehicle_id:
                    return v
            raise VehicleNotFoundException("Vehicle not found")
        else:
            try:
                conn = DBConnUtil.get_connection()
                cursor = conn.cursor()
                query = "SELECT * FROM Vehicle WHERE VehicleID = ?"
                cursor.execute(query, (vehicle_id,))
                row = cursor.fetchone()
                conn.close()

                if row:
                    return Vehicle(
                        vehicle_id=row[0],
                        model=row[1],
                        make=row[2],
                        year=row[3],
                        color=row[4],
                        registration_number=row[5],
                        availability=row[6],
                        daily_rate=row[7]
                    )
                else:
                    raise VehicleNotFoundException("Vehicle not found")

            except Exception as e:
                raise Exception("Failed to retrieve vehicle: " + str(e))

    def get_available_vehicles(self):
        if self.test_mode:
            return [v for v in self.vehicles if v.is_available()]
        else:
            try:
                conn = DBConnUtil.get_connection()
                cursor = conn.cursor()
                query = "SELECT * FROM Vehicle WHERE Availability = 1"
                cursor.execute(query)
                rows = cursor.fetchall()
                conn.close()

                return [
                    Vehicle(
                        vehicle_id=row[0],
                        model=row[1],
                        make=row[2],
                        year=row[3],
                        color=row[4],
                        registration_number=row[5],
                        availability=row[6],
                        daily_rate=row[7]
                    )
                    for row in rows
                ]
            except Exception as e:
                raise Exception("Failed to get available vehicles: " + str(e))

    def update_vehicle(self, vehicle):
        if not self.test_mode:
            try:
                conn = DBConnUtil.get_connection()
                cursor = conn.cursor()
                query = """
                    UPDATE Vehicle
                    SET Model = ?, Make = ?, Year = ?, Color = ?,
                        RegistrationNumber = ?, Availability = ?, DailyRate = ?
                    WHERE VehicleID = ?
                """
                cursor.execute(query, (
                    vehicle.get_model(),
                    vehicle.get_make(),
                    vehicle.get_year(),
                    vehicle.get_color(),
                    vehicle.get_registration_number(),
                    vehicle.is_available(),
                    vehicle.get_daily_rate(),
                    vehicle.get_vehicle_id()
                ))
                conn.commit()
                conn.close()
            except Exception as e:
                raise Exception("Failed to update vehicle: " + str(e))

    def remove_vehicle(self, vehicle_id):
        if not self.test_mode:
            try:
                conn = DBConnUtil.get_connection()
                cursor = conn.cursor()
                query = "DELETE FROM Vehicle WHERE VehicleID = ?"
                cursor.execute(query, (vehicle_id,))
                conn.commit()
                conn.close()
            except Exception as e:
                raise Exception("Failed to remove vehicle: " + str(e))
