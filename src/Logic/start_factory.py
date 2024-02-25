from pathlib import Path
import os
import sys

sys.path.append(os.path.join(Path(__file__).parent.parent,'models'))


from models.range_model import create_gramm,create_kilogram,create_litr,create_mililitr,create_shtuka
from models.reciepe_model import reciepe_model
from storage.storage import storage
from exceptions import argument_exception
from models.nomenclature_model import nomenclature_model,nomenclature_group_model,range_model
from settings import settings

class start_factory:

    __options:settings=None
    __storage:storage=None
    
    def __init__(self,options:settings,stor:storage=None):
        self.__options=options
        self.__storage=stor




    def __build(self,nom:list):
        if self.__storage==None:
            self.__storage=storage()

        nom=start_factory.create_nomenclature()
        #добавляем в data
        self.__storage.data[storage.nomenclature_key()]=nom[0]
        self.__storage.data[storage.unit_key()]=nom[1]      
        self.__storage.data[storage.group_key()]=nom[2]


    @property
    def storage(self):
        return self.__storage

    @staticmethod
    def create_nomenclature():
        #создаём группы
        group=nomenclature_group_model.create_group()
        group_meat=nomenclature_group_model.create_group_meat()
        group_eggs=nomenclature_group_model.create_group_eggs()
        group_vegs=nomenclature_group_model.create_group_vegs()

        Output=[]

        #создаём еденицы
        kg=create_kilogram()
        gr=create_gramm()
        ml=create_mililitr()
        l=create_litr()
        sht=create_shtuka()


        #создаём рецепты


        #добавляем в номенклатуру
        Output.append(nomenclature_model('Pshenichnaya muka','Pshenichnaya muka',group,kg))
        Output.append(nomenclature_model('sugar','sugar',group,kg))
        Output.append(nomenclature_model('maslo','slivochnoe maslo',group,gr))
        Output.append(nomenclature_model('eggs','eggs',group_eggs,sht))
        Output.append(nomenclature_model('Vanilin','Vanilin',group,gr))
        Output.append(nomenclature_model('Yaichyi belok','yaichyi belok',group_eggs,sht))
        Output.append(nomenclature_model('Saharnaya pudra','saharnaya pudra',group,kg))
        Output.append(nomenclature_model('Koritsa','Koritsa',group,gr))
        Output.append(nomenclature_model('Kakao','Kakao',group,gr))
        Output.append(nomenclature_model("chiken file","chicken file",group_meat,kg))
        Output.append(nomenclature_model("Romano salad","Romano salad",group_vegs, gr))
        Output.append(nomenclature_model("Suahri","Suhari",group,kg))


        return [Output,[kg,gr,l,ml,sht],[group,group_eggs,group_vegs,group_meat]]

    def create_receipts(self):
        pass

    def create(self):
        if self.__options.is_first_start:
            self.__options.is_first_start='False'
            ret=start_factory.create_nomenclature()
            self.__build(ret)
            return ret
        
        else:
            items=[]
            return items


    @property
    def options(self):
        return self.__options
    
    @options.setter
    def options(self,value):
        if not isinstance(value,settings):
            raise argument_exception("Неверный аргумент")
        
        self.__options=value

