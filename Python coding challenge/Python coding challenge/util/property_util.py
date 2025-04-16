# util/property_util.py

import configparser
import os

class PropertyUtil:
    @staticmethod
    def get_property_string(property_file):
        """Reads database connection properties from a property file and returns connection string."""
        config = configparser.ConfigParser()

        if not os.path.exists(property_file):
            raise FileNotFoundError(f"Property file {property_file} not found.")
        
        # Read the property file
        config.read(property_file)

        try:
            # Extract database connection details
            server = config.get('database', 'db.server')
            database = config.get('database', 'db.database')
            trusted_connection = config.get('database', 'db.trusted_connection')

            # Build and return the connection string in the required format
            connection_string = (
                f"DRIVER={{SQL Server}};"
                f"SERVER={server};"
                f"DATABASE={database};"
                f"Trusted_Connection={trusted_connection};"
            )
            return connection_string
        except KeyError as e:
            raise KeyError(f"Missing configuration key: {e}")
