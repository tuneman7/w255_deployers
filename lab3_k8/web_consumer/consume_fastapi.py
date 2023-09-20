from includes import *
from flask import Blueprint

consume_fastapi = Blueprint('consume_fastapi', __name__)

from libraries.data_objects import data_objects as do

@consume_fastapi.route('/consume_fastapi_start', methods=['POST', 'GET'])
def consume_fastapi_start():
        res = make_response(render_template('pages/section_content/placeholder.consume_fastapi.html',
        section_number="five"))
        return res


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


        try:

                f_medinc = request.form["medinc"]
                f_houseage = request.form["houseage"]
                f_averooms  = request.form["averooms"]
                f_avebedrms = request.form["avebedrms"]
                f_population = request.form["population"]
                f_aveoccup = request.form["aveoccup"]
                f_cities = request.form["cities"]

        except Exception as ex:
                try:
                        f_medinc = request.args.get("medinc",default="",type=str)
                        f_houseage = request.args.get("houseage",default="",type=str)
                        f_averooms  = request.args.get("averooms",default="",type=str)
                        f_avebedrms = request.args.get("avebedrms",default="",type=str)
                        f_population = request.args.get("population",default="",type=str)
                        f_aveoccup = request.args.get("aveoccup",default="",type=str)
                        f_cities = request.args.get("cities",default="",type=str)
                except:
                        print("*"*30)                              
                        print(str(ex))
                        print("*"*30)

                print("*"*30)                              
                print(str(ex))
                print("*"*30)



        form = home_predict_model_inputs(request.form)

        res = jsonify({'htmlresponse':render_template('modal/fastapi_consumer.modal.html',
                form=form
                )})

        return res
