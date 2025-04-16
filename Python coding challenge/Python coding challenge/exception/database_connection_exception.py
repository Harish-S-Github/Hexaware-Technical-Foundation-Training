# exception/database_connection_exception.py

class DatabaseConnectionException(Exception):
    """Custom exception for database connection errors."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
