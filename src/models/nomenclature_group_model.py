
from src.models.abstract_reference import abstract_reference

class nomenclature_group_model(abstract_reference):

    def _load(self, data: dict):
        return super()._load(data)

    @staticmethod
    def create_group():
        return nomenclature_group_model("Ингридиенты")
    
    @staticmethod
    def create_group_eggs():
        return nomenclature_group_model("яйца")
    
    @staticmethod
    def create_group_meat():
        return nomenclature_group_model("мясо")
    
    @staticmethod
    def create_group_vegs():
        return nomenclature_group_model("Овощи")