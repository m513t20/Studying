from src.error_proxy import error_proxy
from storage.storage import storage
from src.Logic.storage_observer import storage_observer
from src.models.event_type import event_type
from src.Logic.Reporting.Json_convert.reference_conventor import reference_conventor
from pathlib import Path
import json

class log_master:
    __storage=None
    __log=None
    __save_path=Path(__file__).parent.parent/"storage"/"saved_models"/"logs.txt"

    def __init__(self) -> None:
        self.__storage=storage()
        storage_observer.observers.append(self)


    def handle_event(self,event:str):
        splitted=event.split(" ")
        if splitted[0]==event_type.make_log_key():
            self._create_log(splitted[1],splitted[2],splitted[3])
            self._save_log()

    def _create_log(self,type:str,text:str,source:str):

        self.__log=error_proxy(text,source)
        self.__log.log_type=type
        print(list(self.__storage.data.keys()))
        self.__storage.data[storage.logs_key()].append(self.__log)

    def _save_log(self):
        ref=reference_conventor(error_proxy)
        ret=ref.convert(self.__log)
        to_write=json.dumps(ret,ensure_ascii=False)
        with open(self.__save_path,"r+") as saved:
            if not self.__save_path.stat().st_size==0:
                saved.seek(0,2)

            saved.write(to_write)
            saved.write("\n")
            

        
        
