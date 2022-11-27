#!/usr/bin/python3
from models import storage
from models.city import City

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new City --")
city = City()
city.state_id = ""
city.name = "Washington"
city.save()
print(city)
