#!/usr/bin/python3
from models.base_model import BaseModel

baseModel = BaseModel()
baseModel.name = "My First Model"
baseModel.my_number = 89
print(baseModel)
baseModel.save()
print(baseModel)
baseModelJSON = baseModel.todict()
print(baseModelJSON)
print("JSON of baseModel:")
for key in baseModelJSON.keys():
    print("\t{}: ({}) - {}".format(key, type(baseModelJSON[key]), baseModelJSON[key]))

# print("--")
# my_new_model = BaseModel(**baseModelJSON)
# print(my_new_model.id)
# print(my_new_model)
# print(type(my_new_model.created_at))

# print("--")
# print(baseModel is my_new_model)