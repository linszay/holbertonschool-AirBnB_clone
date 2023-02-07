#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
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
        dict_key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[dict_key] = obj

    def save(self):
        """serializes objs to JSON file"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            temp_dict = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(temp_dict, f)

    def reload(self):
        """deserializes JSON file to objs"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                temp_dict = json.load(f)
                for k, v in temp_dict.items():
                    obj_id = k.split('.')
                    self.__objects[k] = eval(obj_id[0])(**v)
        except FileNotFoundError:
            pass
