#!/usr/bin/python3
from models.base_model import BaseModel

baseModel = BaseModel()
baseModel.name = "My First Model"
baseModel.my_number = 89
print(baseModel)
baseModel.save()
print(baseModel)
baseModelJSON = baseModel.to_dict()
print(baseModelJSON)
print("JSON of baseModel:")
for key in baseModelJSON.keys():
    print("\t{}: ({}) - {}".format(key, type(baseModelJSON[key]), baseModelJSON[key]))