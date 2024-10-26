import sys
import os

# Add the application folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DAL.addimplantDAL import *

class AddImplant:
    def __init__(self):
        self.AddImplantDAL = AddImplantDAL()

    def add_implant(self, implant_name, implant_version, implant_type):
        """Add a new location."""
        return self.AddImplantDAL.add_implant(implant_name, implant_version, implant_type)

    def get_all(self):
        """Fetch all locations."""
        return self.AddImplantDAL.get_all()

    def close(self):
        """Close the DAL connection."""
        self.AddImplantDAL.close()

