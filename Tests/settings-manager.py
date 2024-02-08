import os
import json
import uuid
from settings import settings


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
    
    def convert(self):
        if len(self.__data) == 0:
            raise Exception("Невозможно создать объект типа settings.py")
        
        fields = dir(self.__settings.__class__)
        print(fields)
        
        field = "first_name"
        value = self.__data[field]
        setattr(self.__settings, field, value)
        
        print(self.__settings.first_name)        
    
    def __init__(self) -> None:
        self.__unique_number =  uuid.uuid4()
    
    def open(self, file_name: str) -> bool:
        if not isinstance(file_name, str):
            raise Exception("ERROR: Неверный аргумент!")
        
        if file_name == "":
            raise Exception("ERROR: Неверный аргумент!")
        
        self.__file_name = file_name.strip()

        try:
            self.__open()
        except:
            return False
             
        return True
        
    
    @property
    def data(self) -> {}:
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
        file_path = os.path.split(__file__)
        settings_file = "%s/%s" % (file_path[0], self.__file_name)
        if not os.path.exists(settings_file):
            raise Exception("ERROR: Невозможно загрузить настройки! Не найден файл %s", settings_file)

        with open(settings_file, "r") as read_file:
            self.__data = json.load(read_file)          
    
    
    