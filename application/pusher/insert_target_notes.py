import argparse
import mysql.connector
import os
import sys

from mysql.connector import errorcode
from datetime import datetime


def establish_connection():
    try:
        admin_cnx = mysql.connector.connect(user='admin_user', password='admin1234',
                            host='192.168.15.129',
                            database='TRACKER')
        return admin_cnx
    except mysql.connector.Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("[!] Error: Username or password is incorrect")
        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            print("[!] Error: Database does not exist, please create it first")
        else:
            print(f"[!] Error:\n{e}")
        sys.exit(0)



def resolve_target_id(admin_cnx, target_name):
    try:
        cursor = admin_cnx.cursor()
        # Use a SELECT statement to call the function
        query = "SELECT GetTargetId(%s) AS target_id;"
        cursor.execute(query, (target_name,))
        
        # Fetch the result
        result = cursor.fetchone()
        cursor.close()  # Close the cursor
        
        # Return the target_id from the result, if it exists
        return result[0] if result else None 
    except mysql.connector.Error as e:
        print(f"[!] Error: {e}")
        


def resolve_campaign_id(admin_cnx, campaign_name):
    try:
        cursor = admin_cnx.cursor()
        query = "SELECT GetCampaignId(%s) AS id;"
        cursor.execute(query, (campaign_name,))
        
        result = cursor.fetchone()

        return result[0] if result else None
    except mysql.connector.Error as e:
        print(f"[!] Error: {e}")
        

def insert_data(admin_cnx, target_id, campaign_id, note):
    try:
        cursor = admin_cnx.cursor()

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
        admin_cnx.commit()
        print("[+] Data inserted successfully")

    except mysql.connector.Error as e:
        print(f"[!] Error: {e}")

    finally:
        # Close the cursor and connection
        cursor.close()
        admin_cnx.close()


def resolve_campaign_name(target_name):
    magic_index = 0
    split = list(target_name)
    for index, value in enumerate(reversed(split)):
        try:
            convert = int(value)
        except ValueError as e:
            magic_index = index
            break
    return magic_index                



def get_output():
    file_list = os.listdir("output")
    return file_list

# Example usage
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--targetname", help="The name of the target i.e. TESTTARGET1", dest="target_name", required=True)

    args = parser.parse_args()
    
    connection = establish_connection()

    campaign_name_index = resolve_campaign_name(args.target_name)
    campaign_name = args.target_name[0:-1* campaign_name_index]

    print(f"Resolving campaign ID for: {campaign_name}")
    campaign_id = resolve_campaign_id(connection, campaign_name)
    print(campaign_id)

    print(f"Resolving target ID for target: {args.target_name}")
    target_id = resolve_target_id(connection, args.target_name)
    print(target_id)

    print("[+] Pushing files")
    files = get_output()
    for file in files:
        with open("output/"+file, "r") as fp:
            data = fp.read()
        insert_data(connection, target_id, campaign_id, data)

