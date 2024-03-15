
import uuid
from datetime import datetime
from src.models.nomenclature_model import nomenclature_model
from src.exceptions import argument_exception



class storage_journal_transaction:
    __type:bool=None 
    
    __period:datetime=None

    __nomenclature:nomenclature_model=None

    __id:uuid=None


    @property
    def id(self):
        return self.__id
    
    @property
    def period(self):
        return self.__period

    @property 
    def type(self):
        return self.__type*"add" +(not (self.__type))*"delete"


    @property
    def nomenclature(self):
        return self.__nomenclature

    @type.setter
    def type(self,value:bool):
        if not isinstance(value,bool):
            raise  argument_exception("Некорректный аргумент")
        
        self.__type=value

    @period.setter
    def period(self,value:datetime):
        if not isinstance(value,datetime):
            raise  argument_exception("Некорректный аргумент")
        
        self.__period=value
    
    @nomenclature.setter
    def nomenclature(self,value:nomenclature_model):
        if not isinstance(value,nomenclature_model):
            raise argument_exception("Wrong argument")
        self.__nomenclature=value



    def __init__(self,type_arg:bool,nomenclature:nomenclature_model,date:datetime) -> None:
        self.type=type_arg
        self.nomenclature=nomenclature
        self.period=date
        self.__id=uuid.uuid4()
