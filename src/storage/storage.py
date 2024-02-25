


class storage:
    __data={}



    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(storage, cls).__new__(cls)
        return cls.instance  

    @property
    def data(self):
        return self.__data



    #ключ хранения номенклатуры        
    @staticmethod
    def nomenclature_key():


        return "nomenclature"
    
    #ключ хранения группы
    @staticmethod
    def group_key():

        return "group"
    
    #ключ хранения единиц измерения
    @staticmethod
    def unit_key():

        return "unit"


    #ключ хранения рецептов
    @staticmethod
    def reciepe_key():
        return "reciepe"
    