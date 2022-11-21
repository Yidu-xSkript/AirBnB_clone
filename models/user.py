#!/usr/bin/python3
from base_model import BaseModel

class User(BaseModel):
    """
    Inherits from BaseModel & contains user attributes to be stored on the database or any storage engine.
    Containts - email, password, firstName and lastName.
    Args:
        BaseModel (_type_): BaseModel that contains updated_at, created_at & uuid, where this class uses as a parent model
    """

    def __init__(self, email, password, first_name, last_name):
        """Initializing User Attr.

        Args:
            email (string): email of the user
            password (string): password
            first_name (string): firstname of the user
            last_name (string): lastname of the user
        """
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name