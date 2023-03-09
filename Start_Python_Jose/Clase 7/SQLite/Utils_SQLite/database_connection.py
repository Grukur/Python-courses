import sqlite3


class DatabaseConnection:

    def __init__(self, host):
        self.connection = None
        self.host = host
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.host)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not (exc_tb or exc_val or exc_type):
            self.connection.commit()
        self.connection.close()

