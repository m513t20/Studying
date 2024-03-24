from flask import Flask,send_file,request

from pathlib import Path
from datetime import datetime
import os
import sys
import uuid

sys.path.append(os.path.join(Path(__file__).parent,'src'))

from error_proxy import error_proxy
from pathlib import Path
from storage.storage import storage
from Logic.start_factory import start_factory
from src.settings_manager import settings_manager
from Logic.report_factory import report_factory
from src.Logic.storage_sevice import storage_service



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

    # response_type=app.response_class(
    #     response=f"{result}",
    #     status=200,
    #     mimetype="application/text"
    # )
   
    return send_file(f'report.{report_type.lower()}')


@app.route("/api/storage/<nomenclature_id>/turns",methods=["GET"])
def get_nomenclature_rests(nomenclature_id:uuid.UUID):
    key=storage.journal_key()


    #генерация работает, однако столкнулся с проблемой - тк айди каждый раз генериться случайно, узнать актуальный айди для фильтрации - можно  только из других запросов
    data=storage_service(item.storage.data[key]).create_id_turns(uuid.UUID(nomenclature_id))

    responce_type=storage_service.create_response(data,app)

    return responce_type
    



@app.route("/api/storage/rests",methods=["GET"])
def get_rests():

    key=storage.journal_key()


    args=request.args
    if("start_period") not in args.keys():
        return error_proxy.create_error(error_proxy,Exception)
    if("stop_period") not in args.keys():
        return error_proxy.create_error(error_proxy,Exception)
    #BEREM DATU ZAPROSOM

    start_date= datetime.strptime(args["start_period"], "%Y-%m-%d")
    finish_date=datetime.strptime(args["stop_period"], "%Y-%m-%d")


    data=storage_service(item.storage.data[key]).create_turns(start_date,finish_date)

    response_type=storage_service.create_response(data,app)


    return response_type
   




if __name__=="__main__":
    app.run(debug=True)