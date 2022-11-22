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
        print(f"[{self.__class__.__name__}]({self.id})<{self.__dict__}>")

    def save(self):
        self.updated_at = datetime.datetime.now()
        # storage.save()

    # Change created_at and updated_at to string from datetime datatype when adding to dict
    def to_dict(self):
        return self.__dict__