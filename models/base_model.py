#!/usr/bin/python3
"""Module for Base class
Contains the Base class for the AirBnB clone console.
"""

import uuid
from datetime import datetime


class BaseModel:

    """Class for base model"""
    def __init__(self):
        """Initialization"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """str format"""
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.to_dict())

    def save(self):
        """updates."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """dictionary format"""
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict
