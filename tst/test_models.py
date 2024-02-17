from pathlib import Path
import os
import sys

sys.path.append(os.path.join(Path(__file__).parent.parent,'src'))


from models import range_model,organisation_model,nomenclature,nomenclature_group
from settings import settings
from settings_manager import  settings_manager


import unittest


class test_settings(unittest.TestCase):

    def test_abstract_name_length(self):
        #подготовка
        k="a"*51
        
        #действие
        try: 
            item=range_model(k)

        except Exception as ex:
            assert True==True
            return

        assert False==True
    

    def test_inheritance_abstract(self):
        #подготовка
        item=range_model("  name_example    ")

        #действие
        
        
        #проверка
        assert item.name=="name_example"



    #range model tests
        
    def test_range_model_name(self):
        #подготовка
        item=range_model("  name_example    ",1)

        #действие
        
        
        #проверка
        assert item.name=="name_example"


    def test_range_model_base(self):
        #подготовка
        item=range_model(" Грамм ",1)


        #действие
        item2=range_model("Килограмм  ",1000,item)
        
        #проверка
        assert item2.base_range.name=="Грамм"


    def test_range_model_recount(self):
        #подготовка
        item=range_model(" Грамм ",1)


        #действие
        item2=range_model("Килограмм  ",1000,item)
        
        #проверка
        assert item2.recount_ratio*5==5000

    def test_range_model_recount_two_sons(self):
        #подготовка
        item=range_model(" Грамм ",1)


        #действие
        item2=range_model("Килограмм  ",1000,item)
        item3=range_model("Тонна ",1000000,item)
        #проверка
        assert item2.recount_ratio*5==item3.recount_ratio/200




    #organisation и проверки загрузок
    def test_organisation_model_import_abort(self):
        #подготовка

        #действие 
        try:
            company=organisation_model("aweaw")
        except Exception as ex:
            assert True==True
            return

        assert False==True


        #проверка    
    
    def test_organisation_model_import_BIK(self):
        #подготовка
        manager=settings_manager()
        manager.open("settings.json")



        #действие
        company = organisation_model(manager.settings)

        
        #проверка
        assert company.BIK==manager.settings.BIK

    def test_organisation_model_import_INN(self):
        #подготовка
        manager=settings_manager()
        manager.open("settings.json")



        #действие
        company = organisation_model(manager.settings)

        
        #проверка
        assert company.INN==manager.settings.INN

    def test_organisation_model_import_account(self):
        #подготовка
        manager=settings_manager()
        manager.open("settings.json")



        #действие
        company = organisation_model(manager.settings)

        
        #проверка
        assert company.account==manager.settings.account

    def test_organisation_model_import_property_type(self):
        #подготовка
        manager=settings_manager()
        manager.open("settings.json")



        #действие
        company = organisation_model(manager.settings)

        
        #проверка
        assert company.property_type==manager.settings.property_type





    #группы номенклатуры
    def test_nomenclature_atributes(self):
        #подготовка
        item=nomenclature_group("  name_example    ")

        #действие
        
        
        #проверка
        assert item.name=="name_example"



    #номенклатура
    def test_nomenclature(self):
        #подготвка 
        item1=nomenclature_group("some_name")
        item2=range_model("model_name")
        

        #действие
        item3=nomenclature("name_nome","f"*100,item1,item2)
        #проверка
        assert item3.nom_group.name==item1.name and item2.name==item3.ran_mod.name

    def test_nomenclature_length(self):
        #подготвка 
        item1=nomenclature_group("some_name")
        item2=range_model("model_name")
        

        #действие
        
        try: 
            item3=nomenclature("name_nome","f"*256,item1,item2)

        except Exception as ex:
            assert True==True
            return

        assert False==True

            