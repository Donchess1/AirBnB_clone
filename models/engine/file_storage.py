#!/usr/bin/python3
"""FIlestorage module"""

from models.base_model1 import BaseModel
import json
class FileStorage(BaseModel):
    """filestorage class"""
    def __init__(self, _file_path=None, _objects=None):
        self._file_path = _file_path
        self._objects = _objects

    def _objects(self):
        objects = "{}.{}".format(self.__class__.__name__, self.id)
        return {objects, value}

    def _file_path(self):
        file_path = os.path.dirname(os.path.realpath(__file__))
        return 

