#!/usr/bin/python3
"""console.py - entry point
    of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exit on EOF (Control-D)"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
