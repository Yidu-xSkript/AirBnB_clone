#!/usr/bin/python3
from models.base_model import BaseModel

class State(BaseModel):
    """Contains name of the state as an attribute.

    Args:
        BaseModel (_type_): BaseModel that contains updated_at, created_at & uuid, where this class uses as a parent model
    """

    def __init__(self, name):
        """Initializing State Attr.

        Args:
            name (string): Name of the state.
        """
        self.name = name