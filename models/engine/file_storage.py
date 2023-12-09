#!/usr/bin/env python3

""" Module for saving and loading instances to JSON """

import json


class FileStorage:

    """ Class that stores and loads instances to/from files in JSON format """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary (__objects) """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj key <obj class name>.id """
        obj_id = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[obj_id] = obj

    def save(self):
        """ this saves the __object into the JSON file with path: __file_path """
        json_dic = {}

        for key, value in FileStorage.__objects.items():
            json_dic[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as myfile:
            json.dump(json_dic, myfile)

    def reload(self):
        """retrieves the JSON file to __objects if  the JSON file
        (__file_path) exists """
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as myfile:
                from models.base_model import BaseModel
                from models.user import User
                from models.city import City
                from models.amenity import Amenity
                from models.place import Place
                from models.review import Review
                from models.state import State

                my_obj = json.load(myfile)
                for key, value in my_obj.items():
                    my_class = value["__class__"]
                    obj = eval(my_class + "(**value)")
                    FileStorage.__objects[key] = obj
        except IOError:
            pass
