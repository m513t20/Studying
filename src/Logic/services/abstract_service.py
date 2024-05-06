from pathlib import Path
from datetime import datetime
import os
import json
import uuid
import sys

sys.path.append(os.path.join(Path(__file__).parent,'src'))

from error_proxy import error_proxy
from pathlib import Path
from storage.storage import storage
from settings import settings
from Logic.storage_prototype import storage_prototype
from src.Logic.Reporting.Json_convert.reference_conventor import reference_conventor
from exceptions import argument_exception
from src.Logic.process_factory import process_factory

#для референсов
from src.storage.storage_turn_model import storage_turn_model
from models.nomenclature_model import nomenclature_model
from src.models.range_model import range_model
from src.models.nomenclature_group_model import nomenclature_group_model
from models.reciepe_model import reciepe_model
from src.storage.storage_factory import storage_factory
from storage.storage_journal_row import storage_journal_row
from src.storage.storage_journal_transaction import storage_journal_transaction


from abc import ABC


class abstract_sevice(ABC):

    __data=[]
    #конструктор
    def __init__ (self,data:list):


        if len(data)==0:
            raise argument_exception("Wrong argument")
        
        self.__data=data



    def handle_event(self,handle_type:str,args):
        if not isinstance(handle_type,str):
            raise argument_exception("Неверный тип аргумента")
        
        pass