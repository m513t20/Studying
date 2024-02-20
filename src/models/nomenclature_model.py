from pathlib import Path
import os
import sys

sys.path.append(Path(__file__).parent.parent)



from abstract_reference import abstract_reference
from exceptions import argument_exception
from nomenclature_group_model import nomenclature_group_model
from models.range_model import range_model





class nomenclature_model(abstract_reference):
    __full_name:str=""
    __nom_group:nomenclature_group_model
    __ran_mod:range_model

    
    def __init__(self, name:str, f_NAME:str, nom:nomenclature_group_model,ran:range_model):
        self.name=name 
        self.__id=self.get_id()
        self.full_name=f_NAME

        self.nom_group=nom

        self.ran_mod=ran
        

    

    @property
    def full_name(self):
        return self.__full_name
    
    @property
    def nom_group(self):
        return self.__nom_group
    
    @property
    def ran_mod(self):
        return self.__ran_mod
    
    #полное имя
    @full_name.setter
    def full_name(self,value:str):
        if not isinstance(value,str):
            raise argument_exception("Неверный аргумент!")
        
        value_striped=value.strip()
        
        if value_striped== "" or len(value_striped)>255:
            raise argument_exception("Некорректное значение наименование!")
        
        self.__full_name = value_striped


    #группа номенклатуры
    @nom_group.setter
    def nom_group(self,value: nomenclature_group_model):
        print(type(value))

        if not isinstance(value, nomenclature_group_model):
            raise argument_exception("Неверный аргумент")
        

        self.__nom_group=value



    #еденица измерения
    @ran_mod.setter
    def ran_mod(self,value:range_model):
        if not isinstance(value,range_model):
            raise argument_exception("Неверный аргумент")
        
        self.__ran_mod=value