from settings import settings
import unittest


class test_settings(unittest.TestCase):
    
    
    #
    # Провеиить корректность заполнения поля first_name
    #
    def test_check_first_name(self):
        # Подготовка
        item = settings()
        
        # Действие
        item.first_name = "a  "
        
        # Проверка
        assert item.first_name == "a"