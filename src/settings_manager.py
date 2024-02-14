import os
from pathlib import Path
import json
import uuid
from settings import settings
from exceptions import argument_exception, operation_exception

class settings_manager(object) :
    # Имя файла настроек
    __file_name = "settings.json"
    # Уникальный номер
    __unique_number = None
    # Словарь с данными
    __data = {}
    
    # Настройки инстанс
    __settings = settings()


    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(settings_manager, cls).__new__(cls)
        return cls.instance  
    
    def __convert(self):
        if len(self.__data) == 0:
            raise operation_exception("Невозможно создать объект типа settings.py")
        
        fields = dir(self.__settings.__class__)
        print(fields)
        

        
        field_keys=list(self.__data.keys())
        print(field_keys)

        #по ключам json подставляет атрибуты для класса и проверяет их
        check_atrs=0
        for cur_key in field_keys:
            if cur_key in fields:
                check_atrs+=1
                value = self.__data[cur_key]
                setattr(self.__settings,cur_key,value)
                print(getattr(self.__settings,cur_key))




        return True 
    
    def __init__(self) -> None:
        self.__unique_number =  uuid.uuid4()
    
    def open(self, file_name='settings.json',file_path=Path(__file__).parent) -> bool:
        if not isinstance(file_name, str):
            raise argument_exception("ERROR: Неверный аргумент!")
        
        if file_name == "":
            raise argument_exception("ERROR: Неверный аргумент!")
        
        self.__file_name = file_name.strip()
        self.__file_path=file_path
        try:
            self.__open()
            self.__convert()
            return True
        except:
            return False



        
        
    
    @property
    def data(self):
        """
            Текущие данные 
        Returns:
            _type_: словарь
        """
        return self.__data
    
    @property
    def number(self)-> str:
        return str(self.__unique_number.hex)
    
    
    def __open(self):
        """
            Открыть файл с настройками
        Raises:
            Exception: Ошибка при открытии файла
        """
        file_path = os.path.join(self.__file_path,self.__file_name)

        # print('choose file adress')
        # file_adress=input(file_path.parent)

        #settings_file = file_path.parent+self.__file_name
        settings_file = file_path
        if not os.path.exists(settings_file):
            raise operation_exception("ERROR: Невозможно загрузить настройки! Не найден файл %s", settings_file)

        with open(settings_file, "r") as read_file:
            self.__data = json.load(read_file)          
    
    
