#!/usr/bin/python3
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    # Your command interpreter should implement: 
    # - quit and EOF to exit the program
    # - help (this action is provided by default by cmd but you should keep it updated and documented as you work through tasks)
    # - a custom prompt: (hbnb)
    # - an empty line + ENTER shouldn’t execute anything
    # Your code should not be executed when imported
    # if __name__ == '__main__':
    # HBNBCommand().cmdloop()

    # ----------------------------------------
    # RULES
    # =========================
    # You can assume arguments are always in the right order
    # Each arguments are separated by a space
    # A string argument with a space must be between double quote
    # The error management starts from the first argument to the last one

    def create():
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel
        """
        # Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel
        # If the class name is missing, print ** class name missing ** (ex: $ create)
        # If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ create MyModel)
        baseModel = BaseModel()
        pass

    def show():
        """
        Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234. 
        """
        # If the class name is missing, print ** class name missing ** (ex: $ show)
        # If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ show MyModel)
        # If the id is missing, print ** instance id missing ** (ex: $ show BaseModel)
        # If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ show BaseModel 121212)
        pass

    def destroy():
        """
         Deletes an instance based on the class name and id (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234. 
        """
        
        # If the class name is missing, print ** class name missing ** (ex: $ destroy)
        # If the class name doesn’t exist, print ** class doesn't exist ** (ex:$ destroy MyModel)
        # If the id is missing, print ** instance id missing ** (ex: $ destroy BaseModel)
        # If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ destroy BaseModel 121212)

        pass

    def all():
        """
        Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all.
        """        
        # The printed result must be a list of strings (like the example below)
        # If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ all MyModel)
        pass

    def update():
        """
        Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). 
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com". 
        """

        # Usage: update <class name> <id> <attribute name> "<attribute value>"
        # Only one attribute can be updated at the time
        # You can assume the attribute name is valid (exists for this model)
        # The attribute value must be casted to the attribute type
        # If the class name is missing, print ** class name missing ** (ex: $ update)
        # If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ update MyModel)
        # If the id is missing, print ** instance id missing ** (ex: $ update BaseModel)
        # If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ update BaseModel 121212)
        # If the attribute name is missing, print ** attribute name missing ** (ex: $ update BaseModel existing-id)
        # If the value for the attribute name doesn’t exist, print ** value missing ** (ex: $ update BaseModel existing-id first_name)
        # All other arguments should not be used (Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com" first_name "Betty" = $ update BaseModel 1234-1234-1234 email "aibnb@mail.com")
        # id, created_at and updated_at cant’ be updated. You can assume they won’t be passed in the update command
        # Only “simple” arguments can be updated: string, integer and float. You can assume nobody will try to update list of ids or datetime

        pass
    
    def allClass():
        pass

    def count():
        pass