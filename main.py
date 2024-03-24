from flask import Flask,send_file,request

from pathlib import Path
from datetime import datetime
import os
import json
import sys

sys.path.append(os.path.join(Path(__file__).parent,'src'))

from error_proxy import error_proxy
from pathlib import Path
from storage.storage import storage
from Logic.start_factory import start_factory
from models.range_model import range_model
from src.settings_manager import settings_manager
from Logic.report_factory import report_factory
from Logic.storage_prototype import storage_prototype
from storage.storage_factory import storage_factory
from src.Logic.Reporting.Json_convert.reference_conventor import reference_conventor


app=Flask(__name__)

unit=settings_manager()
address=os.path.join(Path(__file__).parent,'Jsons')
unit.open('Tester.json',address)
item=start_factory(unit.settings)
item.create()


#по ссылке выдаёт результат 
@app.route("/api/report/<storage_key>",methods=["GET"])
def get_report(storage_key:str):

    check=[storage.unit_key(),storage.group_key(),storage.reciepe_key(),storage.nomenclature_key(),storage.journal_key()]


    #preparation

    factory=report_factory()

    result=storage_key


    report_type=item.options.report_type
    #action

    if storage_key in check:
        factory.create(report_type,item.storage.data,storage_key)

    #OTDELNAYA FIMCTSIA DLYA SOZDANIYA FAYLA

    # response_type=app.response_class(
    #     response=f"{result}",
    #     status=200,
    #     mimetype="application/text"
    # )
   
    return send_file(f'report.{report_type.lower()}')



@app.route("/api/storage/rests",methods=["GET"])
def get_rests():

    key=storage.journal_key()


    # args=request.args
    # if("start_period") not in args.keys():
    #     return error_proxy.create_error(error_proxy,Exception)
    # if("stop_period") not in args.keys():
    #     return error_proxy.create_error(error_proxy,Exception)
    #BEREM DATU ZAPROSOM

    start_date=datetime(2023,1,1)
    finish_date=datetime(2024,12,31)

    prototype=storage_prototype(item.storage.data[key])

    transactions=prototype.filter_date(start_date,finish_date)

    process=reference_conventor(type(item.storage.data[storage.nomenclature_key()][0]),type(error_proxy()),type(item.storage.data[storage.group_key()][0]),type(item.storage.data[storage.unit_key()][0]),type(transactions.data[0]))
    #UBRAT

    result={}
    for index,cur_tran in enumerate(transactions.data):
        result[index]=process.convert(cur_tran)


    print(result)
    response_type=app.response_class(
        response=f"{json.dumps(result)}",
        status=200,
        mimetype="application/json; charset=utf-8"
    )


    return response_type
   



if __name__=="__main__":
    app.run(debug=True)