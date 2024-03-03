from pathlib import Path
import os
import sys

sys.path.append(Path(__file__).parent.parent)

import uuid
from abc import ABC
from settings import settings
from exceptions import argument_exception
from error_proxy import error_proxy
from Logic.start_factory import start_factory,range_model,nomenclature_group_model,nomenclature_model,reciepe_model
from storage.storage import storage

#range model, nomenclatur model, nomenclature group model v str csv 
class abstract_reporting(ABC):
    #инкапсуляция настроек
    __settings=None
    
    #типы перерабатываемой номенклатуры
    __types={storage.unit_key():range_model(),storage.reciepe_key():reciepe_model(),storage.nomenclature_key():nomenclature_model(),storage.group_key():nomenclature_group_model()}


    #Данные из start_factory
    __data={}

    @property
    def data(self):
        return self.__data


    #сеттер
    @data.setter
    def data(self,value:dict):
        if not isinstance(value,dict):
            raise argument_exception("Неверный аргумент")
        
        self.__data=value


    def __init__(self,data_examp:list,settings_examp:settings):
        self.data=data_examp
        self.hidden_settings=settings_examp



    @property
    def hidden_settings(self):
        return self.__settings
    

    @hidden_settings.setter
    def hidden_settings(self,value:settings):
        if not isinstance(value,settings):
            raise argument_exception ("Неверный аргумент")
        
        self.__settings=value



    #возвращает ключи для отчёта
    def create(self,value:str):
        if not isinstance(value,str):
            raise argument_exception("Неверный аргумент")

        fields = list(filter(lambda x: not x.startswith("_") and not x.startswith('create_'), dir(self.__types[value].__class__)))
        print(fields)

        return fields
    


