#!/usr/bin/python3
from models.base_model import BaseModel
from models.place import Place
from models.user import User

class Review(BaseModel):
    def __init__(self, text):
        """Initializing Review Attrs.

        Args:
            text (string): Review Content.
            place_id (Place): Primary key to a place
            user_id (User): Primary key to a user
        """
        self.text = text
        self.place_id = Place.id
        self.user_id = User.id
