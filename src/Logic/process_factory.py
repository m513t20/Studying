

from exceptions import argument_exception
from storage.storage_journal_row import storage_journal_row
from src.storage.storage import storage
from src.storage.storage_factory import storage_factory
from datetime import datetime

class process_factory:

    __maps={}


    def __build_structure(self):
        self.__maps[storage.process_turn_key()]=process_factory.process_storage_turn

    #просеять по временному промежутку
    @staticmethod
    def __seed_on_period(journal:list,start:datetime,finish:datetime):
        result=[]
        for cur_line in journal:
            if cur_line.period>=start and cur_line.period<=finish:
                result.append(cur_line)
        return result


    @staticmethod
    def process_storage_turn(journal:list):
        if not isinstance(journal,list) :
            raise argument_exception("Неверный аргумент")
        
        if len(journal)==0:
            raise argument_exception("пустой массив")
        
        if not isinstance(journal[0],storage_journal_row):
            raise argument_exception("Неверный массив")
        

        result={}
        
        for cur_line in journal:
            #айди склада и имя номенклатуры, для того чтобы рассортировать строки складского журнала
            key=cur_line.nomenclature.name+' '+str(cur_line.storage_id)
            keys=list(result.keys())

            koef=1-2*( cur_line.operation_type=="delete")
            

            if key in keys:
                result[key].amount+=cur_line.amount*koef
            else:
                
                #в turnmodel хранятся данные о складе, а также  количестве,  типе и единицах измерения номенклатуры
                result[key]=storage_factory.create_turn(cur_line.storage_id,cur_line.amount*koef,cur_line.nomenclature,cur_line.nomenclature.ran_mod)

        #по требованию задания мы возвращаем список, поэтому list(result.values())
        return list(result.values())
    


    def create(self,key:str,journal:list,start:datetime,finish:datetime):
        if not isinstance(key,str):
            raise argument_exception("Неверный аргумент")
        
        #получаем просеяный массив 
        seeded=self.__seed_on_period(journal,start,finish)


        operation=self.__maps[key]



        return operation(seeded)



    def __init__(self) -> None:
        self.__build_structure()

        

        
