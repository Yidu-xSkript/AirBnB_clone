#!/usr/bin/python3
"""_summary_
"""
from models.base_model import BaseModel
# from models.place import Place
# from models.user import User


class Review(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """
    text = ""
    place_id = ""
    user_id = ""
