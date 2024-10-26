#from DAL.studentDAL import StudentDAL
import sys
import os

# Add the application folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DAL.getdeploymentDAL import *

class GetDeployment:
    def __init__(self, install_date, kill_date, poc, location, country, implant_name, implant_version):
        self.GetDeploymentDAL = GetDeploymentDAL()
        self.install_date = install_date
        self.kill_date = kill_date
        self.poc = poc
        self.location = location
        self.country = country
        self.implant_name = implant_name
        self.implant_version = implant_version

    def get_all(self):
        """Fetch all deployment details from the database."""
        return self.GetDeploymentDAL.get_deployment()
    