#!/usr/bin/python3
"""FileStorage class."""
import datetime
import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all method"""
        return FileStorage.__objects

    def new(self, obj):
        """new method"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """save method"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                jf = json.load(f)
            for key in jf:
                self.__objects[key] = classes[jf[key]["__class__"]](**jf[key])
        except:
            pass
