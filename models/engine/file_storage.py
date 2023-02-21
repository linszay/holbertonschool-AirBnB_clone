#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

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
                    obj = eval(v['__class__'])(**v)
                    self.__objects[k] = obj
        except FileNotFoundError:
            pass
