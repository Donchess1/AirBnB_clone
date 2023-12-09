#!/usr/bin/python3

""" Module that create a unique FileStorage instances """

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
