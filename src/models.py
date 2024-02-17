from abstract_reference import abstract_reference
from exceptions import argument_exception
from settings import settings
import uuid

class range_model(abstract_reference):
    __recount_ratio:int=1 
    __base_range=None
    

    def __init__(self, name:str="untituled", ratio:int=1, base=None):
        self.name=name 

        self.recount_ratio=ratio 

        self.__id=self.get_id()

        if base:
            self.base_range=base 


    @property 
    def recount_ratio(self):
        return self.__recount_ratio
    
    @recount_ratio.setter
    def recount_ratio(self,value):
        
        if not isinstance(value,int):
            raise argument_exception("некорректный тип данных!")
        
        if value<=0:
            raise argument_exception("некорректный аргумент")

        self.__recount_ratio=value        

    @property 
    def base_range(self):
        return self.__base_range
    
    @base_range.setter
    def base_range(self,value):
        if not isinstance(value,range_model):
            raise argument_exception("некорректный аргумент")
        
        self.__base_range=value


class organisation_model(abstract_reference):
    __BIK=""
    __INN=""
    __account=""
    __property_type=""
    

    def __init__(self,value:settings=None):
        if not isinstance(value,settings):
            raise argument_exception("Неверный аргумент")
        
        settings_names=dir(settings)
        self.__id=self.get_id()
        #берем общие атрибуты с property и передаём их классу
        for pr_name in (dir(self)):
            if isinstance(getattr(organisation_model,pr_name),property) and (pr_name in settings_names):
                setattr(self,pr_name,getattr(value,pr_name))
                print (getattr(self,pr_name))


    
    @property
    def BIK(self):
        return self.__BIK

    @property
    def INN(self):
        return self.__INN
    
    @property
    def account(self):
        return self.__account

    @property 
    def property_type(self):
        return self.__property_type
        

    

    @BIK.setter
    def BIK(self,value:str):
        value_stripped=value.strip().replace(' ','')
        #Состоит ли из символов (value у нас str на случай незначащих нулей в начале числа)
        if not isinstance(value,str) or not(value_stripped.isdigit()):
            raise  argument_exception("Некорректный аргумент")
        

        #проверка на длинну
        if len(value_stripped)!=9:
            raise argument_exception("Некорректная длинна")
            
        self.__BIK=value_stripped


    @INN.setter
    def INN(self,value: str):
        #value_stripped=value.replace(' ','')
        value_stripped=value.strip().replace(' ','')
        #Состоит ли из символов (value у нас str на случай незначащих нулей в начале числа)
        if not isinstance(value,str) or not(value_stripped.isdigit()):
            raise  argument_exception("Некорректный аргумент")
        

        #проверка на длинну
        if len(value_stripped)!=12:
            raise argument_exception("Некорректная длинна")
            
        self.__INN=value_stripped

    @account.setter
    def account(self,value:str):
        #делаем через replace на случай введения с пробелами
        value_stripped=value.strip().replace(' ','')
        #Состоит ли из символов (value у нас str на случай незначащих нулей в начале числа)
        if not isinstance(value,str) or not(value_stripped.isdigit()):
            raise  argument_exception("Некорректный аргумент")
        

        #проверка на длинну
        if len(value_stripped)!=11:
            raise argument_exception("Некорректная длинна")
            
        self.__account=value_stripped



    @property_type.setter
    def property_type(self,value:str):
        value_stripped=value.strip()
        if not isinstance(value,str):
            raise  argument_exception("Некорректный аргумент")
        

        #проверка на длинну
        if len(value_stripped)!=5:
            raise argument_exception("Некорректная длинна")
            
        self.__property_type=value_stripped


class nomenclature_group(abstract_reference):
    __gr=""

class nomenclature(abstract_reference):
    __full_name:str=""
    __nom_group:nomenclature_group
    __ran_mod:range_model

    
    def __init__(self, name:str, f_NAME:str, nom:nomenclature_group,ran:range_model):
        self.name=name 
        self.__id=self.get_id()
        self.full_name=f_NAME
        self.nom_group=nom
        self.ran_mod=ran
        

    

    @property
    def full_name(self):
        return self.__full_name
    
    @property
    def nom_group(self):
        return self.__nom_group
    
    @property
    def ran_mod(self):
        return self.__ran_mod
    

    @full_name.setter
    def full_name(self,value:str):
        if not isinstance(value,str):
            raise argument_exception("Неверный аргумент!")
        
        value_striped=value.strip()
        
        if value_striped== "" or len(value_striped)>255:
            raise argument_exception("Некорректное значение наименование!")
        
        self.__name = value_striped

    @nom_group.setter
    def nom_group(self,value: nomenclature_group):
        if not isinstance(value, nomenclature_group):
            raise argument_exception("Неверный аргумент")
        
        self.__nom_group=value

    @ran_mod.setter
    def ran_mod(self,value:range_model):
        if not isinstance(value,range_model):
            raise argument_exception("Неверный аргумент")
        
        self.__ran_mod=value