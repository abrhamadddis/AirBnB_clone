#!/usr/bin/python3
'''
A module BaseModel that defines all common attributes/methods for other modules
'''

from datetime import date, datetime
from uuid import uuid4
from models import storage


class BaseModel:
    '''
    a class that defines a base model for all modules
    '''
    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel

        Args:
            *args: unused
            **kwargs: key/value pair of arguments
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        t = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k == "created_at" or k == "updated_at":
                        self.__dict__[k] = datetime.strptime(v, t)
                    else:
                        self.__dict__[k] = v
        else:
            storage.new()

    def __str__(self):
        '''
        a string representation of Rectatngle
        '''
        a, b, c = self.__class__.__name__, self.id, self.__dict__
        return("[{:s}] ({:s}) {}".format(a, b, c))

    def save(self):
        '''
        updates a updated day of an object
        '''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''
        returns dictionary value of all key/values
        '''
        idme = self.id
        created = self.created_at.isoformat()
        updated = self.updated_at.isoformat()
        classname = self.__class__.__name__
        di = {'id': idme, 'created_at': created, 'updated_at': updated, '__class__': classname}
        return di
