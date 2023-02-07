#!/usr/bin/python3
"""console.py import basemodel"""


import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Quit the program"""
        return True

    def do_create(self, args):
        """Create instance of BaseModel, save it (to the JSON file) print id.
                Ex: $ create BaseModel"""
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args.split()[0]
        if class_name in models.classes:
            new_model = models.classes[class_name]()
            new_model.save()
            print(new_model.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Print string rep of an instance based on the class name and id.
                Ex: $ show BaseModel 1234-1234-1234."""
        if len(args) == 0:
            print("** class name missing **")
            return
        args = args.split()
        if len(args) == 1:
            print("** instance id missing **")
            return
        class_name, obj_id = args[0], args[1]
        if class_name in models.classes:
            objects = models.storage.all()
            for key, value in objects.items():
                if class_name in key and obj_id in key:
                    print(value)
                    return
            print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """Deletes instance based on class name and id (save into JSON file).
                Ex: $ destroy BaseModel 1234-1234-1234."""
        if len(args) == 0:
            print("** class name missing **")
            return
        args = args.split()
        if len(args) == 1:
            print("** instance id missing **")
            return
        class_name, obj_id = args[0], args[1]
        if class_name in models.classes:
            objects = models.storage.all()
            for key in list(objects.keys()):
                if class_name in key and obj_id in key:
                    models.storage.delete(objects[key])
                    return
            print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """Prints all string rep of all instances.
                Ex: $ all BaseModel or $ all."""
        objects = models.storage.all()
        obj_list = []
        if len(args) == 0:
            for value in objects.values():
                obj_list.append(str(value))
        else:
            class_name = args.split
