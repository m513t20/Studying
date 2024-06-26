from src.error_proxy import error_proxy
from storage.storage import storage
from src.Logic.storage_observer import storage_observer
from src.models.event_type import event_type
from src.Logic.services.abstract_service import abstract_sevice
from src.Logic.Reporting.Json_convert.reference_conventor import reference_conventor
from pathlib import Path
import json

class log_master(abstract_sevice):
    __storage=None
    __log=None
    __save_path=Path(__file__).parent.parent/"storage"/"saved_models"/"logs.txt"
    __save_path_json=Path(__file__).parent.parent/"storage"/"saved_models"/"logs.json"

    def __init__(self) -> None:
        self.__storage=storage()
        storage_observer.observers.append(self)


    def handle_event(self,event:str,*args):
        super().handle_event(event,args)
        splitted=event.split(" ")
        if splitted[0]==event_type.make_log_key():
            self._create_log(args[0],args[1],args[2])
            self._save_log()

    def _create_log(self,type:str,text:str,source:str):

        self.__log=error_proxy(text,source)
        self.__log.log_type=type
        print(list(self.__storage.data.keys()))
        self.__storage.data[storage.logs_key()].append(self.__log)

    def _save_log(self):
        ref=reference_conventor(error_proxy)
        ret=ref.convert(self.__log)
        get=None
        to_write=json.dumps(ret,ensure_ascii=False)
        with open(self.__save_path,"r+") as saved:
            if not self.__save_path.stat().st_size==0:
                saved.seek(0,2)

            saved.write(to_write)
            saved.write("\n")

        with open(self.__save_path_json,"r+") as saved_json:
            if self.__save_path_json.stat().st_size==0:
                saved_json.write(json.dumps({'logs':[to_write]}))
            else:
                get=json.load(saved_json)
                get['logs'].append(to_write)


        if get is not None:
            with open(self.__save_path_json,"w") as saved_json:
                saved_json.write(json.dumps(get,ensure_ascii=False))

        
        
