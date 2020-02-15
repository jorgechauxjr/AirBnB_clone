#!/usr/bin/python3
import cmd
import shlex
import models


class HBNBCommand(cmd.Cmd):
    """hbnb command interpreter class"""

    prompt = '(hbnb) '

    __myClasses = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]

    def do_EOF(self, line):
        """End of file function """
        return True

    def do_quit(self, line):
        """Command that quit"""
        return True

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        args = shlex.split(args)
        if args == []:
            print("** class doesn't exist **")
        elif args[0] not in HBNBCommand.__myClasses:
            print("** class doesn't exist **")
        pass

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        pass

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        pass

    def do_all(self, line):
        """ Prints all string representation of all instances based or not on the class name."""
        pass

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute """
        pass
    


    def emptyline(self):
        """print a new empty line"""
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
