#!/usr/bin/python3
from models.base_model import BaseModel
from models.state import State

class City(BaseModel):
    def __init__(self):
        """Initializing City Attr.
        """
        BaseModel.__init__(self)

        state = State()
        state.save()

        self.name = ""
        self.state_id = state.id