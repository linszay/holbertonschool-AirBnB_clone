#!/usr/bin/python3
"""console.py pycodestyle updated"""
import cmd
import json
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Command class for the HBNB console.
    """
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

    def do_quit(self, args):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """
        EOF command to exit the program
        """
        return True

    def do_create(self, args):
        """
        Creates a new instance of a class and saves it to a JSON file.
        """
        if not args:
            print("** class name missing **")
            return
        class_name = args.split()[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance based on class name and id.
        """
        if not args:
            print("** class name missing **")
            return
        class_name, instance_id = self.split_args(args)
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if not instance_id:
            print("** instance id missing **")
            return
        key = "{}.{}".format(class_name, instance_id)
        if key not in models.storage.all():
            print("** no instance found **")
            return
        print(models.storage.all()[key])

    def do_destroy(self, args):
        """
        Deletes an instance based on class name and id and saves changes to JSON file.
        """
        if not args:
            print("** class name missing **")
            return
        class_name, instance_id = self.split_args(args)
       
