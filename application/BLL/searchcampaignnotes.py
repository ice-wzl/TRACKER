"""
File should be the foundation of the search by project functionality that will then call the DAL layer to query for project notes
"""
import sys
import os

# Add the application folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DAL.searchcampaignnotesDAL import *

class SearchCampaignNotes:
    def __init__(self):
        self.SearchCampaignNotesDAL = SearchCampaignNotesDAL()
    
    def search_campaign(self, campaign_name):
        """Search camapaign for target notes"""
        return self.SearchCampaignNotesDAL.search_campaign(campaign_name)
    
    def search_date(self, date):
        """Search notes by date of operation"""
        return self.SearchCampaignNotesDAL.search_date(date)

    def close(self):
        """Close the DAL connection."""
        self.SearchCampaignNotes.close()