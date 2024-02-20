from pathlib import Path
import os
import sys

sys.path.append(os.path.join(Path(__file__).parent.parent,'src'))

from Logic.start_factory import start_factory
from models.range_model import range_model
from src.settings_manager import settings_manager


import unittest


class test_factory(unittest.TestCase):

    def test_check_create_factory(self):
        #preparation
        unit=start_factory()


        #action
        A=unit.create_nomenclature()

        #check
        assert A is not None


    def test_check_first_start(self):
        #preparation
        unit=settings_manager()
        address=os.path.join(Path(__file__).parent.parent,'Jsons')
        unit.open(address,'Tester.json')
        item=start_factory()

        #action 
        item.options=unit.settings
        check=item.create()


        #check
        assert len(check)>0
