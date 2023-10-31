#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        objects = FileStorage.__objects
        objs = {obj: objects[obj].to_dict() for obj in objects.keys()}
        with open(self.__file_path, 'w') as file:
            json.dump(objs, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                dict_objects = json.load(file)
                for obj in dict_objects.values():
                    obj = eval(obj['__class__'])(**obj)
                    self.new(obj)
        except FileNotFoundError:
            pass
