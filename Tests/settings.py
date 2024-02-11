

class settings:
    __first_name = ""



    #переменные для settings
    __INN=""
    __account=""
    __correspond_account=""
    __BIK=""
    __name=""
    __property_type=""


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
            raise Exception("Некорректный аргумент!")
        
        self.__first_name = value.strip()
    

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


    #Сеттеры
    @INN.setter
    def INN(self,value: str):
        #делаем через replace на случай введения с пробелами
        value_stripped=value.replace(' ','')
        #Состоит ли из символов (value у нас str на случай незначащих нулей в начале числа)
        if not isinstance(value,str) or not(value_stripped.isdigit()):
            raise  Exception("Некорректный аргумент")
        

        #проверка на длинну
        if len(value_stripped)!=12:
            raise Exception("Некорректная длинна")
            
        self.__INN=value_stripped

    @account.setter
    def account(self,value:str):
        #делаем через replace на случай введения с пробелами
        value_stripped=value.replace(' ','')
        #Состоит ли из символов (value у нас str на случай незначащих нулей в начале числа)
        if not isinstance(value,str) or not(value_stripped.isdigit()):
            raise  Exception("Некорректный аргумент")
        

        #проверка на длинну
        if len(value_stripped)!=11:
            raise Exception("Некорректная длинна")
            
        self.__account=value_stripped


    @correspond_account.setter
    def correspond_account(self,value:str):
        #делаем через replace на случай введения с пробелами
        value_stripped=value.replace(' ','')
        #Состоит ли из символов (value у нас str на случай незначащих нулей в начале числа)
        if not isinstance(value,str) or not(value_stripped.isdigit()):
            raise  Exception("Некорректный аргумент")
        

        #проверка на длинну
        if len(value_stripped)!=11:
            raise Exception("Некорректная длинна")
            
        self.__correspond_account=value_stripped

    @BIK.setter
    def BIK(self,value:str):
        #делаем через replace на случай введения с пробелами
        value_stripped=value.replace(' ','')
        #Состоит ли из символов (value у нас str на случай незначащих нулей в начале числа)
        if not isinstance(value,str) or not(value_stripped.isdigit()):
            raise  Exception("Некорректный аргумент")
        

        #проверка на длинну
        if len(value_stripped)!=9:
            raise Exception("Некорректная длинна")
            
        self.__BIK=value_stripped

    @name.setter
    def name(self,value:str):
        #берем first name
        if not isinstance(value, str):
            raise Exception("Некорректный аргумент!")
        
        self.__name = value.strip()

    @property_type.setter
    def property_type(self,value:str):
        value_stripped=value.strip()
        if not isinstance(value,str):
            raise  Exception("Некорректный аргумент")
        

        #проверка на длинну
        if len(value_stripped)!=5:
            raise Exception("Некорректная длинна")
            
        self.__property_type=value_stripped