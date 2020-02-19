#!/usr/bin/python3
"""FileStorage class."""
import datetime
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all method"""
        return FileStorage.__objects

    def new(self, obj):
        """new method"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """save method"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """reload method"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                jf = json.load(f)
            for key in jf:
                self.__objects[key] = classes[jf[key]["__class__"]](**jf[key])
        except Exception:
            pass
