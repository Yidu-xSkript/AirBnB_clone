#!/usr/bin/python3
"""Define Console"""
import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review  import Review
from models.state import State
from models.user import User
from models import storage
import shlex
import re

def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in shlex.split(arg)]
        else:
            lexer = shlex.split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = shlex.split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl

class HBNBCommand(cmd.Cmd):
    """Command Interpreter for AirBnB Clone Project"""

    prompt = '(hbnb) '
    __classes = ['BaseModel', 'City', 'Place', 'Review', 'State', 'User', 'Amenity']

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True
        
    def emptyarg(self):
         pass

    def do_create(self, arg):
        """Creates a new instance of A Class, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel."""
        if arg == "":
            print("** class name missing **")
            return

        if arg != "" and arg not in self.__classes:
            print("** class doesn't exist **")
            return

        print(eval(arg)().id)
        storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234."""
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
            return

        if len(args) > 0 and args[0] not in self.__classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        storage.reload()
        allData = storage.all()

        if args[0] + '.' + args[1] in allData.keys():
            print(f"{allData[args[0] + '.' + args[1]]}")
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234."""
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
            return

        if len(args) > 0 and args[0] not in self.__classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        storage.reload()
        allData = storage.all()
        
        if args[0] + '.' + args[1] in allData.keys():
            allData.pop(args[0] + '.' + args[1])
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all."""   
        
        args = shlex.split(arg)
        if len(args) > 0 and args[0] not in self.__classes:
            print("** class doesn't exist **")
            return

        storage.reload()
        allData = storage.all()

        splitData = list()
        for data in allData.values():
            if len(args) > 0 and args[0] == data.__class__.__name__:
                splitData.append(data.__str__())
            if len(args) == 0:
                splitData.append(data.__str__())

        print(splitData)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update <classname> <instance-id> <attribute-name> <value>."""
        args = parse(arg)

        if len(args) == 0:
            print("** class name missing **")
            return

        if len(args) > 0 and args[0] not in self.__classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        storage.reload()
        allData = storage.all()

        if "{}.{}".format(args[0], args[1]) not in allData.keys():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return

        if len(args) == 4:
            if args[2] in allData[args[0] + '.' + args[1]].__class__.__dict__.keys():
                valtype = type(allData[args[0] + '.' + args[1]].__class__.__dict__[args[2]])
                allData[args[0] + '.' + args[1]].__dict__[args[2]] = valtype(args[3])
            else:
                allData[args[0] + '.' + args[1]].__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            for k, v in eval(args[2]).items():
                if (k in allData[args[0] + '.' + args[1]].__class__.__dict__.keys() and type(allData[args[0] + '.' + args[1]].__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(allData[args[0] + '.' + args[1]].__class__.__dict__[k])
                    allData[args[0] + '.' + args[1]].__dict__[k] = valtype(v)
                else:
                    allData[args[0] + '.' + args[1]].__dict__[k] = v
        storage.save()

    def do_count(self, arg):
        """Counts how many items there are based on a <classname>"""
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
            return

        storage.reload()
        allData = storage.all()

        dataKey = list(allData.keys())
        splitData = list()

        for i in range(len(dataKey)):            
            if args[0] == dataKey[i].split(".")[0]:
                splitData.append(dataKey[i].split(".")[0])

        print(len(splitData))

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()