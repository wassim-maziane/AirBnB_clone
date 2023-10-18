#!/usr/bin/python3
import uuid
from models import storage
from datetime import datetime
class BaseModel:
    def __init__(self, **kwargs):
        if len(kwargs) == 0:    
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)	
        else:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
    def __str__(self):
        return f"{self.__class__.__name__} ({self.id}) {self.__dict__}"
    def save(self):
       	storage.save() 
       	self.updated_at = datetime.now()
    def to_dict(self):
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic


