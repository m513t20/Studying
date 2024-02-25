from pathlib import Path
import os
import sys


sys.path.append(Path(__file__).parent.parent)



from abstract_reference import abstract_reference
from exceptions import argument_exception

class reciepe_model(abstract_reference):
    __coocking_algoritm=""
    __ingridient_proportions={}



    def __init__(self,name:str="untituled",algrotim:str="do whatever", propotions:dict={"a":"v"}):
        self.name=name

        self.__id=self.get_id()

        self.coocking_algoritm=algrotim

        self.ingrident_proportions=propotions


    @property
    def coocking_algoritm(self):
        return self.__coocking_algoritm
    
    @coocking_algoritm.setter 
    def coocking_algoritm(self,value: str):
        if not isinstance(value,str):
            raise argument_exception("Некорректный аргумент")
        
        value_stripped=value.strip() 

        if value_stripped=="":
            raise argument_exception("Некорректный аргумент")
        
        self.__coocking_algoritm=value_stripped


    @property
    def ingridient_proportions(self):
        return self.__ingridient_proportions
    
    @ingridient_proportions.setter
    def ingridient_proportions(self,value:dict):

        if not isinstance(value,dict) or len(value):
            raise argument_exception("Некорректный аргумент")
        
        self.__ingridient_proportions=value



