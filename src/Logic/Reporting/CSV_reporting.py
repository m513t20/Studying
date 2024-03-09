from pathlib import Path
import os
import sys

from settings import settings

sys.path.append(Path(__file__).parent.parent)

from Logic.Reporting.Abstract_reporting import abstract_reporting


class CSV_reporting(abstract_reporting):

    def __init__(self, data_examp: list):
        super().__init__(data_examp)

    def create(self, value):


        #берём ключи
        keys=super().get_fields(value)


        result_csv=""





        #шапка таблицы
        for cur_key in keys:
            result_csv+=cur_key+','
        
        result_csv=result_csv.strip(',')+'\n'



        #добавляем значения
        for cur_val in self.data[value]:
            for cur_key in keys:
                result_csv+=str(getattr(cur_val,cur_key))+','
            result_csv=result_csv.strip(',')
            result_csv+='\n'
        

        #self.hidden_settings.Report_format["CSV"]=result_csv

        return result_csv
        