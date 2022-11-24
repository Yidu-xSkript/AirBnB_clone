#!/usr/bin/python3
import datetime
import uuid
from models import storage

class BaseModel():
    def __init__(self, *args, **kwargs):
        """_summary_
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        if len(kwargs) > 0:
            self.__dict__.update(kwargs)
           
            if '__class__' in self.__dict__:
                self.__dict__.pop('__class__')
           
            if type(self.__dict__['created_at']) == str:
                self.__dict__['created_at'] = datetime.datetime.strptime(self.__dict__['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            if type(self.__dict__['updated_at']) == str:
                self.__dict__['updated_at'] = datetime.datetime.strptime(self.__dict__['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
            
        storage.new(self)

    def __str__(self) -> str:
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the database / storage.
        - update the updated_at attribute.
        - save data to JSON file.
        """
        storage.save()

    def to_dict(self) -> dict:
        """Modify Dictionary and return the modified dictionary

        Returns:
            dict: self.__dict__
        """
        self.__dict__['__class__'] = self.__class__.__name__

        if type(self.__dict__['created_at']) != str:
            self.__dict__['created_at'] = self.__dict__['created_at'].strftime("%Y-%m-%dT%H:%M:%S.%f")

        if type(self.__dict__['updated_at']) != str:
            self.__dict__['updated_at'] = self.__dict__['updated_at'].strftime("%Y-%m-%dT%H:%M:%S.%f")  

        return self.__dict__