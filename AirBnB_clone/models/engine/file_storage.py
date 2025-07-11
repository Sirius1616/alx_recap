import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """The storage class for the storage of other classes"""

    __file_path = 'file.json'
    __objects = {}
    models = {'BaseModel': BaseModel, 'User': User}

    def all(self):
        """returns the dictionary object"""

        return FileStorage.__objects


    def new(self, obj):
        """Creates a new object for the/a particular class"""

        classname = obj.__class__.__name__
        _id = obj.id

        key = "{}.{}".format(classname, _id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes objects to the JSON file (__file_path)"""
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as json_file:
            json.dump(obj_dict, json_file, indent= 4)


    def reload(self):
        """Deserializes the json file that was initially serialized into python objects"""

        try:
            with open(FileStorage.__file_path, 'r') as json_file:
                new_json = json.load(json_file)
            for key, value in new_json.items():
                cls_name = value['__class__']
                if cls_name == "BaseModel":
                    FileStorage.__objects[key] = BaseModel(**value)

        except FileNotFoundError:
            pass
