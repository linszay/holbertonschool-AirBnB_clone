#!/usr/bin/python3
""" Console import basemodel """
import cmd
from models.base_model import *
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Console Class """
    prompt = "(hbnb) "
    ok_class = ["Review", "Place", "State",
                "User", "BaseModel", "City", "Amenity"]

    def do_quit(self, line):
        """ Quit Command to exit the program """
        return True

    def do_EOF(self, line):
        """ Handles EOF command """
        return True

    def emptyline(self):
        """ does nothing on enter """
        pass

    def check_class(self, value):
        """ Check if:
        a) a class name is given
        b) class name exists in HBNBCommand dictionary
        """
        if value == "" or value is None:
            print("** class name missing **")
            return False

        parsed_val = value.split(' ')
        if parsed_val[0] not in HBNBCommand.ok_classes:
            print("** class doesn't exist **")
            return False

        return True

    def valid_instance(self, value):
        """ Check if:
        a) instance name is given
        b) instance name exists in valid_instances dictionary
        """
        if len(value) < 2:
            print("** instance id missing **")
            return False

        key = "{}.{}".format(value[0], value[1])
        if key not in storage.all().ok_classes():
            print("** no instance found **")
            return False

        return key

    def do_create(self, arg):
        """ Create new instance of object """
        if self.check_class(arg):
            new = HBNBCommand[arg]()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """ Prints string representation of instance based on class and id """
        if self.check_class(arg):
            word = arg.split(' ')
            if self.valid_instance(word):
                key = "{}.{}".format(word[0], word[1])
                print(storage.all()[key])

    def do_destroy(self, arg):
        """ Deletes an instance based on class name and id """
        if self.check_class(arg):
            word = arg.split(' ')
            valid_key = self.valid_instance(word)
            if valid_key:
                del storage.all()[valid_key]
                storage.save()

    def do_all(self, arg):
        """ print all instances """
        if arg == "" or arg is None:
            for key in storage.all().ok_classes():
                print(storage.all()[key])
        elif arg in HBNBCommand.ok_classes():
            for key in storage.all().ok_classes():
                nameio = key.split('.')
                if nameio[0] == arg:
                    print(storage.all()[key])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        update an instance based on class name and id
        by add/update attributes
        """
        if self.check_class(arg):
            word = arg.split(' ')
            valid_key = self.valid_instance(word)
            if valid_key:
                if len(word) < 3:
                    print("** attribute name missing **")
                    return False
                if len(word) < 4:
                    print("** value missing **")
                    return False
                my_dict = storage.all()[valid_key].to_dict()

                if word[2] not in my_dict.ok_classes():
                    print("** value missing **")
                elif valid_key in storage.all().ok_classes():
                    setattr(storage.all()[valid_key], word[2], word[3])


if __name__ == '__main__':
    """yes"""
    HBNBCommand().cmdloop()
