#!/usr/bin/python3
import json
from pathlib import Path
import datetime

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
            obj (class): self
        """
        self.__dict__[obj.__class__.__name__ + '.' + obj.__dict__['id']] = obj.__dict__

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        for o in self.__objects().values():
            o['updated_at'] = datetime.datetime.now()
            if type(o['created_at']) != str:
                o['created_at'] = o['created_at'].strftime("%Y-%m-%dT%H:%M:%S.%f")
            if type(o['updated_at']) != str:
                o['updated_at'] = o['updated_at'].strftime("%Y-%m-%dT%H:%M:%S.%f")

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
                self.__dict__.update(json.load(fp))

        for o in self.__objects().values():
            if type(o['created_at']) == str:
                o['created_at'] = datetime.datetime.strptime(o['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            if type(o['updated_at']) == str:
                o['updated_at'] = datetime.datetime.strptime(o['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")