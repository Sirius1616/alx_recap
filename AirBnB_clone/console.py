#!/usr/bin/env python3
import cmd
from models.base_model import BaseModel
from models import storage



class HBNBCommand(cmd.Cmd):
    """The console which inherits from the cmd modele and the controler of all other classes"""

    def do_exit(self, arg):
        """QUits the program"""
        print("Quiting the console")
        return True


    def do_EOF(self, arg):
        """Trying to leave the console due to the end of line"""

        return True


    def emptyline(self):
        """Handles empty line and does nothing when the empty line is prompted"""

        return False

    def do_create(self, *arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel"""
        if not arg:
            print("** class name missing **")
        else:
            clases = ['BaseModel']
            for model in clases:
                if arg[0] != model:
                    print("** class doesn't exist **")
                else:
                    new_model = eval(model)()
                    new_model_id = new_model.id
                    new_model.save()
                    print("{}".format(new_model_id))

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        arg = arg.split()
        if not arg:
            print("** class name missing **")
        else:
            clases = ['BaseModel']
            for model in clases:
                if arg[0] != model:
                    print("** class doesn't exist **")
                else:
                    if len(arg) < 2:
                        print("** instance id missing **")
                    else:
                        class_id = model + '.' + arg[1]
                        stored_objects = storage.all()
                        for model_id in stored_objects:
                            if class_id == model_id:
                                print(stored_objects[class_id])
                                return
                        print("** no instance found **")


    def do_destroy(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        arg = arg.split()
        if not arg:
            print("** class name missing **")
        else:
            clases = ['BaseModel']
            for model in clases:
                if arg[0] != model:
                    print("** class doesn't exist **")
                else:
                    if len(arg) < 2:
                        print("** instance id missing **")
                    else:
                        class_id = model + '.' + arg[1]
                        stored_objects = storage.all()
                        for model_id in stored_objects:
                            if class_id == model_id:
                                one = stored_objects
                                del stored_objects[class_id]
                                storage.save()
                                return
                        print("** no instance found **")


    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        obj_list = []
        stored_object = storage.all()
        if not arg:
            #print(arg.split()
            for key, value in stored_object:
                    obj_list.append(key, value.to_dict())

        else:
            for value in stored_object.items():
                print(value[1].to_dict())
                if value[1].to_dict()['__class__'] == arg[0]:
                    obj_list.append(value[1].to_dict())
                    print("No new Item appended")
        if not obj_list:
            print("** class doesn't exist **")
            print(obj_list)
        else:
            print(obj_list)
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()


