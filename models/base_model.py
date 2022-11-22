#!/usr/bin/python3
import datetime
import uuid
# from models import storage

class BaseModel():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        # If it's a new instance (not from a dictionary representation), add a call to the method "new(self)" on "storage".
        # storage.new()

    def __str__(self) -> str:
        return "[{}](%d)<{}>".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()
        # storage.save()

    def to_dict(self) -> dict:
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['created_at'] = self.__dict__['created_at'].strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.__dict__['updated_at'] = self.__dict__['updated_at'].strftime("%Y-%m-%dT%H:%M:%S.%f")
        return self.__dict__