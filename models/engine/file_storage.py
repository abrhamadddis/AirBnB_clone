#!/usr/bin/python3
''' a module that serializes instances to a JSON file and deserializes JSON file to instances'''

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
        '''serializes __objects to the JSON file (path: __file_path)'''
        mydict = FileStorage.__object.keys()
        for obj in mydict:
            mydict1 = {obj: mydict[obj].to_dict()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(mydict1, f, indent= 4)
    def reload(self):
        try:
            myFile = FileStorage.__file_path
            with open(myFile, 'w') as f:
                mydict = json.load(f)
            for key in mydict:
                classname = key["__class__"]
                del key["__class__"]
                self.new(eval(classname)(**key))
        except:
            pass