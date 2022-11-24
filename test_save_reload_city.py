#!/usr/bin/python3
from models import storage
from models.city import City

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Get State Id --")
dataKey = list(all_objs.keys())
state = dict()

for i in range(len(dataKey)): 
    if "State" == dataKey[i].split(".")[0]:
        state.update({'id': list(all_objs.values())[i]['id']})

print(state['id'])

print("-- Create a new City --")
city = City()
city.state_id = state['id']
city.name = "Washington"
city.save()
print(city)
