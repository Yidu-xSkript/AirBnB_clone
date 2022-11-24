#!/usr/bin/python3
from models.base_model import BaseModel
# from models.place import Place
# from models.user import User

class Review(BaseModel):
    def __init__(self):
        """Initializing Review Attrs.
        """
        BaseModel.__init__(self)
        self.text = ""
        self.place_id = ""
        self.user_id = ""
