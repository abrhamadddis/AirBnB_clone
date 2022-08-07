#!/usr/bin/python3
''' a module that serializes instances to a JSON'''

import json
from models.base_model import BaseModel


class FileStorage:
    '''a class that serializes/deserializes json/string
    Attributes:
        __file_path: name of file to save object
        __object: dictionary of object
    '''

    __file_path = 'file.json'
    __object = {}

    def all(self):
        ''' returns a dictionary object'''
        return FileStorage.__object

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        setattr(FileStorage.__object, obj.id, obj)

    def save(self):
        """Serializes __objects to the JSON file file.json"""
        with open(FileStorage.__file_path, "w") as f:
            new_obj_dict = {k: v.to_dict()
                            for k, v in FileStorage.__objects.items()}
            json.dump(new_obj_dict, f, indent=4)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    FileStorage.__objects[key] = value
        except FileNotFoundError:
            pass
