#!/usr/bin/python3
import json
from models.base_model import BaseModel
"""creating filestorage class and dict to json"""


class FileStorage:
    """creating FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """function returns all"""
        return self.__objects

    def new(self, obj):
        """sets the obj with key such as <obj class name>.id"""
        dict_key = "{}.{}".format(type(obj).__class__.__name__, obj.id)
        self.__objects[dict_key] = obj

    def save(self):
        """serializes objs to JSON file"""
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """deserializes JSON file to objs"""
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
