from pathlib import Path
import os
import sys

sys.path.append(os.path.join(Path(__file__).parent.parent,'src'))

from storage.storage import storage
from Logic.start_factory import start_factory
from models.range_model import range_model
from src.settings_manager import settings_manager


import unittest


class test_factory(unittest.TestCase):
    #проверка на первый старт 
    def test_check_first_start(self):

        #preparation
        unit=settings_manager()
        address=os.path.join(Path(__file__).parent.parent,'Jsons')
        unit.open('Tester.json',address)
        item=start_factory(unit.settings)

        #action 
        
        check=item.create()

        #check
        if unit.settings.is_first_start==True:

            assert len(check)>0
            return
        
        
        #assert  len(check)==0
        assert not item.storage is None 
        print(item.storage.data)
        assert storage().nomenclature_key() in item.storage.data
        assert storage().unit_key()in item.storage.data
        assert storage().group_key() in item.storage.data

    #проверка на не первый старт
    def test_check_not_first_start(self):
        #preparation
        unit=settings_manager()
        address=os.path.join(Path(__file__).parent.parent,'Jsons')
        unit.open('Tester_not.json',address)
        item=start_factory(unit.settings)


        check=item.create()



        assert item.storage is None
        assert len(check)==0