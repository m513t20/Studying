from pathlib import Path
import os
import sys

sys.path.append(os.path.join(Path(__file__).parent.parent,'src'))

from models.range_model import range_model,create_gramm,create_kilogram


import unittest


class test_factory(unittest.TestCase):

    def test_check_create_factory(self):
        #preparation
        unit=create_kilogram()


        #action


        #check
        assert unit is not None