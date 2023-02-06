#!/usr/bin/python3
import json
import os
import models
"""creating filestorage class and dict to json"""


class FileStorage:
    """creating FileStorage class"""

    def __init__(self, file_path, objects):
        self.__file_path = str(json.file)
        self.__objects = {}

    def all(self):
        """function returns all"""
        return self.__objects

    def new(self, obj):
        """sets the obj with key such as <obj class name>.id"""
        dict_key = "{} {}".format(type(object).__class__.__name__, object.id)
        object.__class__.__name__ = dict_key

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
