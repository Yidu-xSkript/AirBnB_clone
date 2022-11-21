#!/usr/bin/python3
from base_model import BaseModel
from city import City
from user import User
# from amenity import Amenity

class Place(BaseModel):
    
    def __init__(self, name, description, number_rooms = 0, nummber_bathrooms = 0, max_guest = 0, price_by_night = 0, latitude = 0.0, longitude = 0.0, amenity_ids = []):
        """
        Model For the Place where users stay at.

        Args:
            name (string): empty string
            city_id (City)
            user_id (User)
            description (string): empty string
            number_rooms (integer)
            nummber_bathrooms (integer)
            max_guest (integer)
            price_by_night (integer)
            latitude (float)
            longitude (float)
            amenity_ids (list[Amenity]): Convert this to Amenity Type later.
        """
        self.name = name
        self.city_id = City.id
        self.user_id = User.id
        self.description = description
        self.number_rooms = number_rooms
        self.number_bathrooms = nummber_bathrooms
        self.max_guest = max_guest
        self.price_by_night = price_by_night
        self.latitude = latitude
        self.longitude = longitude
        self.amenity_ids = amenity_ids

