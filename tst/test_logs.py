from pathlib import Path
import os
import sys
from datetime import date,datetime
from uuid import uuid4

sys.path.append(Path(__file__).parent.parent)


from src.settings_manager import settings_manager
from src.models.event_type import event_type
from src.Logic.storage_observer import storage_observer
from  src.models.log_type_model import log_type
from src.Logic.start_factory import start_factory
from src.storage.storage import storage

import unittest


class test_logs(unittest.TestCase):

    def create_log(self):  
        #preparation
        unit=settings_manager()
        address=os.path.join(Path(__file__).parent.parent,'Jsons')
        unit.open('Tester.json',address)
        item=start_factory(unit.settings)
        item.create()

        #действие 
        storage_observer.raise_event(event_type.make_log(log_type.log_type_debug(),"Проверяем","Тест"))


        #проверка
        assert len(item.storage.data[storage.logs_key()])!=0