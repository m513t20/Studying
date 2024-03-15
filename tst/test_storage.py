from pathlib import Path
import os
import sys
import json

sys.path.append(os.path.join(Path(__file__).parent.parent,'src'))


from datetime import datetime
from src.storage.storage_journal_row import storage_journal_row
from src.storage.storage_model import storage_model
from src.storage.storage_journal_transaction import storage_journal_transaction
from src.models.nomenclature_model import nomenclature_model


import unittest

class test_storage(unittest.TestCase):


    #создать склад
    def test_check_storage_model(self):
        #подготовка
        loc='    Улица малых богов 123       '



        #действие
        item=storage_model(loc)


        #проверка
        print(item.id)
        assert item.location=='Улица малых богов 123'
        assert item.id is not None


    #создать действие на складе
    def test_check_journal_transaction(self):
        #подготовка
        nom=nomenclature_model()

        #действие
        item=storage_journal_transaction(True,nom,datetime.now())

        #проверка
        assert item.id is not None
        assert item.type=="add"
        assert item.period.month    ==datetime.now().month


    def test_build_journal_row(self):
        #подготовка
        nom=nomenclature_model()
        item1=storage_journal_transaction(True,nom,datetime(2014,12,1))
        loc='    Улица малых богов 123       '
        item2=storage_model(loc)


        #действие
        item3=storage_journal_row(item2,item1)



        #проверка
        assert item3.location==item2.location
        assert item3.operation_id==item1.id
        assert item3.storage_id==item2.id
        assert item3.period==item1.period
        assert item3.operation_type==item1.type




    