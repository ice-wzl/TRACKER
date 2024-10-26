import mysql.connector
from mysql.connector import errorcode

class AddDeploymentDAL:
    def __init__(self):
        try:
            self.admin_cnx = mysql.connector.connect(user='admin_user', password='admin1234',
                                host='127.0.0.1',
                                database='TRACKER')
        except mysql.connector.Error as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("[!] Error: Username or password is incorrect")
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print("[!] Error: Database does not exist, please create it first")
            else:
                print(f"[!] Error:\n{e}")

    def target_name_id(self, target_name):
        cursor = self.admin_cnx.cursor(dictionary=True)
        
        # Use a SELECT statement to call the function
        query = "SELECT GetTargetId(%s) AS target_id;"
        cursor.execute(query, (target_name,))
        
        # Fetch the result
        result = cursor.fetchone()
        cursor.close()  # Close the cursor
        
        # Return the target_id from the result, if it exists
        return result['target_id'] if result else None


    def add(self, install_date, kill_date, persistant, poc, ip_address, implant_port, target_id, campaign_id, location_id, implant_type_id):
        """Add a new implant deployment using the AddDeployment stored procedure."""

        try:
            self.cursor = self.admin_cnx.cursor(dictionary=True)
            args = (install_date, kill_date, persistant, poc, ip_address, implant_port, target_id, campaign_id, location_id, implant_type_id)
            self.cursor.callproc('AddDeployment', args)
            self.admin_cnx.commit()
            return f"Implant Deployment: {install_date} {kill_date} {persistant} {poc} {ip_address} {implant_port} {target_id} {campaign_id} {location_id} {implant_type_id} added successfully."
        except mysql.connector.Error as e:
            print(f"[!] Error: {e}")
            return None


    def get_deployment(self):
        """Fetch implant deployment details via stored procedure."""
        cursor = self.admin_cnx.cursor(dictionary=True)
        query = "CALL GetDeploymentDetails();"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()  # Close the cursor
        return results


    def close(self):
        """Close the database connection."""
        if self.cursor is not None:
            self.cursor.close()
        if self.admin_cnx is not None and self.admin_cnx.is_connected():
            self.admin_cnx.close()