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
import sys

class HBNBCommand(cmd.Cmd):
    # The \n on the commands might cause problem

    prompt = '(hbtn) '
    classes = ['BaseModel', 'City', 'Place', 'Review', 'State', 'User', 'Amenity']

    def do_EOF(self, arg):
        'Ctrl-D (i.e. EOF) to exit \n'
        exit()
        
    def do_quit(self, arg):
        'Quit command to exit the program \n'
        quit()
        
    def emptyline(self):
         pass

    def do_create(self, arg):
        'Creates a new instance of A Class, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel \n'

        if arg == "":
            print("** class name missing **")
            return

        if arg != "" and arg not in self.classes:
            print("** class doesn't exist **")
            return

        model = BaseModel()
        model.save()
        print(model.id)

    def do_show(self, arg):
        'Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234. \n'
        args = arg.split(" ")

        if args[0] == "":
            print("** class name missing **")
            return

        if args[0] != "" and args[0] not in self.classes:
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

    def do_destroy(self, arg):
        'Deletes an instance based on the class name and id (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234. \n'

        args = arg.split(" ")

        if args[0] == "":
            print("** class name missing **")
            return

        if args[0] != "" and args[0] not in self.classes:
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
        'Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all. \n'

        if len(arg) > 0 and arg not in self.classes:
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


    def do_update(self, arg):
        'Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com". \n'

        args = shlex.split(arg)

        if args[0] == "":
            print("** class name missing **")
            return

        if args[0] != "" and args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2 and args[1] == "":
            print("** instance id missing **")
            return

        if len(args) < 3 and args[2] == "":
            print("** attribute name missing **")
            return

        if len(args) < 4 and args[3] == "":
            print("** value missing **")
            return

        storage.reload()
        allData = storage.all()

        if args[0] + '.' + args[1] in allData.keys():
            if args[2] != 'id' or args[2] != 'created_at' or args[2] != 'updated_at':
                allData[args[0] + '.' + args[1]][args[2]] = args[3]
                storage.save()
        else:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()