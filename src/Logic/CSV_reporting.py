from pathlib import Path
import os
import sys

from settings import settings

sys.path.append(Path(__file__).parent.parent)

import uuid
from abc import ABC
from exceptions import argument_exception
from error_proxy import error_proxy
from Logic.start_factory import start_factory,range_model,nomenclature_group_model,nomenclature_model
from Logic.Abstract_reporting import abstract_reporting


class CSV_reporting(abstract_reporting):

    def __init__(self, data_examp: list, settings_examp: settings):
        super().__init__(data_examp, settings_examp)

    def create(self, value):


        #берём ключи
        keys=super().create(value)

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
        

        self.hidden_settings.Report_format["CSV"]=result_csv

        return result_csv
        