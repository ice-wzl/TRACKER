import mysql.connector
from mysql.connector import errorcode

class AddCampaignDAL:
    def __init__(self):
        try:
            self.write_cnx = mysql.connector.connect(
                user='admin_user', password='admin1234',
                host='127.0.0.1', database='TRACKER'
            )
            self.cursor = self.write_cnx.cursor(dictionary=True)
        except mysql.connector.Error as e:
            print(f"[!] Error: {e}")


    def add_campaign(self, name):
        try:
            self.cursor.callproc('AddCampaign', (name,))
            self.write_cnx.commit()
            return True
        except mysql.connector.Error as e:
            print(f"[!] Error: {e}")
            return False
        finally:
            self.cursor.close()  # Ensure the cursor is closed


    def get_all(self):
        """Retrieve all campaigns."""
        try:
            self.cursor.execute("SELECT * FROM CAMPAIGN")
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"[!] Error: {e}")
            return []


    def close(self):
        """Close the database connection."""
        if self.cursor:
            self.cursor.close()
        if self.write_cnx.is_connected():
            self.write_cnx.close()