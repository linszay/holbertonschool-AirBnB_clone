#!/usr/bin/python3
"""console"""

import cmd
import json
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, line):
        """Create a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        """
        if line:
            args = line.split()
            if args[0] in ["BaseModel"]:
                new_instance = eval(args[0])()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """Prints the string representation of an instance based on the class
        name and id.
        """
        if line:
            args = line.split()
            if args[0] in ["BaseModel"]:
                if len(args) > 1:
                    key = args[0] + "." + args[1]
                    if key in storage.all().keys():
                        print(storage.all()[key])
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id (save the change
        into the JSON file).
        """
        if line:
            args = line.split()
            if args[0] in ["BaseModel"]:
                if len(args) > 1:
                    key = args[0] + "." + args[1]
                    if key in storage.all().keys():
                        del storage.all()[key]
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """Prints all string representation of all instances based or not on
        the class name.
        """
        instances = storage.all()
        if line:
            args = line.split()
            if args[0] in ["BaseModel"]:
                for key in instances:
                    if key.startswith(args[0]):
                        print(instances[key])
            else:
                print("** class doesn't exist **")
        else:
            for instance in instances.values():
                print(instance)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        """
        if line:
            args = line.split()
            if args[0] in ["BaseModel"]:
                if len(args) > 1:
                    key = args[0] + "." + args[1]
                    if key in storage.all().keys():