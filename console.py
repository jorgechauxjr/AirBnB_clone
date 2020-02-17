#!/usr/bin/python3
import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """hbnb command interpreter class"""

    prompt = '(hbnb) '

    __myClasses = [
        "BaseModel", "User", "State",
        "City", "Place", "Amenity", "Review"]

    def do_EOF(self, line):
        """End of file function """
        return True

    def do_quit(self, line):
        """Command that quit"""
        return True

    def do_create(self, args):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        args = shlex.split(args)
        if args == []:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__myClasses:
            print("** class doesn't exist **")
        else:
            models.storage.reload()
            instance = eval(args[0])()
            instance.save()
            print(instance.id)

    def do_show(self, args):
        """Prints the string representation of an
        instance based on the class name and id"""
        args = shlex.split(args)
        if args == []:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__myClasses:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            models.storage.reload()
            for key, obj in models.storage.all().items():
                if obj.id == args[1] and obj.__class__.__name__ == args[0]:
                    print(obj.__str__())
                    return
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(args)
        if args == []:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__myClasses:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            models.storage.reload()
            my_objs = models.storage.all()
            for k, obj in my_objs.items():
                if obj.id == args[1] and obj.__class__.__name__ == args[0]:
                    del(my_objs[k])
                    models.storage.save()
                    return
            print("** no instance found **")

    def do_all(self, args):
        """ Prints all string representation of all
        instances based or not on the class name."""
        args = shlex.split(args)
        if args[0] not in HBNBCommand.__myClasses:
            print("** class doesn't exist **")
        else:
            models.storage.reload()
            my_list = []
            for i, obj in models.storage.all().items():
                if obj.__class__.__name__ == args[0]:
                    my_list.append(obj.__str__())
            print(my_list)

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating attribute """
        pass

    def emptyline(self):
        """print a new empty line"""
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
