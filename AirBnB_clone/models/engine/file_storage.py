import json

class FileStorage:
    """The storage class for the storage of other classes"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary object"""

        return self.__objects


    def new(self, obj):
        """Creates a new object for the/a particular class"""

        classname = obj.__class__.__name__
        _id = obj.id

        key = "{}.{}".format(classname, _id)
        self.__objects[key] = obj

    def save(self):
        """Serializes objects to the json file path(__file_path)"""

        obj_dict = {}
        for key, value in self.__objects:
            obj_dict[key] = value

        with open(self.__file_path, 'w') as json_file:
            json.dump(obj_dict, json_file, indent= 4)


    def reload(self):
        """Deserializes the json file that was initially serialized into python objects"""

        try:
            with open(self.__file_path, 'r') as json_file:
                new_json = json.load(json_file)

        except FileNotFoundError:
            pass
