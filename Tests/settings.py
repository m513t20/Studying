

class settings:
    __first_name = ""
    
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
        
        