


from src.storage.storage_turn_model import storage_turn_model
from exceptions import argument_exception
from storage.storage_journal_row import storage_journal_row
from src.storage.storage import storage
from datetime import datetime

class process_factory:

    __maps={}


    def __build_structure(self):
        self.__maps[storage.process_turn_key()]=process_factory.process_storage_turn


    @staticmethod
    def process_storage_turn(journal:list,start:datetime,finish:datetime):
        if not isinstance(journal,list) :
            raise argument_exception("Неверный аргумент")
        
        if len(journal)==0:
            raise argument_exception("пустой массив")
        
        if not isinstance(journal[0],storage_journal_row):
            raise argument_exception("Неверный массив")
        

        result={}
        
        for cur_line in journal:

            if cur_line.period<=finish and cur_line.period>=start:
                key=cur_line.nomenclature.name+' '+str(cur_line.storage_id)
                keys=list(result.keys())
                koef=1-2*( cur_line.operation_type=="delete")
                storage_turn_model(cur_line.storage_id,cur_line.amount*koef,cur_line.nomenclature,cur_line.nomenclature.ran_mod)

                if key in keys:
                    result[key].amount+=cur_line.amount*koef
                else:
                    result[key]=storage_turn_model(cur_line.storage_id,cur_line.amount*koef,cur_line.nomenclature,cur_line.nomenclature.ran_mod)


        return list(result.values())

    def create(self,key:str,journal:list,start:datetime,finish:datetime):
        if not isinstance(key,str):
            raise argument_exception("Неверный аргумент")
        operation=self.__maps[key]

        return operation(journal,start,finish)



    def __init__(self) -> None:
        self.__build_structure()

        

        

