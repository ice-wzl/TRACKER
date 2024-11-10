import argparse
import os
import sys
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime


def get_note(file_name):
    if os.path.exists(file_name):
        with open(file_name) as fp:
            file_contents = fp.read()
        return file_contents
    else:
        print(f"[!] Could not get file contents: {file_name}")
        sys.exit(1)

def insert_data(target_id, campaign_id, file_name):
   
    note = get_note(file_name)
    if not file_name:
        print(f"[!] {file_name} not found")
        return

    try:
        # Connect to the database
        cnx = mysql.connector.connect(
            user='admin_user', 
            password='admin1234',
            host='127.0.0.1', 
            database='TRACKER'
        )
        cursor = cnx.cursor()

        # SQL INSERT query
        query = """
        INSERT INTO TARGETNOTES (target_id, campaign_id, date_of_note, note) 
        VALUES (%s, %s, %s, %s)
        """
        
        # Use the current date for the date_of_note field
        current_date = datetime.now().date()
        
        # Execute the query
        cursor.execute(query, (target_id, campaign_id, current_date, note))

        # Commit the transaction
        cnx.commit()
        print("[+] Data inserted successfully")

    except mysql.connector.Error as e:
        print(f"[!] Error: {e}")

    finally:
        # Close the cursor and connection
        cursor.close()
        cnx.close()

# Example usage
if __name__ == "__main__":
        
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="The file to push to the database", required=True, dest="file_name")
    parser.add_argument("-e", "--target", help="The target id of the target", required=True, dest="target")
    parser.add_argument("-p", "--campaign", help="The campaign id of the target", required=True, dest="campaign")
    args = parser.parse_args()
    
    campaign = args.campaign
    target = args.target
    campaign = int(campaign)
    target = int(target)

    if args.file_name:
        insert_data(target_id=target, campaign_id=campaign, file_name=args.file_name)
