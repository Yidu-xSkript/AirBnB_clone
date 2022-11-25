#!/usr/bin/python3
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
import json

class HBNBCommand(cmd.Cmd):
    # The \n on the commands might cause a problem

    prompt = '(hbtn) '
    __classes = ['BaseModel', 'City', 'Place', 'Review', 'State', 'User', 'Amenity']

    def help_EOF(self):
        print('Ctrl-D (i.e. EOF) to exit \n')

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        return True

    def help_quit(self):
        print('Quit command to exit the program \n')

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True
        
    def emptyline(self):
         pass

    def help_create(self):
        print('Creates a new instance of A Class, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel \n')

    def do_create(self, arg):
        if arg == "":
            print("** class name missing **")
            return

        if arg != "" and arg not in self.__classes:
            print("** class doesn't exist **")
            return

        model = BaseModel() if arg == "BaseModel" else User() if arg == "User" else Place() if arg == "Place" else City() if arg == "City" else Review() if arg == "Review" else State() if arg == "State" else Amenity()
        model.save()
        print(model.id)

    def help_show(self):
        print('Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234. \n')

    def do_show(self, arg):
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

    def help_destroy(self):
        print('Deletes an instance based on the class name and id (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234. \n')

    def do_destroy(self, arg):
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

    def help_all(self):
        print('Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all. \n')

    def do_all(self, arg):        
        if arg != "" and arg not in self.__classes:
            print("** class doesn't exist **")
            return

        storage.reload()
        allData = storage.all()

        splitData = list()
        for data in allData.values():
            if len(arg) > 0 and arg == data.__class__.__name__:
                splitData.append(data.__str__())
            if len(arg) == 0:
                splitData.append(data.__str__())

        print(splitData)

    def help_update(self):
        print('Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com". \n')

    def do_update(self, arg):
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

        if len(args) < 3 and type(eval(args[2])) != dict:
            print("** attribute name missing **")
            return

        if len(args) < 4 and type(eval(args[2])) != dict:
            print("** value missing **")
            return

        storage.reload()
        allData = storage.all()

        if args[0] + '.' + args[1] in allData.keys():
            if len(args) == 4:
                if args[2] != 'id' and args[2] != 'created_at' and args[2] != 'updated_at':
                    allData[args[0] + '.' + args[1]].__dict__[args[2]] = args[3]
            elif type(eval(args[2])) == dict:
                for k, v in eval(args[2]).items():
                    if (k in allData[args[0] + '.' + args[1]].__class__.__dict__.keys() and type(allData[args[0] + '.' + args[1]].__class__.__dict__[k]) in {str, int, float}):
                        valtype = type(allData[args[0] + '.' + args[1]].__class__.__dict__[k])
                        allData[args[0] + '.' + args[1]].__dict__[k] = valtype(v)
                    else:
                        allData[args[0] + '.' + args[1]].__dict__[k] = v
            storage.save()
        else:
            print("** no instance found **")

    def help_count(self):
        print("Counts how many items there are based on a <classname>")

    def do_count(self, arg):
        if arg != "" and arg not in self.__classes:
            print("** class doesn't exist **")
            return

        storage.reload()
        allData = storage.all()

        dataKey = list(allData.keys())
        splitData = list()

        for i in range(len(dataKey)):            
            if arg == dataKey[i].split(".")[0]:
                splitData.append(dataKey[i].split(".")[0])

        print(len(splitData))

    def onecmd(self, line: str) -> bool:
        c = line.split(".")

        if len(c) != 2 or line.count('.') != 1 or line.count('(') != 1 or line.count(')') != 1:
            return super().onecmd(line)
        
        if c[0] not in self.__classes:
            return super().onecmd(line)

        if c[1].replace('()', '') == "all": 
            return super().onecmd(f'all {c[0]}')

        if c[1].replace('()', '') == "count":
            return super().onecmd(f'count {c[0]}')

        splitable = re.findall('"([^"]*)"', c[1])

        if len(splitable) == 1:
            if c[1].replace('("' + splitable[0] + '")', '') == "show":
                return super().onecmd(f'show {c[0]} {splitable[0]}')
            if c[1].replace('("' + splitable[0] + '")', '') == "destroy":
                return super().onecmd(f'destroy {c[0]} {splitable[0]}')

        curly_braces = re.search(r"\{(.*?)\}", line)
        retl = []
        if curly_braces is not None:
            lexer = shlex.split(line[:curly_braces.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(curly_braces.group())

        if len(retl) == 2:
            _splitable = retl[0].split("(")
            _splitable2 = _splitable[0].split(".")
            if _splitable2[1] == "update":
                return super().onecmd(f'update {_splitable2[0]} {_splitable[1]} {json.dumps(retl[1])}')

        if len(splitable) == 3:
            if c[1].replace('("' + splitable[0] + '", "' + splitable[1] + '", "' + splitable[2] + '")', '') == "update":
                return super().onecmd(f'update {c[0]} {splitable[0]} {splitable[1]} {splitable[2]}')

if __name__ == '__main__':
    HBNBCommand().cmdloop()