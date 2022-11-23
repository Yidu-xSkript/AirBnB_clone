#!/usr/bin/python3
from models.base_model import BaseModel
from models.state import State

class City(BaseModel):
    def __init__(self, name):
        """Initializing City Attr.

        Args:
            name (string): name of the city
            state_id (State): The primary key of state
        """
        self.name = name
        self.state_id = State.id