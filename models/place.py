#!/usr/bin/python3
from models.base_model import BaseModel
# from models.city import City
# from models.user import User
# from amenity import Amenity

class Place(BaseModel):
    
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = list()

