from pathlib import Path
import os
import sys
import json
from datetime import datetime

sys.path.append(os.path.join(Path(__file__).parent.parent,'src'))


from settings import settings
from settings_manager import  settings_manager
from datetime import datetime
from storage.storage import storage
from Logic.start_factory import start_factory
from src.Logic.services.storage_sevice import storage_service
from src.Logic.storage_observer import storage_observer
from src.models.event_type import event_type

import unittest


class test_settings(unittest.TestCase):
    
    def test_check_create_manager(self):
        # Подготовка
        manager1 = settings_manager()
        manager2 = settings_manager()
        
        # Действие
        
        # Проверки
        print(str(manager1.number))
        print(str(manager2.number))
    
        assert manager1.number == manager2.number
    
    #
    # Провеиить корректность заполнения поля first_name
    #
    def test_check_first_name(self):
        # Подготовка
        item = settings()
        
        # Действие
        item.first_name = "a  "
        
        # Проверка
        assert item.first_name == "a"


    #INN проверка 
    def test_INN_check(self):
        item=settings()

        item.INN="    000000123456          "

        assert item.INN=="000000123456"

    #account проверка
    def test_account_check(self):
        item=settings()

        item.account="       12345678901"

        assert item.account=="12345678901"

    #коррепсондетский счет проверка
    def test_cor_account_check(self):
        item=settings()

        item.correspond_account="        12345678901                "

        assert item.correspond_account=="12345678901"

    #BIK проверка
    def test_BIK_check(self):
        item=settings()

        item.BIK="       123456789        "

        assert item.BIK=="123456789"

    #name проверка 
    def test_name_chekc(self):
        item=settings()

        item.name="abcx asd       "

        assert item.name=="abcx asd"

    #проверка типа собственности
    def test_property_type_check(self):
        item=settings()

        item.property_type="'000'   "

        assert item.property_type=="'000'"


    def test_block_period_check(self):
        #подготовка
        item=settings()
        #дкйствие
        item.block_period="2024-1-1"
        #проверка
        print(datetime(2024,4,5),item.block_period)
        assert item.block_period==datetime(2024,1,1)






    #Проверки с пробелами
    def test_INN_check_spaces(self):
        item=settings()

        item.INN="    000 00 0123 456          "

        assert item.INN=="000000123456"

    #account проверка с пробелами
    def test_account_check_spaces(self):
        item=settings()

        item.account="       1234 56   7 8 90 1"

        assert item.account=="12345678901"

    #коррепсондетский счет проверка с пробелами
    def test_cor_account_chec_spaces(self):
        item=settings()

        item.correspond_account="        12 34 56 78 901                "

        assert item.correspond_account=="12345678901"

    #BIK проверка с пробелами
    def test_BIK_check_spaces(self):
        item=settings()

        item.BIK="       1234 56 78 9        "

        assert item.BIK=="123456789"













    
        
    def test_check_manager_convert(self):
        # Подготовка
        manager = settings_manager()

        #Действия
        A=manager.open("settings.json")
         
        
        
        # Проверка 
        assert A==True

   

        
    def test_check_open_settings(self):
        # Подготовка
        manager = settings_manager()
        
        # Действие
        result = manager.open()
        
        # Проверка
        print(manager.data)
        
        assert result==True
        

    #Загрузка настроек с другой папки и с другим названием
    def test_check_open_other_dir_settings(self):
        #подготовка
        manager=settings_manager()
        #адрес
        address=os.path.join(Path(__file__).parent.parent,'Jsons')

        print(address)


        result=manager.open("Tester.json",address)
        assert result==True


    #тест на сохранение (сохранение считается правильным, при прохождении остальных автотестов)
    def test_check_save_settings(self):
        #подготовка
        manager=settings_manager()
        #адрес
        address=os.path.join(Path(__file__).parent.parent,'Jsons')
        result=manager.open("Tester.json",address)


        #действие

        dic=manager.save_settings()

           
        #проверка
        assert dic==True




    #тест наблюдатель
    def test_check_observer_event(self):
        #Подготовка
        unit=settings_manager()
        address=os.path.join(Path(__file__).parent.parent,'Jsons')
        unit.open('Tester.json',address)
        factory=start_factory(unit.settings)
        factory.create()
        key=storage.b_turn_key()
        transactions_data_control = factory.storage.data[ key ]

        #действие         
        unit.settings.block_period="2024-5-5"
        transactions_data = factory.storage.data[ key ]



        assert len(transactions_data_control)!=len(transactions_data)


