class error_proxy:
    __error_text=""
    __error_source=""



    def __init__ (self, error_text: str="", error_source:str=""):
        self.error_source=error_source
        self.error_text=error_text

    @property
    def error_text(self):
        return self.__error_text
    

    @error_text.setter
    def error_text(self,value:str):
        if not isinstance(value,str):
            raise Exception("Invalid argument")
            
        if value.strip()==" ":
            self.__if_error=False
            return
            

        self.__if_error=True 
        self.__error_text=value.strip()

        
    @property
    def error_source(self):
        return self.__error_source
    
    @error_source.setter
    def error_source(self,value:str):
        if not isinstance(value,str):
            raise Exception("Invalid argument")
            
        if value.strip()==" ":
            self.__if_error=False
            return
            

        self.__if_error=True 
        self.__error_source=value.strip()

    
    
    @property 
    def if_error(self):
        return self.__if_error
    
    def create_error(self,exception: Exception):
        if not isinstance(exception,Exception):
            self.error_text="Invalid parameters"
            self.error_source="set_error"
            return
        self.error_text=f"ERROR! {str(exception)}"
        self.error_source=f"Exception {type(exception)}"

    def __str__(self):
        return str(self.if_error)

