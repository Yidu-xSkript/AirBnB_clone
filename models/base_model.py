#!/usr/bin/python3
"""_summary_
"""
from datetime import datetime
import uuid
import models


class BaseModel():
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        dateToStr = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs) > 0:
            self.__dict__.update(kwargs)
            for k, v in kwargs.items():
                if (k == "created_at" and type(k) == str
                        or k == "updated_at" and type(k) == str):
                    self.__dict__[k] = datetime.strptime(v, dateToStr)
        else:
            models.storage.new(self)

    def __str__(self) -> str:
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)

    def save(self):
        """Update the database / storage.
        - update the updated_at attribute.
        - save data to JSON file.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self) -> dict:
        """Modify Dictionary and return the modified dictionary

        Returns:
            dict: self.__dict__
        """
        _dict = self.__dict__.copy()
        _dict["created_at"] = self.created_at.isoformat()
        _dict["updated_at"] = self.updated_at.isoformat()
        _dict["__class__"] = self.__class__.__name__
        return _dict
