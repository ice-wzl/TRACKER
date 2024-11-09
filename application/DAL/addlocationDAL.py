import mysql.connector
from mysql.connector import errorcode


class AddLocationDAL:
    def __init__(self):
        self.admin_cnx = None
        try:
            self.admin_cnx = mysql.connector.connect(
                user='admin_user', password='admin1234',
                host='127.0.0.1', database='TRACKER'
            )
            self.cursor = self.admin_cnx.cursor(dictionary=True)
        except mysql.connector.Error as e:
            print(f"[!] Error: {e}")
            self.cursor = None  


    def add_location(self, state, country):
        """Add a new location using a stored procedure."""
        if not self.cursor:
            print("[!] Error: Database connection not established.")
            return False
        try:
            args = (state, country)
            self.cursor.callproc('AddLocation', args)
            self.admin_cnx.commit()
            return True
        except mysql.connector.Error as e:
            print(f"[!] Error: {e}")
            return False


    def get_all(self):
        """Retrieve all locations."""
        try:
            self.cursor.execute("SELECT * FROM LOCATION")
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"[!] Error: {e}")
            return []


    def close(self):
        """Close the database connection."""
        if hasattr(self, 'cursor') and self.cursor:
            self.cursor.close()
        if self.admin_cnx and self.admin_cnx.is_connected():  
            self.admin_cnx.close()