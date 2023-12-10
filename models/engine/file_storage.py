#!/usr/bin/env python3

""" Module for serializing and deserializing instances to JSON and keeping
storage of instances
"""

import json


class FileStorage:

    """ Class that stores and loads instances to/from files in JSON format """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj key <obj class name>.id """
        new_obj_id = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[new_obj_id] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        obj_dic = {}

        for key, value in FileStorage.__objects.items():
            obj_dic[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as filemi:
            json.dump(obj_dic, filemi)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file
        doesn’t exist, no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as filemi:
                from models.base_model import BaseModel
                from models.user import User
                from models.city import City
                from models.amenity import Amenity
                from models.place import Place
                from models.review import Review
                from models.state import State

                loaded_obj = json.load(filemi)
                for key, value in loaded_obj.items():
                    cls = value["__class__"]
                    obj = eval(cls + "(**value)")
                    FileStorage.__objects[key] = obj
        except IOError:
            pass
