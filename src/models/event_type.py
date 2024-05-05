from src.models.abstract_reference import abstract_reference
from src.exceptions import argument_exception
import uuid

#
# Типы событий
#
class event_type(abstract_reference):
 
    @staticmethod
    def changed_block_period() -> str:
        """
            Событие изменения даты блокировки
        Returns:
            str: _description_
        """
        return "changed_block_period"


    @staticmethod 
    def deleted_nomenclature()->str:
        """
            Событие удаления номенклатуры
        Returns:
            str: _description_
        """
        return f"deleted_nomenclature"
    

    @staticmethod 
    def deleted_nomenclature_id()->str:
        """
            Событие удаления номенклатуры
        Returns:
            str: _description_
        """
        return f"deleted_nomenclature"
    
    @staticmethod
    def make_log_key():
        return f"make_log"

    @staticmethod
    def make_log():
        return f"make_log"