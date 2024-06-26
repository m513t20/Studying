from exceptions import argument_exception, operation_exception
from datetime import datetime
from src.Logic.storage_observer import storage_observer
from src.models.event_type import event_type
from src.models.log_type_model import log_type


class settings:
    __first_name = ""
    __first_start=True


    #переменные для settings
    __block_period=datetime(1,1,1)
    __INN=""
    __account=""
    __correspond_account=""
    __BIK=""
    __name=""
    __property_type=""
    __report_type=""


    #Репорт формат, из него будем брать строки 
    __Report_format={"CSV":"","Markdown":"","Json":""}


    @property
    def Report_format(self):
        return self.__Report_format



    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, value: str):
        """
            Полное наименование
        Args:
            value (str): _description_

        Raises:
            Exception: _description_
        """
        if not isinstance(value, str):
            raise argument_exception("Некорректный аргумент!")
        
        self.__first_name = value.strip()


    
    @property
    def report_type(self):
        return self.__report_type
    
    @report_type.setter
    def report_type(self, value: str):
        """
            Полное наименование
        Args:
            value (str): _description_

        Raises:
            Exception: _description_
        """
        if not isinstance(value, str):
            raise argument_exception("Некорректный аргумент!")
        
        self.__report_type = value.strip()
    
    

    #объявления
    @property
    def INN(self):
        return self.__INN
    
    @property
    def account(self):
        return self.__account
    
    @property
    def correspond_account(self):
        return self.__correspond_account
    
    @property
    def BIK(self):
        return self.__BIK
    
    @property
    def name(self):
        return self.__name
    
    @property 
    def property_type(self):
        return self.__property_type
    
    @property
    def block_period(self):
        return self.__block_period

    #вывод CSV
    @property
    def Report_CSV(self):
        return self.__Report_format['CSV']
    
    @property
    def Report_Markdown(self):
        return self.__Report_format['Markdown']
    
    @property
    def Report_Json(self):
        return self.__Report_format['Json']


    #Сеттеры
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
        storage_observer.raise_event(event_type.make_log(),log_type.log_type_debug(),"изменение INN", "settings.py/INN")
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
        storage_observer.raise_event(event_type.make_log(),log_type.log_type_debug(),"изменение account", "settings.py/account")
        self.__account=value_stripped


    @correspond_account.setter
    def correspond_account(self,value:str):
        #делаем через replace на случай введения с пробелами
        value_stripped=value.strip().replace(' ','')
        #Состоит ли из символов (value у нас str на случай незначащих нулей в начале числа)
        if not isinstance(value,str) or not(value_stripped.isdigit()):
            raise  argument_exception("Некорректный аргумент")
        

        #проверка на длинну
        if len(value_stripped)!=11:
            raise argument_exception("Некорректная длинна")
        storage_observer.raise_event(event_type.make_log(),log_type.log_type_debug(),"изменение correspond_account", "settings.py/correspond_account")
        self.__correspond_account=value_stripped

    @BIK.setter
    def BIK(self,value:str):
        value_stripped=value.strip().replace(' ','')
        #Состоит ли из символов (value у нас str на случай незначащих нулей в начале числа)
        if not isinstance(value,str) or not(value_stripped.isdigit()):
            raise  argument_exception("Некорректный аргумент")
        

        #проверка на длинну
        if len(value_stripped)!=9:
            raise argument_exception("Некорректная длинна")
        storage_observer.raise_event(event_type.make_log(),log_type.log_type_debug(),"изменение BIK", "settings.py/BIK")
        self.__BIK=value_stripped

    @name.setter
    def name(self,value:str):
        #берем first name
        if not isinstance(value, str):
            raise argument_exception("Некорректный аргумент!")
        storage_observer.raise_event(event_type.make_log(),log_type.log_type_debug(),"изменение name", "settings.py/name")
        self.__name = value.strip()

    @property_type.setter
    def property_type(self,value:str):
        value_stripped=value.strip()
        if not isinstance(value,str):
            raise  argument_exception("Некорректный аргумент")
        

        #проверка на длинну
        if len(value_stripped)!=5:
            raise argument_exception("Некорректная длинна")
        storage_observer.raise_event(event_type.make_log(),log_type.log_type_debug(),"изменение property_type", "settings.py/property_type")
        self.__property_type=value_stripped

    @block_period.setter
    def block_period(self,value:str):
        if not isinstance(value,str):
            raise  argument_exception("Некорректный аргумент")
        
        #проверка на указание даты со временем

        try:
            value=value.split(' ')[0]

            legacy=self.__block_period

            self.__block_period=datetime.strptime(value, "%Y-%m-%d")

            if legacy!=self.__block_period:
                storage_observer.raise_event(event_type.changed_block_period())
                storage_observer.raise_event(event_type.make_log(),log_type.log_type_debug(),"изменение block_period", "settings.py/block_period")
            
        except Exception as ex:
            raise operation_exception(f'неудалось сконвертировать дату {ex}')





    @property
    def is_first_start(self):
        return self.__first_start

    @is_first_start.setter
    def is_first_start(self,value):
        if not isinstance(value,str) and not isinstance(value,bool):
            raise argument_exception("wrong argument")
        
        storage_observer.raise_event(event_type.make_log(),log_type.log_type_debug(),"изменение is_first_start", "settings.py/is_first_start")
        self.__first_start=(str(value).lower()=='true')