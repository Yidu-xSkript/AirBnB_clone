#!/usr/bin/python3
from models.base_model import BaseModel

class User(BaseModel):
    """
    Inherits from BaseModel & contains user attributes to be stored on the database or any storage engine.
    Containts - email, password, firstName and lastName.
    Args:
        BaseModel (_type_): BaseModel that contains updated_at, created_at & uuid, where this class uses as a parent model
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
        