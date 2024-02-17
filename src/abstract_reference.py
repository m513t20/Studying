import uuid
from abc import ABC
from exceptions import argument_exception
from error_proxy import error_proxy

class abstract_reference(ABC):
    __id: uuid.UUID
    __name:str = " "
    __error: error_proxy = error_proxy()
    
    def __init__(self, name: str = "untituled") -> None:
        self.name = name
        self.__id=self.get_id()

        
    @property    
    def error(self):
        """
           Работа с ошибками

        Returns:
            _type_: _description_
        """
        return self.__error    
        
    @property    
    def id(self):
        """
            Уникальный код
        Returns:
            _type_: _description_
        """
        return self.__id    
    

    
    def get_id(self):
        return uuid.uuid4()

        
    @property    
    def name(self):
        """
           Наименование
        Returns:
            _type_: _description_
        """
        return self.__name.strip()    
   
    
    @name.setter 
    def name(self, value: str):
        
        if not isinstance(value,str):
            raise argument_exception("Неверный аргумент!")
        
        value_striped=value.strip()
        
        if value_striped== "" or len(value_striped)>50:
            raise argument_exception("Некорректное значение наименование!")
        
        self.__name = value_striped
        
        