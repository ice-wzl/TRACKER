import mysql.connector
from mysql.connector import errorcode
    

class GetDeploymentDAL:
    def __init__(self):
        try:
            # Create separate connections for different user roles
            self.admin_cnx = mysql.connector.connect(
                user='admin_user', password='admin1234',
                host='127.0.0.1', database='TRACKER', port=3306
            )
        except mysql.connector.Error as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("[!] Error: Username or password is incorrect")
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print("[!] Error: Database does not exist")
            else:
                print(f"[!] Error:\n{e}")

    def get_deployment(self):
        """Fetch implant deployment details via stored procedure."""
        cursor = self.admin_cnx.cursor(dictionary=True)
        query = "CALL GetDeploymentDetails();"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()  # Close the cursor
        return results
