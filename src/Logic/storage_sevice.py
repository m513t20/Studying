from pathlib import Path
from datetime import datetime
import os
import json
import sys

sys.path.append(os.path.join(Path(__file__).parent,'src'))

from error_proxy import error_proxy
from pathlib import Path
from storage.storage import storage
from Logic.start_factory import start_factory
from models.range_model import range_model
from src.settings_manager import settings_manager
from Logic.report_factory import report_factory
from Logic.storage_prototype import storage_prototype
from storage.storage_factory import storage_factory
from src.Logic.Reporting.Json_convert.reference_conventor import reference_conventor
from Logic.process_factory import process_factory
from exceptions import argument_exception

#PERENESTI I ZAMENIT MAIN

class storage_service:
    __data=[]

    __convert:reference_conventor=None 

    __process:process_factory=None


    def __init__ (self,data:list):
        if len(data==0):
            raise argument_exception("Wrong argument")
        
        self.__data=data

    def create_turns(self,start_date:datetime,finish_date:datetime)->dict:
  
        prototype=storage_prototype(self.__data)

        transactions=prototype.filter_date(start_date,finish_date)
        #DOBAVIT TIPY
        process=reference_conventor()
        #UBRAT

        result={}
        for index,cur_tran in enumerate(transactions.data):
            result[index]=process.convert(cur_tran)


        return result

    def create_respomse(self,data:dict,app):
        if app is None:
            raise argument_exception()
        

        data=json.dumps(some_data_from_class)


        #DOBAVLAYEM V 