#!/usr/bin/python3
from models.base_model import BaseModel
# from models.city import City
# from models.user import User
# from amenity import Amenity

class Place(BaseModel):
    
    def __init__(self):
        """
        Model For the Place where users stay at.
        """
        BaseModel.__init__(self)

        self.name = ""
        self.city_id = ""
        self.user_id = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = list()

