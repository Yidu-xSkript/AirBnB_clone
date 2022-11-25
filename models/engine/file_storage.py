#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State

class FileStorage():
    __file_path =  "file.json"
    __objects = {}

    def all(self) -> dict:
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """ 
        sets in __objects the obj with key <obj class name>.id
        Args:
            obj (class): self
        """
        self.__objects[obj.__class__.__name__ + '.' + obj.__dict__['id']] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        to_JSON = {obj: self.__objects[obj].to_dict() for obj in self.__objects.keys()}
        with open(self.__file_path, 'w') as fp:
            json.dump(to_JSON, fp)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; 
        otherwise, do nothing. If the file doesn't exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, "r") as fp:
                _dict = json.load(fp)
                for o in _dict.values():
                    className = o["__class__"]
                    del o["__class__"]
                    self.new(eval(className)(**o))
        except FileNotFoundError:
            return
