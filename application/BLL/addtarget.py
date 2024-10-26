import sys
import os

# Add the application folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DAL.addtargetDAL import *

class AddTarget:
    def __init__(self):
        self.AddTargetDAL = AddTargetDAL()

    def add_target(self, name, ip_address, campaign_id):
        """Add a new target."""
        return self.AddTargetDAL.add_target(name, ip_address, campaign_id)

    def get_all(self):
        """Fetch all targets."""
        return self.AddTargetDAL.get_all()
    
    def search_target(self, name):
        """Search for target/s"""
        return self.AddTargetDAL.search_target(name)

    def close(self):
        """Close the DAL connection."""
        self.AddTargetDAL.close()

