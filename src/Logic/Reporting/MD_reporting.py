from pathlib import Path
import os
import sys

from settings import settings

sys.path.append(Path(__file__).parent.parent)

from Logic.Reporting.Abstract_reporting import abstract_reporting


class MD_reporting(abstract_reporting):

    def __init__(self, data_examp: list):
        super().__init__(data_examp)

    def create(self, value):


        #берём ключи
        keys=super().get_fields(value)


        result_md="|"



        #Разделение шапки и ячеек
        bottom_line='|'


        #шапка таблицы
        for cur_key in keys:
            result_md+=cur_key+'|'
            bottom_line+='-'*len(cur_key)+'|'
        
        
        result_md+='\n'+bottom_line+'\n'
        




        #добавляем значения
        for cur_val in self.data[value]:

            result_md+='|'
            for cur_key in keys:
                result_md+=str(getattr(cur_val,cur_key))+'|'
            
            result_md+='\n'
        

        #self.hidden_settings.Report_format["CSV"]=result_csv

        return result_md
        