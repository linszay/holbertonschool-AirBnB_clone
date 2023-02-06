#!/usr/bin/python3
"""
This module contains the Console class that implements a command interpreter
to manipulate instances of the BaseModel class from the models module.
"""
import cmd
import models
from models.base_model import BaseModel
from shlex import split


class Console(cmd.Cmd):
    """
    A command interpreter class that inherits from the cmd library's Cmd class.
    Implements method to handle the creation, show, destroy, update and list of
    instances of the BaseModel class.
    """
    prompt = '(hbnb) '

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it to the JSON file and
        prints its id.
        """
        if not arg:
            print('** class name missing **')
            return
        class_name = arg.strip()
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return
        new_model = models.classes[class_name]()
        new_model.save()
        print(new_model.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name
        and id.
        """
        args = split(arg)
        if len(args) == 0:
            print('** class name missing **')
            return
        class_name = args[0].strip()
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print('** instance id missing **')
            return
        obj_id = args[1].strip()
        obj = models.storage.all().get(class_name + '.' + obj_id)
        if obj is None:
            print('** no instance found **')
            return
        print(obj)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id, saving the change
        into the JSON file.
        """
        args = split(arg)
        if len(args) == 0:
            print('** class name missing **')
            return
        class_name = args[0].strip()
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print('** instance id missing **')
            return
        obj_id = args[1].strip()
        obj = models.storage.all().get(class_name + '.' + obj_id)
        if obj is None:
            print('** no instance found **')
            return
        obj.delete()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the
        class name.
        """
        class_name = arg.strip()
        obj_list = []
        if class_name and class_name in models.classes:
            for obj in models.storage.all().values():
                if obj.__class__.__name__ == class_name:
