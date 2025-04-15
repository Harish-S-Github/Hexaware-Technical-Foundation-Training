import pyodbc
from exception.database_connection_exception import DatabaseConnectionException

db_config = {
    'server': r'Hariishs\SQLEXPRESS',
    'database': 'car',
    'driver': '{SQL Server}',
    'trusted_connection': 'yes'
}

class DBConnUtil:
    @staticmethod
    def get_connection():
        try:
            conn_str = (
                f"DRIVER={db_config['driver']};"
                f"SERVER={db_config['server']};"
                f"DATABASE={db_config['database']};"
                f"Trusted_Connection={db_config['trusted_connection']}"
            )
            return pyodbc.connect(conn_str)
        except Exception as e:
            raise DatabaseConnectionException(str(e))

