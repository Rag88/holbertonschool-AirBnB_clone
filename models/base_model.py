#!/usr/bin/python3
"""
Class BaseModel that defines all common attributes/methods for other classes
"""


import uuid
from datetime import datetime
import models


class BaseModel:
    """
    3 Public instances attributes:
    id: uuid when an instance is created
    created_at: current datetime when an instance is created
    updated_at: current datetime when an instance is created and
                it will be updated every time you change your object
    4 Public instance methods:
    __init__: Method used to create an instance of the object
    __str__: Method used to print the representation of the obj
    save: updates the public instance attribute updated_at
          with the current datetime
    to_dict: Returns a dictionary containing all keys/values of
             the instance
    """

    def __init__(self):
        """
        Instantation of class (id, created_at, updated_at)
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Method returns string representation
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        new_dic = vars(self).copy()
        new_dic['__class__'] = self.__class__.__name__
        new_dic['created_at'] = self.created_at.isoformat()
        new_dic['updated_at'] = self.updated_at.isoformat()
        return (new_dic)
