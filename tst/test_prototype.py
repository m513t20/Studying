from pathlib import Path
import os
import sys
import json

sys.path.append(os.path.join(Path(__file__).parent.parent,'src'))

from settings_manager import settings_manager
from storage.storage import storage
from Logic.start_factory import start_factory
from datetime import datetime
from src.Logic.process_factory import process_factory


from src.Logic.storage_prototype import storage_prototype
import unittest


class test_prototype(unittest.TestCase):

    #фильтер по дате
    def test_filter_date(self):
        #Подготовка
        unit=settings_manager()
        address=os.path.join(Path(__file__).parent.parent,'Jsons')
        unit.open('Tester.json',address)
        factory=start_factory(unit.settings)

        factory.create()
        key=storage.journal_key()

        prot=storage_prototype(factory.storage.data[key])


        #действие
        result=storage_prototype.filter_date(prot,datetime(2023,1,1),datetime(2024,12,31))



        #проверка 
        assert isinstance(result,storage_prototype)
        assert len(result.data)>0
        assert not result.if_error

    #фильтер по номенклатуре
    def test_filter_nom(self):
        #Подготовка
        unit=settings_manager()
        address=os.path.join(Path(__file__).parent.parent,'Jsons')
        unit.open('Tester.json',address)
        factory=start_factory(unit.settings)

        factory.create()
        key=storage.journal_key()

        prot=storage_prototype(factory.storage.data[key])


        #Действие
        result=storage_prototype.filter_nom(prot,factory.storage.data[key][0].nomenclature)


        #проверка
        assert isinstance(result,storage_prototype)
        assert len(result.data)>0
        assert len(result.data)==5
        assert not result.if_error


    #фильтер по двум или больше условиям
    def test_filter_nom_and_date(self):
        #Подготовка
        unit=settings_manager()
        address=os.path.join(Path(__file__).parent.parent,'Jsons')
        unit.open('Tester.json',address)
        factory=start_factory(unit.settings)

        factory.create()
        key=storage.journal_key()

        prot=storage_prototype(factory.storage.data[key])


        #действие
        result=storage_prototype.filter_nom(prot,factory.storage.data[key][0].nomenclature)
        result=storage_prototype.filter_date(result,datetime(2023,3,1),datetime(2024,12,31))

        result_chek1=storage_prototype.filter_nom(prot,factory.storage.data[key][0].nomenclature)
        result_chek2=storage_prototype.filter_date(prot,datetime(2023,3,1),datetime(2024,12,31))


        #проверка
        assert isinstance(result,storage_prototype)
        assert len(result.data)>0
        assert len(result.data)<len(result_chek1.data) or len(result.data)<len(result_chek2.data)
        assert not result.if_error


    #фильтер по айди номенклатуры
    def test_filter_nom_id(self):
        #Подготовка
        unit=settings_manager()
        address=os.path.join(Path(__file__).parent.parent,'Jsons')
        unit.open('Tester.json',address)
        factory=start_factory(unit.settings)

        factory.create()
        key=storage.journal_key()

        prot=storage_prototype(factory.storage.data[key])


        #действие
        result=storage_prototype.filter_nom_id(prot,factory.storage.data[key][0].nomenclature.id)

        print(factory.storage.data[key][0].nomenclature.id)

        #проверка
        assert isinstance(result,storage_prototype)
        assert len(result.data)>0
        assert len(result.data)==5
        assert not result.if_error

    #фильтрация по рецепту
    def test_filter_reciepe(self):
        #Подготовка
        unit=settings_manager()
        address=os.path.join(Path(__file__).parent.parent,'Jsons')
        unit.open('Tester.json',address)
        factory=start_factory(unit.settings)

        factory.create()
        key=storage.journal_key()

        prot=storage_prototype(factory.storage.data[key])


        #действие
        result=storage_prototype.filter_reciepe(prot,factory.storage.data[storage.reciepe_key()][0])

        for i in result.data:
            print(i.nomenclature.id)

        #проверка
        assert isinstance(result,storage_prototype)
        assert len(result.data)>0
        assert not result.if_error