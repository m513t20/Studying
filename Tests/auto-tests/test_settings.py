from settings import settings
from settings_manager import  settings_manager
from pathlib import Path
import os
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
        address=os.path.join(Path(__file__).parent.parent.parent,'Jsons')
        print(address)


        result=manager.open("Tester.json",address)
        assert result==True
                
        
        