#!/usr/bin/python3
"""console.py - entry point
    of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    while input == "":
        pass

    def do_EOF(self, line):
        "Exit"
        return True

    def do_quit(self, line):
        "Quit commany to exit program\n"
        raise SystemExit

    if __name__ == '__main__':
        HBNBCommand().cmdloop()
