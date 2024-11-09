import mysql.connector
from mysql.connector import errorcode

class AddTargetDAL:
    def __init__(self):
        try:
            self.admin_cnx = mysql.connector.connect(
                user='admin_user', password='admin1234',
                host='127.0.0.1', database='TRACKER'
            )
            self.cursor = self.admin_cnx.cursor(dictionary=True)
        except mysql.connector.Error as e:
            print(f"[!] Error: {e}")


    def add_target(self, name, ip_address, mac_address, campaign_id):
        try:
            args = (name, ip_address, mac_address, campaign_id)
            self.cursor.callproc('AddTarget', args)
            self.admin_cnx.commit()
            return True
        except mysql.connector.Error as e:
            print(f"[!] Error: {e}")
            return False
        finally:
            self.cursor.close()  # Ensure the cursor is closed
 

    def get_all(self):
        try:
            cursor = self.admin_cnx.cursor(dictionary=True)
            query = "CALL GetTargetNormalized();"
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            return results
        except mysql.connector.Error as e:
            print(f"[!] Error addtargetDAL.py: {e}")
        

    def search_target(self, name):
        """Search for specific target"""
        try:
            query = "SELECT * FROM TARGET WHERE name LIKE %s"
            search_value = f"%{name}%"  # Add wildcards for partial matching
            self.cursor.execute(query, (search_value,))
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