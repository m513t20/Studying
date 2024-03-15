

from src.exceptions import argument_exception
from models.nomenclature_model import nomenclature_model
from models.range_model import range_model
from src.storage.storage_model import storage_model
import uuid

class storage_turn_model:
    #склад
    __storage:storage_model=None

    #оборот
    __amount:int=0


    #период
    __nomenclature:nomenclature_model=None

    #еденица измерения
    __range:range_model=None

    @property
    def storage(self):
        return self.__storage
    
    @property 
    def amount(self):
        return self.__amount
    
    @property
    def nomenclature(self):
        return self.__nomenclature
    
    @property
    def range(self):
        return self.__range

    
    @storage.setter
    def storage(self,value:storage_model):
        if not isinstance(value,storage_model):
            raise argument_exception("Невереный аргумент!")
        
        self.__storage=value

    
    @amount.setter
    def amount(self,value:int):
        if not isinstance(value,int):
            raise argument_exception("Невереный аргумент!")
        
        self.__amount=value


    @nomenclature.setter
    def nomenclature(self,value:nomenclature_model):
        if not isinstance(value,nomenclature_model):
            raise argument_exception("Невереный аргумент!")
        
        self.__nomenclature=value


    @range.setter
    def range(self,value:range_model):
        if not isinstance(value,range_model):
            raise argument_exception("Невереный аргумент!")
        
        self.__range=value

    
    def __init__(self,stor:storage_model,amount:int,nom:nomenclature_model,ran:range_model) -> None:
        self.amount=amount
        self.storage=stor
        self.nomenclature=nom
        self.range=ran
        