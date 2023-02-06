#!/usr/bin/python3
"""CONSOLE"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand contains the entry point of the command interpreter"""
    prompt = '(hbnb) '

    def do_quit(self, args):
        """quit command to exit the program"""
        raise SystemExit

    def do_EOF(self, args):
        """EOF command to exit the program"""
        raise SystemExit

    def emptyline(self):
        """Empty line or ENTER entered by user should not execute anything"""
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
