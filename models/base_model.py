#!/usr/bin/python3
"""BaseModel Class for AirBnb project"""
import uuid
from datetime import datetime
import models

storage = FileStorage()


class BaseModel:
    """creating the base class for the project"""

    def __init__(self, *args, **kwargs):
        """initializing class with attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key, datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f'))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """str function"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """save function"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """to_dict function"""
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result
