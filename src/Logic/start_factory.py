from pathlib import Path
import os
import sys

sys.path.append(os.path.join(Path(__file__).parent.parent,'models'))


from models.nomenclature_model import nomenclature_model,nomenclature_group_model,range_model, create_gramm,create_kilogram
from settings import settings

class start_factory:

    __options:settings=None

    @staticmethod
    def create_nomenclature():
        group=nomenclature_group_model.create_group()
        Output=[]
        kg=create_kilogram()
        gr=create_gramm()
        sht=range_model("Shtuka",1)

        Output.append(nomenclature_model('Pshenichnaya muka','Pshenichnaya muka',group,kg))
        Output.append(nomenclature_model('sugar','sugar',group,kg))
        Output.append(nomenclature_model('maslo','slivochnoe maslo',group,gr))
        Output.append(nomenclature_model('eggs','eggs',group,sht))
        Output.append(nomenclature_model('Vanilin','Vanilin',group,range_model))

        return Output


    def create(self):
        if self.__options.is_first_start:
            self.__options.is_first_start=False
            return start_factory.create_nomenclature()
        
        else:
            items=[]
            return items

