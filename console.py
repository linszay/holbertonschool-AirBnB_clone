#!/usr/bin/python3
"""console.py import basemodel"""


import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_create(self, args):
        """Create a new instance of BaseModel, save it, and print the id."""
        if not args:
            print("** class name missing **")
            return

        class_name = args.split()[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        obj = self.classes[class_name]()
        obj.save()
        print(obj.id)

    def do_show(self, args):
        """Print str representation of instance based on class name and id."""
        if not args:
            print("** class name missing **")
            return

        class_name, obj_id = self.get_class_and_id(args)
        if not obj_id:
            print("** instance id missing **")
            return

        obj = models.storage.get(class_name, obj_id)
        if not obj:
            print("** no instance found **")
            return

        print(obj)

    def do_destroy(self, args):
        """Delete an instance based on the class name and id."""
        if not args:
            print("** class name missing **")
            return

        class_name, obj_id = self.get_class_and_id(args)
        if not obj_id:
            print("** instance id missing **")
            return

        obj = models.storage.get(class_name, obj_)
