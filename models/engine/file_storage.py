#!/usr/bin/python3
import json
from pathlib import Path

class FileStorage():
    def __file_path(self) -> str:
        """
        string - path to the JSON file (ex: file.json)
        """        
        return "file.json"

    def __objects(self) -> dict:
        """
        empty but will store all objects by <class name>.id 
        (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)
        """        
        return self.__dict__

    def all(self) -> dict:
        """
        returns the dictionary __objects
        """
        return self.__objects()

    def new(self, obj):
        """ 
        sets in __objects the obj with key <obj class name>.id
        Args:
            obj (_type_): _description_
        """
        self.__dict__[obj.__class__.__name__ + '.' + obj.__dict__['id']] = obj.to_dict()

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path(), 'w') as fp:
            json.dump(self.__objects(), fp)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; 
        otherwise, do nothing. If the file doesn't exist, no exception should be raised)
        """
        file = Path(self.__file_path())
        if file.is_file():
            with open(self.__file_path(), "r") as fp:
                self.__dict__ = json.load(fp)