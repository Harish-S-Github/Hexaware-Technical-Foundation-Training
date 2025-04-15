from util.db_conn_util import DBConnUtil
from entity.admin import Admin
from exception.authentication_exception import AuthenticationException

class AdminService:
    def __init__(self, test_mode=False):
        self.test_mode = test_mode
        self.admins = [] if test_mode else None

    def register_admin(self, admin):
        if self.test_mode:
            self.admins.append(admin)
        else:
            try:
                conn = DBConnUtil.get_connection()
                cursor = conn.cursor()
                query = """
                    INSERT INTO admins (
                        AdminID, FirstName, LastName, Email, PhoneNumber,
                        Username, Password, Role, JoinDate
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """
                cursor.execute(query, (
                    admin.get_admin_id(),
                    admin.get_first_name(),
                    admin.get_last_name(),
                    admin.get_email(),
                    admin.get_phone_number(),
                    admin.get_username(),
                    admin.get_password(),
                    admin.get_role(),
                    admin.get_join_date()
                ))
                conn.commit()
                conn.close()
            except Exception as e:
                raise Exception("Failed to register admin: " + str(e))

    def get_admin_by_username(self, username):
        if self.test_mode:
            for admin in self.admins:
                if admin.get_username() == username:
                    return admin
            raise AuthenticationException("Admin not found")
        else:
            try:
                conn = DBConnUtil.get_connection()
                cursor = conn.cursor()
                query = "SELECT * FROM admins WHERE Username = ?"
                cursor.execute(query, (username,))
                row = cursor.fetchone()
                conn.close()

                if row:
                    return Admin(
                        admin_id=row[0],
                        first_name=row[1],
                        last_name=row[2],
                        email=row[3],
                        phone_number=row[4],
                        username=row[5],
                        password=row[6],
                        role=row[7],
                        join_date=row[8]
                    )
                else:
                    raise AuthenticationException("Admin not found")

            except Exception as e:
                raise Exception("Failed to retrieve admin: " + str(e))

    def get_admin_by_id(self, admin_id):
        if self.test_mode:
            for admin in self.admins:
                if admin.get_admin_id() == admin_id:
                    return admin
            return None
        else:
            try:
                conn = DBConnUtil.get_connection()
                cursor = conn.cursor()
                query = "SELECT * FROM admins WHERE AdminID = ?"
                cursor.execute(query, (admin_id,))
                row = cursor.fetchone()
                conn.close()

                if row:
                    return Admin(
                        admin_id=row[0],
                        first_name=row[1],
                        last_name=row[2],
                        email=row[3],
                        phone_number=row[4],
                        username=row[5],
                        password=row[6],
                        role=row[7],
                        join_date=row[8]
                    )
                else:
                    return None

            except Exception as e:
                raise Exception("Failed to retrieve admin: " + str(e))
