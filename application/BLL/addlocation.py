import sys
import os

# Add the application folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DAL.addlocationDAL import *

class AddLocation:
    def __init__(self):
        self.AddLocationDAL = AddLocationDAL()

    def add_location(self, state, country):
        """Add a new location."""
        return self.AddLocationDAL.add_location(state, country)

    def get_all(self):
        """Fetch all locations."""
        return self.AddLocationDAL.get_all()

    def close(self):
        """Close the DAL connection."""
        self.AddLocationDAL.close()

