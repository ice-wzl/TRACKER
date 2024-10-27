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
## How to use this application
### Add Location
- Start by adding a location that your Red Team will be operating in. Input the State and the Country.
![Screenshot from 2024-10-26 20-01-02](https://github.com/user-attachments/assets/05bdb090-5055-4ef2-b39e-8eb3502ecf5d)
### Add Campaign
- Then create a Campaign
![Screenshot from 2024-10-26 20-02-08](https://github.com/user-attachments/assets/22292c36-f978-414d-bbf7-983372bbfc6f)
### Add Targets
- After creating a campaign, you can now identify target hosts and add them as targets tying them to a campaign. This will keep your targets organized and all linked to your specific Red Team campaign.
- You can either name hosts in the target network numberically or by hostname, either is possible.
![Screenshot from 2024-10-26 20-07-17](https://github.com/user-attachments/assets/facf6f90-20df-4a70-82ae-78734618043b)
## Add Implants
- You can add implants that your Red Team is using and track their version
- You will need to have implants added before you create and implant deployment on a target.
- For example you can add `Sliver v5.4` and `Meterpreter 6.3`. This will assign the implant an implant ID which you can use in the `add_deployment` page.
## Add Deployment
- This page will allow you to track deployed implants in the Red Team engangement. You will need your Campaign ID, Target ID, and Implant ID. These can be gathered from the respective pages. You can further annotate any automatic kill-date along with the Red Team operator that installed the implant.
![Screenshot from 2024-10-26 20-12-20](https://github.com/user-attachments/assets/5b3c76ae-5d00-461d-82fd-eb90042cb23e)

## How to add notes 
- Simply place the notes file in the output directory and run `python3 -t TESTCAMPAIGN1 insert_target_notes.py`
- `-t TESTCAMPAIGN1` is the Target Name. It is the host the RedTeam attempted to gain access to and the notes should be stored for later use in the database.



## TO DO 
- add mac address and hostname to the add targets
- add ability to modify targets after creation, should be able to add data to blank data fields 
- add ability to search for notes on target id to not pull the whole campaign 
- add ability to modify any data after processing except notes!!! important notes are not allowed to be changed
