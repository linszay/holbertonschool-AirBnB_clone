#!/usr/bin/python3
"""console.py"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    Class definition for the command interpreter
    """
    prompt = '(hbnb) '

    def do_quit(self, args):
        """
        Command to quit the program
        """
        return True

    def do_EOF(self, args):
        """
        Command to quit the program on EOF (end-of-file)
        """
        return True

    def emptyline(self):
        """
        Action to be taken when an empty line is entered
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

