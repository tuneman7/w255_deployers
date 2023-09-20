from includes import *
from flask import Blueprint

consume_fastapi = Blueprint('consume_fastapi', __name__)

from libraries.data_objects import data_objects as do


@consume_fastapi.route('/consume_fastapi_start', methods=['POST', 'GET'])
def consume_fastapi_start():
        res = make_response(render_template('pages/section_content/placeholder.consume_fastapi.html',
        section_number="five"))
        return res

def create_home_request(form):
       hr = dict()
       hr["MedInc"] = float(request.form["medinc_text"])
       hr["HouseAge"] = float(request.form["houseage_text"])
       hr["AveRooms"]  = float(request.form["averooms_text"])
       hr["AveBedrms"] = float(request.form["avebedrms_text"])
       hr["Population"] = float(request.form["population_text"])
       hr["AveOccup"] = float(request.form["aveoccup_text"])
       hr["Latitude"] = float(request.form["lat_text"])
       hr["Longitude"] = float(request.form["long_text"])
       return hr

import requests

def execute_fastapi_call(json_post):
    url = "http://192.168.49.2:31355/predictitem"
    r = requests.post(url, json=json_post)
    return url,r.status_code,json.dumps(r.json(),indent=1)

        

@consume_fastapi.route('/consume_fastapi', methods=['POST', 'GET'])
def consume_fastapi_json(popout = False):

        mdo = do()
        t_medinc = mdo.hh_income_tuple()
        t_houseage = mdo.h_age_tuple()
        t_averooms  = mdo.avg_beds_tuple()
        t_avebedrms = mdo.avg_beds_tuple()
        t_population = mdo.bg_pop_tuple()
        t_aveoccup = mdo.avg_occupacy()
        t_cities = mdo.ca_city_lat_long_tuple()

        got_values = True

        float_values = ["medinc_text","houseage_text","averooms_text","avebedrms_text","population_text","aveoccup_text","lat_text","long_text"]

        #make sure we got all of these and that they are float values.
        try:
                f_medinc = request.form["medinc_text"]
                f_houseage = request.form["houseage_text"]
                f_averooms  = request.form["averooms_text"]
                f_avebedrms = request.form["avebedrms_text"]
                f_population = request.form["population_text"]
                f_aveoccup = request.form["aveoccup_text"]
                f_lat = request.form["lat_text"]
                f_long = request.form["long_text"]
        except Exception as ex:
                got_values = False
                print("*"*30)                              
                print(str(ex))
                print("*"*30)

        print("got_values={}".format(got_values))
        api_json = None
        return_json = None
        status_code = None
        url = None
        if got_values is True:
               hr = create_home_request(form=request.form)
               api_json =json.dumps(hr,indent=1)
               api_json_to_post=json.dumps(hr)
               print(api_json)
               url,status_code,return_json=execute_fastapi_call(hr)


        form = home_predict_model_inputs(request.form)

        res = jsonify({'htmlresponse':render_template('modal/fastapi_consumer.modal.html',
                form=form,
                api_json=api_json,
                return_json=return_json,
                return_status_code=status_code,
                post_url=url
                )})

        return res
