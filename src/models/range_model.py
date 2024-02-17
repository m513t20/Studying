from pathlib import Path
import os
import sys

sys.path.append(Path(__file__).parent.parent)



from abstract_reference import abstract_reference
from exceptions import argument_exception
from settings import settings
import uuid

class range_model(abstract_reference):
    __recount_ratio:int=1 
    __base_range=None
    

    def __init__(self, name:str="untituled", ratio:int=1, base=None):
        self.name=name 

        self.recount_ratio=ratio 

        self.__id=self.get_id()

        if base:
            self.base_range=base 

    

    #коэффициент пересчёта
    @property 
    def recount_ratio(self):
        return self.__recount_ratio
    #сеттер
    @recount_ratio.setter
    def recount_ratio(self,value):
        
        if not isinstance(value,int):
            raise argument_exception("некорректный тип данных!")
        #если, он ниже 0 вызываем исключение
        if value<=0:
            raise argument_exception("некорректный аргумент")

        self.__recount_ratio=value        


    #базовая еденица
    @property 
    def base_range(self):
        return self.__base_range
    #сеттер
    @base_range.setter
    def base_range(self,value):
        if not isinstance(value,range_model):
            raise argument_exception("некорректный аргумент")
        
        self.__base_range=value
