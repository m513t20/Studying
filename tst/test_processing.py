from pathlib import Path
import os
import sys
import json

sys.path.append(os.path.join(Path(__file__).parent.parent,'src'))

from settings_manager import settings_manager
from storage.storage import storage
from Logic.start_factory import start_factory
from datetime import datetime
from src.Logic.process_factory import process_factory

import unittest

class test_processing(unittest.TestCase):

    def test_check_journal_to_turn(self):
        #Подготовка
        unit=settings_manager()
        address=os.path.join(Path(__file__).parent.parent,'Jsons')
        unit.open('Tester.json',address)
        factory=start_factory(unit.settings)

        factory.create()


        process=process_factory()

        #действие
        result=process.create(storage.process_turn_key(),factory.storage.data[storage.journal_key()],datetime(2023,1,1),datetime(2024,12,31))

        #тут проверял через excel, поэтому assert не придумал, но сходится
        
        

        #проверка
        assert len (result)!=0
        assert result[0].amount==-300