


from src.storage.storage_turn_model import storage_turn_model
from exceptions import argument_exception
from src.storage.storage_journal_row import storage_journal_row
from src.storage.storage import storage

class process_factory:

    __maps={}


    def __build_structure(self):
        self.__maps[storage.process_turn_key()]=self.process_storage_turn



    def process_storage_turn(self,journal:list):
        if not isinstance(journal,list) :
            raise argument_exception("Неверный аргумент")
        
        if len(journal)==0:
            raise argument_exception("пустой массив")
        
        if not isinstance(journal[0],storage_journal_row):
            raise argument_exception("Неверный массив")
        

        result=[]
        
        for cur_line in journal:
            result.append(storage_turn_model(storage_journal_row.st))



        

        

