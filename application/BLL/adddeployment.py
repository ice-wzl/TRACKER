import sys
import os

# Add the application folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DAL.adddeploymentDAL import *

class AddDeployment:
    def __init__(self):
        self.AddDeploymentDAL = AddDeploymentDAL()

    
    def convert_name_id(self, target_name):
        return self.AddDeploymentDAL.target_name_id(target_name)
    

    def add(self, install_date, kill_date, persistant, poc, ip_address, implant_port, target_id, campaign_id, location_id, implant_type_id):
        """Set the instance variables and call DAL to add deployment."""
        self.install_date = install_date
        self.kill_date = kill_date
        self.persistant = persistant
        self.poc = poc
        self.ip_address = ip_address
        self.implant_port = implant_port
        self.target_id = target_id
        self.campaign_id = campaign_id
        self.location_id = location_id
        self.implant_type_id = implant_type_id

        # Call the DAL method to save to the database
        return self.AddDeploymentDAL.add(
            self.install_date, self.kill_date, self.persistant, self.poc, 
            self.ip_address, self.implant_port, self.target_id, self.campaign_id, self.location_id, self.implant_type_id
            )

    def get_deployment(self):
        """Fetch deployment details."""
        return self.AddDeploymentDAL.get_deployment()

    def close(self):
        """Close the database connection."""
        self.AddDeploymentDAL.close()

