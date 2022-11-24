#!/usr/bin/python3
from models.base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self):
        """Initializing Ammenity Attr.

        Args:
            name (string): name of the amnenity.
        """
        BaseModel.__init__(self)
        self.name = ""
