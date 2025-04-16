# util/db_conn_util.py

import pyodbc
from exception.database_connection_exception import DatabaseConnectionException
from util.property_util import PropertyUtil

class DBConnUtil:
    @staticmethod
    def get_connection(property_file='db_config.properties'):
        """Get the connection object using the connection string obtained from PropertyUtil."""
        try:
            # Get the connection string from the PropertyUtil class
            conn_str = PropertyUtil.get_property_string(property_file)
            # Return the connection object using pyodbc
            return pyodbc.connect(conn_str)
        except Exception as e:
            raise DatabaseConnectionException(f"Error connecting to DB: {str(e)}")
