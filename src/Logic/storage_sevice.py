from pathlib import Path
from datetime import datetime
import os
import json
import sys

sys.path.append(os.path.join(Path(__file__).parent,'src'))

from error_proxy import error_proxy
from pathlib import Path
from storage.storage import storage

from Logic.storage_prototype import storage_prototype
from src.Logic.Reporting.Json_convert.reference_conventor import reference_conventor
from exceptions import argument_exception
from src.Logic.process_factory import process_factory


from src.storage.storage_turn_model import storage_turn_model
from models.nomenclature_model import nomenclature_model
from src.models.range_model import range_model
from src.models.nomenclature_group_model import nomenclature_group_model
from storage.storage_journal_row import storage_journal_row

#PERENESTI I ZAMENIT MAIN

class storage_service:
    __data=[]

    #конструктор
    def __init__ (self,data:list):


        if len(data)==0:
            raise argument_exception("Wrong argument")
        
        self.__data=data


    #получить обооты за период
    def create_turns(self,start_date:datetime,finish_date:datetime)->dict:

        if not isinstance(start_date,datetime) or not isinstance(finish_date,datetime):
            raise argument_exception("Неверный аргумент")
        
        if start_date>finish_date:
            raise argument_exception("Неверно переданы аргументы")
  
        prototype=storage_prototype(self.__data)

        #фильтруем
        transactions=prototype.filter_date(start_date,finish_date)
        
        
        
        #конвентор
        reference=reference_conventor(nomenclature_model,error_proxy,nomenclature_group_model,range_model,storage_journal_row,storage_turn_model)
        

        proces=process_factory()

        data=proces.create(storage.process_turn_key(),transactions.data)

        result={}
        for index,cur_tran in enumerate(data):
            result[index]=reference.convert(cur_tran)


        return result
    
    #получить обороты по номенклатуре
 

    @staticmethod
    def create_response(data:list,app):
        if app is None:
            raise argument_exception()
        json_text = json.dumps( data)  
   
        # Подготовить ответ    
        result = app.response_class(
            response = f"{json_text}",
            status = 200,
            mimetype = "application/json; charset=utf-8"
        )


        return result