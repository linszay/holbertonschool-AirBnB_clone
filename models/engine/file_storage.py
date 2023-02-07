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
        objects = {for key in self.__objects: objects[key] = self.__objects[key].to_dict()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(objects, f)

    def reload(self):
        """deserializes JSON file to objs"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                objects = json.load(f)
                for key in objects:
                    class_name, id = key.split(".")
                    self.__objects[key] = globals()[class_name](**objects[key])
        except FileNotFoundError:
            pass
