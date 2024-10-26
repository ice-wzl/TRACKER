import sys
import os

# Add the application folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from DAL.addcampaignDAL import *

class AddCampaign:
    def __init__(self):
        self.AddCampaignDAL = AddCampaignDAL()

    def add_campaign(self, name):
        """Add a new campaign."""
        return self.AddCampaignDAL.add_campaign(name)

    def get_all(self):
        """Fetch all campaigns."""
        return self.AddCampaignDAL.get_all()

    def close(self):
        """Close the DAL connection."""
        self.AddCampaignDAL.close()

