#!/usr/bin/python3
"""console for handling database"""
import cmd
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    def do_EOF(self, line):
        return True
    def do_quit(self, line):
        return True
    def emptyline(self):
        pass
if __name__ == "__main__":
    HBNBCommand().cmdloop()
