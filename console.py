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

class HBNBCommand(cmd.Cmd):
    # The \n on the commands might cause a problem

    prompt = '(hbtn) '
    classes = ['BaseModel', 'City', 'Place', 'Review', 'State', 'User', 'Amenity']

    def help_EOF(self):
        print('Ctrl-D (i.e. EOF) to exit \n')

    def do_EOF(self, arg):
        exit()

    def help_quit(self):
        print('Quit command to exit the program \n')

    def do_quit(self, arg):
        quit()
        
    def emptyline(self):
         pass

    def help_create(self):
        print('Creates a new instance of A Class, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel \n')

    def do_create(self, arg):
        if arg == "":
            print("** class name missing **")
            return

        if arg != "" and arg not in self.classes:
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

        if len(args) > 0 and args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        storage.reload()
        allData = storage.all()

        if args[0] + '.' + args[1] in allData.keys():
            print(f"[{args[0]}] ({args[1]}) {allData[args[0] + '.' + args[1]]}")
        else:
            print("** no instance found **")

    def help_destroy(self):
        print('Deletes an instance based on the class name and id (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234. \n')

    def do_destroy(self, arg):
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
            return

        if len(args) > 0 and args[0] not in self.classes:
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
        if arg != "" and arg not in self.classes:
            print("** class doesn't exist **")
            return

        storage.reload()
        allData = storage.all()

        dataKey = list(allData.keys())
        splitData = list()

        for i in range(len(dataKey)):            
            if len(arg) > 0 and arg == dataKey[i].split(".")[0]:
                splitData.append("[{}] ({}) {}".format(dataKey[i].split(".")[0], list(allData.values())[i]['id'], list(allData.values())[i]))
            elif len(arg) == 0:
                splitData.append("[{}] ({}) {}".format(dataKey[i].split(".")[0], list(allData.values())[i]['id'], list(allData.values())[i]))

        print(splitData)

    def help_update(self):
        print('Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com". \n')

    def do_update(self, arg):
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
            return

        if len(args) > 0 and args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        storage.reload()
        allData = storage.all()

        if args[0] + '.' + args[1] in allData.keys():
            if args[2] != 'id' and args[2] != 'created_at' and args[2] != 'updated_at':
                allData[args[0] + '.' + args[1]][args[2]] = args[3]
                storage.save()
        else:
            print("** no instance found **")

    def do_count(self, arg):
        if arg != "" and arg not in self.classes:
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
        
        if c[0] not in self.classes:
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

        # if len(splitable) == 2:
        #     pass

        if len(splitable) == 3:
            if c[1].replace('("' + splitable[0] + '", "' + splitable[1] + '", "' + splitable[2] + '")', '') == "update":
                return super().onecmd(f'update {c[0]} {splitable[0]} {splitable[1]} {splitable[2]}')

if __name__ == '__main__':
    HBNBCommand().cmdloop()