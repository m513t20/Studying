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

    def create_id_turns(self,id:uuid.UUID):
        if not isinstance(id,uuid.UUID):
            raise argument_exception("Неверный аргумент")
        
        prototype=storage_prototype(self.__data)

        #фильтруем
        transactions=prototype.filter_nom_id(id)

        #конвентор
        reference=reference_conventor(nomenclature_model,error_proxy,nomenclature_group_model,range_model,storage_journal_row,storage_turn_model)
        
        

        proces=process_factory()

        data=proces.create(storage.process_turn_key(),transactions.data)

        result={}
        for index,cur_tran in enumerate(data):
            result[index]=reference.convert(cur_tran)


        return result
    
    def create_reciepe_transactions(self,reciepe:reciepe_model):
        if not isinstance(reciepe,reciepe_model):
            raise argument_exception("Неверный аргумент")
        
        prototype=storage_prototype(self.__data)

        #фильтруем
        transactions=prototype.filter_reciepe(reciepe)

        #оборот
        proces=process_factory()
        turn=proces.create(storage.process_turn_key(),transactions.data)


        transactions_list=[]
        #пробегаемся по обороту
        for cur_ing in list(reciepe.ingridient_proportions.keys()):
            #флаг для проверки на присутствие на складах
            flag=True
            for cur_nom in turn:

                if cur_ing.id==cur_nom.nomenclature.id:

                    amount=list(reciepe.ingridient_proportions[cur_ing].keys())[0]

                    #пересчитываем единицы измерения
                    if cur_ing.ran_mod!=cur_nom.nomenclature.ran_mod:
                        amount*=cur_ing.ran_mod.recount_ratio


                    transactions_list.append(storage_factory.create_transaction(False,cur_ing,amount,datetime.now()))

                    flag=False 
                    break 
            if not flag:
                transactions_list.append(f"{cur_nom.nomenclature.id} not found")


        reference=reference_conventor(nomenclature_model,error_proxy,nomenclature_group_model,range_model,storage_journal_row,storage_turn_model,storage_journal_transaction)
        result={}
        for index,cur_tran in enumerate(transactions_list):
            if isinstance(cur_tran,str):
                result[index]=cur_tran
                continue

            result[index]=reference.convert(cur_tran)



        return result
        






        

    @staticmethod
    def create_response(data:dict,app):
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