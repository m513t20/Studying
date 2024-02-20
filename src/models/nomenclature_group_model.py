from abstract_reference import abstract_reference

class nomenclature_group_model(abstract_reference):
    @staticmethod
    def create_group():
        return nomenclature_group_model("Ингридиенты")