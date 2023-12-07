#!/usr/bin/python3
"""FIlestorage module"""

from models.base_model1 import BaseModel
import json


class FileStorage(BaseModel):
    """filestorage class"""
    def __init__(self, __file__path=None, __objects={}):
        self.__file__path = __file__path
        self.__objects = _objects

    def all(self):
        __objects = "{}.{}".format(self.__class__.__name__, self.id)
        return {__objects, value}
    def new(self,obj):
        obj = "obj{}.{}".format(self.__class__.__name__, self.id)
    
    def save(self):
        json.dump(__objects, __file__path, indent=4)

    def reload(self):
        if __file__path:
            return json.load(__objects)
