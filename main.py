from flask import Flask

from pathlib import Path
import os
import sys

sys.path.append(os.path.join(Path(__file__).parent,'src'))



from pathlib import Path
from storage.storage import storage
from Logic.start_factory import start_factory
from models.range_model import range_model
from src.settings_manager import settings_manager
from Logic.report_factory import report_factory


app=Flask(__name__)



@app.route("/api/report/<storage_key>/<report_type>",methods=["GET"])
def get_report(storage_key:str,report_type:str):

    check=[storage.unit_key(),storage.group_key(),storage.reciepe_key(),storage.nomenclature_key()]

    type=["CSV","Markdown","Json"]

    #preparation
    unit=settings_manager()
    address=os.path.join(Path(__file__).parent,'Jsons')
    unit.open('Tester.json',address)
    item=start_factory(unit.settings)
    item.create()
    factory=report_factory()

    result=storage_key
    #action
    if storage_key in check and report_type in type:
        result=factory.create(report_type,item.storage.data,storage_key)





    response_type=app.response_class(
        response=f" KEY {storage_key}\n{result}",
        status=200,
        mimetype="application/text"
    )

    return response_type



if __name__=="__main__":
    app.run(debug=True)