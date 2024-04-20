from abc import ABC


class abstract_handle(ABC):
    
    @staticmethod
    def handle_event():
        pass
#nam nado chtoby on vozvraschal funktsyu dlya raboty s eventom 
#na vhod on nichego ne poluchaet, poetome emu nado dobavit staticmethod dlya vernoy raboty
#Takje v delete v service dobavlyaem dopolnitelnyi klass u kotorogo v konstruktoe nomenclatura 
#Potom bydem brat ego i rabotat v handle_delete. Voooooooooooot