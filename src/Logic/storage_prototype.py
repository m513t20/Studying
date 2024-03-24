
from error_proxy import error_proxy
from datetime import datetime
from models.nomenclature_model import nomenclature_model

class storage_prototype(error_proxy):
    __data=[]
    
    @property
    def data(self):
        return self.__data


    def __init__(self,data:list) -> None:
        if len(data)<=0:
            self.error_text="Wrong argument"
        self.__data=data





    def filter_date(self,start:datetime,finish:datetime):
        if len(self.__data)<=0:
            self.error_text="Wrong argument"


        if start>finish:
            self.error_text="Incorrect period"

        if self.if_error:
            return self.__data
        
        result=[]
        for cur_line in self.__data:
            if cur_line.period>=start and cur_line.period<=finish:
                result.append(cur_line)


        return storage_prototype(result)



    def filter_nom(self,nom:nomenclature_model):
        if not isinstance(nom,nomenclature_model):
            self.error_text="Wrong argument"



        if self.if_error:
            return self.__data
        
        result=[]
        for cur_line in self.__data:
            if cur_line.nomenclature==nom:
                result.append(cur_line)


        return storage_prototype(result)
