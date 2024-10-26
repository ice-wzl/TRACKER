# TRACKKIT
![Screenshot from 2024-10-26 19-54-09](https://github.com/user-attachments/assets/cecf893c-0d62-4acd-91fa-4f6b3554b13d)
- This repo is designed for Red Teams to track their implant deployments across different engagements. It provies an ability to track locations, implant versions, target IDs, and campaign IDs. It further provies a way to centralize engagement notes allowing different Red Team operators to have access to all the notes across an engagement.

## Install
- This repo should work across Linux distributions, however it has only been tested and verified on Ubuntu 24.04
- I recommend using a virtual enviroment to avoid dependency conflicts.
````
sudo apt update
# install required dependencies 
sudo apt install -y pkg-config python3-dev libmysqlclient-dev build-essential
cd application/
python3 -m venv venv
source venv/bin/activate 
pip3 install -r requirements.txt
# fix Werkzeug deprecation issues
pip3 install --upgrade Flask Werkzeug
pip install --upgrade mysql-connector-python
````
## Example Systemd service file 
````
/etc/systemd/system/trackit.service
[Unit]
Description=trackkit
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/opt/trackkit/application
ExecStart=/opt/trackkit/application/venv/bin/python3 /opt/trackkit/application/app.py
Restart=always
Environment="PATH=/opt/trackkit/application/venv/bin"
Environment="VIRTUAL_ENV=/opt/trackkit/application/venv"


[Install]
WantedBy=multi-user.target
````
## Database Setup
- Install mysql database 
````
sudo apt install mysql-server
````
- Connect to your database `mysql -u root -p`
- Run the files in order listed below 
````
source users.sql
source ddl.sql
source function_procedures.sql
source permissions.sql
````
## Run the application 
- Once your database is set up you can `cd application/` and run the application with 
````
python3 app.py
````
## How to add notes 
- Simply place the notes file in the output directory and run `python3 -t TESTCAMPAIGN1 insert_target_notes.py`
- `-t TESTCAMPAIGN1` is the Target Name. It is the host the RedTeam attempted to gain access to and the notes should be stored for later use in the database.

## Errors 
````
AttributeError: 'AddLocationDAL' object has no attribute 'cursor'
[!] Error: Authentication plugin 'caching_sha2_password' is not supported
````
- Fix with connecting to your database and running 
````
USER TRACKER;
ALTER USER 'admin_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'admin1234';
FLUSH PRIVILEGES;
````

## TO DO 
- add mac address and hostname to the add targets
- add ability to modify targets after creation, should be able to add data to blank data fields 
- add ability to search for notes on target id to not pull the whole campaign 
- add ability to modify any data after processing except notes!!! important notes are not allowed to be changed
