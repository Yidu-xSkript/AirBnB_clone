#!/usr/bin/python3

class FileStorage():
    def __file_path():
        """
        string - path to the JSON file (ex: file.json)
        """        
        pass

    def __objects():
        """
        empty but will store all objects by <class name>.id 
        (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)
        """        
        pass

    def all(self):
        """
        returns the dictionary __objects
        """
        pass

    def new(self, obj):
        """ 
        sets in __objects the obj with key <obj class name>.id
        Args:
            obj (_type_): _description_
        """
        pass

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        pass

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; 
        otherwise, do nothing. If the file doesn't exist, no exception should be raised)
        """
        pass