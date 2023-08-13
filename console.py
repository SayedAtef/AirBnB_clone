#!/usr/bin/python3
""" AirBnB The """
import cmd
import sys
import os
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand  Class Console """
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel, 'User': User, 'City': City,
               'Place': Place, 'Amenity': Amenity, 'Review': Review,
               'State': State}

    def do_quit(self, arg):
        """ Quit command to exit the program """
        exit()

    def do_EOF(self, arg):
        """ Exit method for EOF """
        print('')
        exit()

    def emptyline(self):
        """ Method to pass when entering emptyline """
        pass

    def do_create(self, arg):
        """ Create a new instance of base model """
        if len(arg) == 0:
            print('** class name missing **')
            return
        newInstance = None
        if arg:
            arg_list = arg.split()
            if len(arg_list) == 1:
                if arg in self.classes.keys():
                    newInstance = self.classes[arg]()
                    newInstance.save()
                    print(newInstance.id)
                else:
                    print("** class doesn't exist **")


    def do_show(self, arg):
        """ Method to print string rep of instance """
        if len(arg) == 0:
            print('** class name missing **')
            return
        elif arg.split()[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg.split()) > 1:
            keyInstance = arg.split()[0] + '.' + arg.split()[1]
            if keyInstance in storage.all():
                instance = storage.all()
                print(instance[keyInstance])
            else:
                print('** no instance found **')
        else:
            print('** instance id missing **')
        
    def do_destroy(self, arg):
        """ Method to delete instance with both class and id """
        if len(arg) == 0:
            print("** class name missing **")
            return
        argumentList = arg.split()
        try:
            obj = eval(argumentList[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(argumentList) == 1:
            print('** instance id missing **')
            return
        if len(argumentList) > 1:
            key = argumentList[0] + '.' + argumentList[1]
            if key in storage.all():
                storage.all().pop(key)
                storage.save()
            else:
                print('** no instance found **')
                return

    def do_all(self, arg):
        """ Method to print all instances """
        if len(arg) == 0:
            print([str(a) for a in storage.all().values()])
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(a) for b, a in storage.all().items() if arg in b])

    def do_update(self, arg):
        """ Method to update JSON file"""
        arg = arg.split()
        if len(arg) == 0:
            print('** class name missing **')
            return
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print('** instance id missing **')
            return
        else:
            key = arg[0] + '.' + arg[1]
            if key in storage.all():
                if len(arg) > 2:
                    if len(arg) == 3:
                        print('** value missing **')
                    else:
                        setattr(
                            storage.all()[key],
                            arg[2],
                            arg[3][1:-1])
                        storage.all()[key].save()
                else:
                    print('** attribute name missing **')
            else:
                print('** no instance found **')

if __name__ == '__main__':
    HBNBCommand().cmdloop()