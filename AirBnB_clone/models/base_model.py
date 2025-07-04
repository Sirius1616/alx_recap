"""Module for BaseModel class."""
import uuid
from datetime import datetime
from models import storage

"""BaseModel class for AirBnB clone project.
This class serves as the base for all other classes in the project.
It provides common attributes and methods for all models.
    """
class BaseModel:
    """BaseModel class for AirBnB clone project.
    Attributes:
        id (str): Unique identifier for each instance.
        created_at (datetime): Timestamp of when the instance was created.
        updated_at (datetime): Timestamp of when the instance was last updated.
    """
    def __init__(self, *args, **kwargs):

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ('created_at', 'updated_at'):
                    value = datetime.strptime(alue, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        storage.new()

    def __str__(self):
        """Prints a string format for each of the model created
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__)


    def save(self):
        """Updates the public instance attribute updated_at when the function is called on a model object"""
        self.updated_at = datetime.now()
        storage.save()

    
    def to_dict(self):
        """returns a dictionary format for the object ready for serializing"""
        
        dictn = self.__dict__.copy()
        dictn['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        dictn['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        dictn['id'] = self.id
        dictn['__class__'] = self.__class__.__name__
        return dictn



