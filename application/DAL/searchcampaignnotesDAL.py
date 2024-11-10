import mysql.connector
from mysql.connector import errorcode
import mysql.connector.errors

class SearchCampaignNotesDAL:
    def __init__(self):
        try:
            self.admin_cnx = mysql.connector.connect(
                user='admin_user', password='admin1234',
                host='127.0.0.1', database='TRACKER'
            )
            self.cursor = self.admin_cnx.cursor(dictionary=True)
        except mysql.connector.Error as e:
            print(f"[!] Error: {e}")


    def campaign_name_id(self, campaign_name):
        cursor = self.admin_cnx.cursor(dictionary=True)
        try:
            # Use a SELECT statement to call the function
            query = "SELECT GetCampaignId(%s) AS campaign_id;"
            cursor.execute(query, (campaign_name,))
            
            # Fetch the result
            result = cursor.fetchone()
        except mysql.connector.Error as e:
            print(f"[!] Error: {e}")
            result = None
        finally:
            cursor.close()
        return result['campaign_id'] if result else None


    def search_campaign(self, campaign_name):
        '''
        Take in the campaign_name from the html form and then we need to convert name to campaign id. After converting name 
        to campaign_id we can query the target notes table and then return all notes tied to a specific campaign_id.
        '''
        """Search for specific campaign returning target notes about targets in the campaign"""
        try:
            campaign_id = self.campaign_name_id(campaign_name)
            cursor = self.admin_cnx.cursor(dictionary=True)
            query = "SELECT * FROM TARGETNOTES WHERE campaign_id = %s"
            cursor.execute(query, (campaign_id,))
            results = cursor.fetchall()
            # print(f"Results: {results}")
        except mysql.connector.Error as e:
            print(f"[!] Error: {e}")
            results = []
        finally:
            cursor.close()
        return results
    
    def search_date(self, date):
        '''
        Take in the date from the html form and then query across campaigns by date
        '''
        try:
            cursor = self.admin_cnx.cursor(dictionary=True)
            query = "SELECT * FROM TARGETNOTES WHERE date_of_note = %s"
            cursor.execute(query, (date,))
            results = cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"[!] Error: {e}")
            results = []
        finally:
            cursor.close()
        return results


    def close(self):
        """Close the database connection."""
        if self.cursor:
            self.cursor.close()
        if self.admin_cnx.is_connected():
            self.admin_cnx.close()