#!/usr/bin/python3
from models.base_model import BaseModel

class City(BaseModel):
    def __init__(self):
        """Initializing City Attr.
        """
        BaseModel.__init__(self)
        self.name = ""
        self.state_id = ""