from pathlib import Path
import os
import sys

sys.path.append(os.path.join(Path(__file__).parent.parent,'models'))


from models.range_model import range_model
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
        self.__storage.data[storage.reciepe_key()]=nom[3]


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
        kg=range_model.create_kilogram()
        gr=range_model.create_gramm()
        ml=range_model.create_mililitr()
        l=range_model.create_litr()
        sht=range_model.create_shtuka()


        #создаём рецепты через фабричный метод в reciepe_model
        draniki=reciepe_model.create_draniki()
        


        #добавляем в номенклатуру
        Output.append(nomenclature_model('Пшеничная мука','Пшеничная мука',group,kg))
        Output.append(nomenclature_model('сахар','сахар',group,kg))
        Output.append(nomenclature_model('масло','масло',group,gr))
        Output.append(nomenclature_model('яйца','яйца',group_eggs,sht))
        Output.append(nomenclature_model('ванилин','ванилин',group,gr))
        Output.append(nomenclature_model('яичный белок','яичный белок',group_eggs,sht))
        Output.append(nomenclature_model('сахарная пудра','сахарная пудра',group,kg))
        Output.append(nomenclature_model('корица','корица',group,gr))
        Output.append(nomenclature_model('какао','какао',group,gr))
        Output.append(nomenclature_model("куринное филе","куринное филе",group_meat,kg))
        Output.append(nomenclature_model("салат романо","салат романо",group_vegs, gr))
        Output.append(nomenclature_model("сухари","сухари",group,kg))
        Output.append(nomenclature_model('картофель','картофель',group,sht))
        Output.append(nomenclature_model('лук репчатый','лук репчатый',group,sht))
        Output.append(nomenclature_model('соль','соль',group,gr))

        #создаём пропорции для рецептов
        draniki_prop={Output[2]:'2 ст л',Output[0]:"2 ст л",Output[12]:"7 шт",Output[13]:"1 шт",Output[14]:"2 г"}

        draniki.ingridient_proportions=draniki_prop

        return [Output,[kg,gr,l,ml,sht],[group,group_eggs,group_vegs,group_meat],[draniki]]

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

