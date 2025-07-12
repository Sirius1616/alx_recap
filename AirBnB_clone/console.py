#!/usr/bin/env python3
import cmd
from models.base_model import BaseModel
from models.user import User
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
            print("** class name is missing **")
        else:
            clases = ['BaseModel', 'User']
            
            if arg[0] not in clases:
                print("** class doesn't exist **")
            else:
                new_model = eval(arg[0])()
                new_model_id = new_model.id
                new_model.save()
                print("{}".format(new_model_id))

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        arg = arg.split()
        if not arg:
            print("** class name is missing **")
        else:
            clases = ['BaseModel', 'User']
            if arg[0] not in clases:
                print("** class doesn't exist **")
            else:
                if len(arg) < 2:
                    print("** instance id is missing **")
                else:
                    class_id = arg[0] + '.' + arg[1]
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
            print("** class name is missing **")
        else:
            clases = ['BaseModel', 'User']
            if arg[0] not in clases:
                print("** class doesn't exist **")
            else:
                if len(arg) < 2:
                    print("** instance id is missing **")
                else:
                    class_id = arg[0] + '.' + arg[1]
                    stored_objects = storage.all()
                    for model_id in stored_objects:
                        if class_id == model_id:
                            one = stored_objects
                            del stored_objects[class_id]
                            storage.save()
                            return
                    print("** no instance is found **")


    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        count = 0
        stored_object = storage.all()
        if not arg:
            for value in stored_object.items():
                    print(value[1])
                    count = count + 1

        else:
            for value in stored_object.items():
                
                if value[1].to_dict()['__class__'] == arg:
                    print(value[1])
                    count = count + 1
        if count < 1:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)"""
        if not arg:
            print("** class name missing **")
        else:
            list_class = []
            list_id = []
            arg_list = arg.split()
            stored_object = storage.all()
            if len(arg_list) > 0:
                for value in stored_object.items():
                    list_class.append(value[1].to_dict()['__class__'])
                    list_id.append(value[0])
                if arg_list[0] not in list_class:
                    print("** class doesn't exist **")
                else:
                    if len(arg_list) == 1:
                        print("** instance id missing **")
                    else:
                        if not list_class:
                            print("** class doesn't exist **")
                        else:
                            id_class = "{}.{}".format(arg_list[0], arg_list[1])
                            if id_class not in list_id:
                                print(list_id)
                                print(id_class)
                                print("** no instance found **")
                            else:
                                if len(arg_list) == 2:
                                    print("** attribute name missing **")
                                else:
                                    if len(arg_list) == 3:
                                        print("** value missing **")
                                    else:
                                        #stored_object[id_class].to_dict()[arg_list[2]] = arg_list[3]
                                        setattr(stored_object[id_class], arg_list[2], arg_list[3])
                                        stored_object[id_class].save()
                                        #print(stored_object[id_class].to_dict())
                                        #return

            else:
                pass
        #print(list_class)
        #print(list_id)

        #if len(arg_list) == 5:
        #    if arg_list[0] in 


    
if __name__ == '__main__':
    HBNBCommand().cmdloop()


