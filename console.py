import cmd
import shlex
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
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
        """Print string rep of an instance based on the class name and id."""
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
