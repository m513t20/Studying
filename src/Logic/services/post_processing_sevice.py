from pathlib import Path
import os
import uuid
import sys

sys.path.append(os.path.join(Path(__file__).parent,'src'))

from pathlib import Path
from storage.storage import storage

from exceptions import argument_exception
from src.Logic.storage_observer import storage_observer
from src.models.event_type import event_type
from src.Logic.services.abstract_service import abstract_sevice

class post_processing_service(abstract_sevice):

    __nomenclature=None
    __storage=None
    



    def __init__(self):
        self.__storage=storage()


    #тк веб метод удаления у нас требует именно айди номенклатуры, с id
    @property
    def nomenclature_id(self):
        return self.__nomenclature
    

    @nomenclature_id.setter
    def nomenclature_id(self,nom_id:uuid.UUID):
        if not isinstance(nom_id,uuid.UUID):
            raise argument_exception("неверный тип аргумента")
        self.__nomenclature=nom_id
        #add observer
        storage_observer.observers.append(self)


    def handle_event(self, handle_type: str,*args):
        super().handle_event(handle_type,args)

        if handle_type==event_type.deleted_nomenclature() and args[0]==str(self.nomenclature_id):
            self.clear_reciepe()
            self.clear_journal()

    #очищаем рецепт
    def clear_reciepe(self):

        key=storage.reciepe_key()
        for index,cur_rec in enumerate(self.__storage.data[key]):
            #структура ингридиентов у нас {айди_номенклатуры:{количество:единица измерения}}
            for cur_id in list(cur_rec.ingridient_proportions.keys()):
                #если совали айди, удалаем из словаря строку и сохраняем его в модели рецепта
                if self.__nomenclature==cur_id:
                    res=cur_rec.ingridient_proportions
                    res.pop(self.__nomenclature )
                    storage().data[key][index].ingridient_proportions=res 
        
    #очищаем журнал
    def clear_journal(self):
        key=storage.journal_key()
        res=[]
        #собираем второй массив без операций над удалённой номенклатурой
        for cur_line in (self.__storage.data[key]):
            if cur_line.nomenclature.id!=self.__nomenclature:
                res.append(cur_line)

        self.__storage.data[key]=res

        #перерасчитываем оборот за блок период
        storage_observer.raise_event(event_type.changed_block_period())