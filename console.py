#!/usr/bin/python3
"""
Console entry point
"""

from ast import parse
from models.base_model import BaseModel
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """A class that defines a console"""
    prompt = '(hbnb) '
    __classes = {"BaseModel"}

    def do_quit(self, arg):
        """a command to quit the terminal"""
        sys.exit()

    def do_EOF(self, arg):
        """a command to quit the terminal"""
        sys.exit()

    def do_hbnb(self, arg):
        """custom command to implment hbnb"""
        print("excuiting hbnb")

    def emptyline(self):
        """pass an empty input"""
        pass

    def do_create(self, arg):
        """Create a Class with console"""
        if len(arg) == 0:
            print("** class name missing **")
        elif sys.argv[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(sys.argv[0])().id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if len(arg) == 0:
            print("** class name missing **")
        elif sys.argv[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(sys.argv[0])().id)


if __name__ == '__main__':
    """Entry point"""
    HBNBCommand().cmdloop()
    cmd.cmdloop()
