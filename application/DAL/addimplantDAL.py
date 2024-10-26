import mysql.connector
from mysql.connector import errorcode

class AddImplantDAL:
    def __init__(self):
        try:
            self.admin_cnx = mysql.connector.connect(
                user='admin_user', password='admin1234',
                host='127.0.0.1', database='TRACKER'
            )
            self.cursor = self.admin_cnx.cursor(dictionary=True)
        except mysql.connector.Error as e:
            print(f"[!] Error: {e}")


    def add_implant(self, implant_name, implant_version, implant_type):
        try:
            args = (implant_name, implant_version, implant_type)
            self.cursor.callproc('AddImplant', args)
            self.admin_cnx.commit()
            return True
        except mysql.connector.Error as e:
            print(f"[!] Error: {e}")
            return False
        finally:
            self.cursor.close()  # Ensure the cursor is closed


    def get_all(self):
        """Retrieve all implants."""
        try:
            self.cursor.execute("SELECT * FROM IMPLANTTYPE")
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"[!] Error: {e}")
            return []


    def close(self):
        """Close the database connection."""
        if self.cursor:
            self.cursor.close()
        if self.admin_cnx.is_connected():
            self.admin_cnx.close()