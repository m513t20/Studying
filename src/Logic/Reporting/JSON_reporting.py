from pathlib import Path
import sys



sys.path.append(Path(__file__).parent.parent)

from Logic.Reporting.Abstract_reporting import abstract_reporting
import json 



class Json_reporting(abstract_reporting):

    def __init__(self, data_examp: list):
        super().__init__(data_examp)

    def create(self, value):


        #берём ключи
        keys=super().get_fields(value)
        Json_return={}
        for cur_val in self.data[value]:
            Json_return[cur_val]={}
            for cur_key in keys:
                Json_return[cur_val][cur_key]=(getattr(cur_val,cur_key))

        return json.dump(Json_return)
