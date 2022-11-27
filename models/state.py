#!/usr/bin/python3
"""_summary_
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Contains name of the state as an attribute.

    Args:
        BaseModel (_type_): BaseModel that contains updated_at,
        created_at & uuid, where this class uses as a parent model
    """

    name = ''
