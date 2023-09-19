from includes import *
from flask import Blueprint

section_5 = Blueprint('section_5', __name__)

from libraries.data_objects import data_objects as do

@section_5.route('/section_five', methods=['POST', 'GET'])
def section_five():
        res = make_response(render_template('pages/section_content/placeholder.prediction_calc.html',
        section_number="five"))
        return res

def get_signal_icon(signal):
    #print("signal=",signal)
    image_path = "./static/images/predict_icons/thumbs_"+ signal +".png"
    return image_path

def get_aggregate_signal_icon(signal):
    #print("signal=",signal)
    image_path = "./static/images/predict_icons/all_"+ signal +".png"
    return image_path

def get_aggregate_signal_text(signal):
        if signal=="up":
                return " this could be a good time to buy."
        if signal == "down":
                return " this is probably not a good time to buy."
        if signal == "neutral":
                return " wait, and watch this market."


def get_model_image(county_name,model_used,is_county=True):
        print("get_model_images:=",county_name)

        image_path = None
        if model_used is not None:
                image_path = "./static/images/pytorch_files/"+ county_name.lower() +"_"+ model_used +"/"+county_name.lower()+".png"
                if is_county == False:
                        image_path = "./static/images/pytorch_msa/"+ county_name.lower() +"_"+ model_used +"/"+county_name.lower()+".png"

        # error_file = os.path.join(os.get(),"static","images","pytorch_files",county_name +"_initial","errored_out.txt")
        # if os.path.exists(error_file):

        return image_path

def get_ana_image():

        image_path = "./static/images/predict_icons/analytics.png"
        return image_path

        


from datetime import datetime
import operator
from libraries.analysis_object import analysis_object as ao

@section_5.route('/section_five_popout', methods=['POST', 'GET'])
def section_five_popout():
        try:
                county=request.args.get("county",default="",type=str)
                state =request.args.get("state",default="",type=str)
                county_or_msa = request.args.get("county_or_msa",default="MSA",type=str)
                popout = bool(request.args.get("popout",default=True,type=bool))
        except:
                fido='dido'


        res = make_response(render_template('pages/placeholder.predict_no_header.html',
        state=state,
        county_or_msa=county_or_msa,
        popout=popout,
        county=county,
        section_number="five"))
        return res





@section_5.route('/section_five_pred', methods=['POST', 'GET'])
def section_five_pred(popout = False):

        '''Counties to look at:
        los angeles, san francisco city, bexar tx (san antonio),
        '''


        try:
                state = request.form["state"]
                county = request.form["county"]
                county_or_msa = request.form["county_or_msa"]  

        except Exception as ex:
                try:
                        county=request.args.get("county",default="",type=str)
                        state =request.args.get("state",default="",type=str)
                        county_or_msa = request.args.get("county_or_msa",default="",type=str)
                        popout = bool(request.args.get("popout",default=True,type=bool))
                except:
                        print("*"*3000)                              
                        print(str(ex))
                        print("*"*3000)

                print("*"*3000)                              
                print(str(ex))
                print("*"*3000)

        print("county_or_msa=",county_or_msa)


        mdo = do()
        form = state_county_selection_form(request.form,county_or_msa=county_or_msa)
        is_county = True
        if county_or_msa == "MSA":
                is_county = False
                form.county_list.choices = mdo.msa_names_tuple(state)
        else:
                form.county_list.choices = mdo.county_names_tuple(state)
        
        if county=="":
                m_list = [x[0] for x in form.county_list.choices]
                county=m_list[0]
                print("*"*100)
                print("county=",county)
                print("*"*100)
                print(m_list)
                print("*"*100)
                #county=map(operator.itemgetter(0), form.county_list.choices)

        county_name = county.replace(" ","_")

        mao = ao(county_name,is_county)

        DOM_SIGNAL_DF,NO_MO_DOM_UP,NO_MO_DOM_DOWN,DOM_SIGNAL_GRAPH,DOM_SIGNAL,dom_this_year_count, dom_last_year_count,dom_this_year_higher,dom_pct_change,dom_response_text = mao.do_dom_analysis()

        INT_SIGNAL_DF,NO_MO_INT_UP,NO_MO_INT_DOWN,INT_SIGNAL_GRAPH,INT_SIGNAL,int_this_year_count, int_last_year_count,int_this_year_higher,int_pct_change,int_response_text = mao.do_int_analysis()
        
        INV_SIGNAL_DF,NO_MO_INV_UP,NO_MO_INV_DOWN,INV_SIGNAL_GRAPH,INV_SIGNAL,inv_this_year_count, inv_last_year_count,inv_this_year_higher,inv_pct_change,inv_response_text = mao.do_inv_analysis()

        PRICE_SIGNAL_DF,NO_MO_PRICE_UP,NO_MO_PRICE_DOWN,PRICE_SIGNAL_GRAPH,PRICE_SIGNAL,price_this_year_count, price_last_year_count,price_this_year_higher,price_pct_change,price_response_text = mao.do_price_analysis()

        inv_signal_gif = get_signal_icon(INV_SIGNAL)
        int_signal_gif = get_signal_icon(INT_SIGNAL)
        price_signal_gif = get_signal_icon(PRICE_SIGNAL)
        dom_signal_gif = get_signal_icon(DOM_SIGNAL)

        t0 = datetime(1, 1, 1)
        now = datetime.utcnow()
        seconds = (now - t0).total_seconds()
        ticks = seconds * 10**7

        model_signal,model_return_text,model_used,MODEL_DF = mao.get_model_signal()
        model_signal_gif = get_signal_icon(model_signal)

        # print("*"*60)
        # print(model_signal)
        # print("*"*60)
        # return None

        MODEL_DF = MODEL_DF[['date','time_idx','active_listing_count','thirty_year_interest_rate_five','median_listing_price','pred_median_listing_price']]
        MODEL_DF.columns = ['date','time_idx','Listing Count','30 yr Int (5lag)','Med List Price','Pred Med List Price']

        model_image = get_model_image(county_name,model_used,is_county) 
        model_image + "?"+str(ticks)


        dataset =  mao.get_county_df() 
        dataset.loc[:, "median_listing_price"] ='$'+ dataset["median_listing_price"].map('{:,.0f}'.format)
        dataset.loc[:, "active_listing_count"] =dataset["active_listing_count"].map('{:,.0f}'.format)
        dataset.loc[:, "thirty_year_interest_rate"] =dataset["thirty_year_interest_rate"].map(str) + " %"
        dataset.loc[:, "thirty_year_interest_rate_five"] =dataset["thirty_year_interest_rate_five"].map(str) + " %"
        dataset.loc[:, "median_days_on_market"] = dataset["median_days_on_market"].map('{:,.0f}'.format)


        #http://192.168.50.234:5023/test_jqgrid?county_name=los_angeles_ca

        dataset.columns = ["County","Date","Med List Price","30 Yr Int Rate","30 Yr Int Rate (5lag)","Active Listings","Med Days on Market"]
        county_text = dataset["County"][0]

        aggregate_signal_gif = get_aggregate_signal_icon(mao.get_aggregate_signal())

        aggregate_signal_text = get_aggregate_signal_text(mao.get_aggregate_signal())

        ana_image=get_ana_image()

        model_graph=mao.get_model_graph()

        INITIAL_HPARAMS, TUNED_HPARAMS, MODEL_USED = mao.get_models_hparams()



        res = jsonify({'htmlresponse':render_template('modal/prediction.modal.html',
                form=form,
                state=state,
                MODEL_USED=MODEL_USED.capitalize(),
                INITIAL_HPARAMS=INITIAL_HPARAMS,
                TUNED_HPARAMS=TUNED_HPARAMS,
                model_json=model_graph.to_json(),
                ana_image=ana_image,
                county=county,
                county_or_msa=county_or_msa,
                aggregate_signal_text = aggregate_signal_text,
                county_name=county_name,
                county_text = county_text,
                chart_json = DOM_SIGNAL_GRAPH.to_json(),
                chart_json1=INT_SIGNAL_GRAPH.to_json(),
                chart_json2=INV_SIGNAL_GRAPH.to_json(),
                chart_json3=PRICE_SIGNAL_GRAPH.to_json(),
                inv_signal_gif=inv_signal_gif,
                inv_response_text=inv_response_text,
                int_signal_gif=int_signal_gif,
                int_response_text=int_response_text,
                price_signal_gif=price_signal_gif,
                price_response_text=price_response_text,
                dom_signal_gif=dom_signal_gif,
                dom_response_text=dom_response_text,
                overall_signal_gif=aggregate_signal_gif,
                model_image_tuned=model_image,
                model_signal_gif = model_signal_gif,
                model_signal_text = model_return_text,
                predict_tables = [MODEL_DF.to_html()],
                tables=[dataset.to_html()],
                titles=[''],
                popout=popout
                )})

        return res


import locale
@section_5.route('/get_county_dataset', methods=['POST', 'GET'])
def get_county_dataset():

        locale.setlocale( locale.LC_ALL, 'en_CA.UTF-8' )
        county_name = request.form["county_name"]

        mao = ao(county_name)
        
        dataset =  mao.get_county_df() 

        dataset.loc[:, "median_listing_price"] ='$'+ dataset["median_listing_price"].map('{:,.0f}'.format)
        dataset.loc[:, "active_listing_count"] = dataset["active_listing_count"].map('{:,.0f}'.format)
        dataset.loc[:, "median_days_on_market"] = dataset["median_days_on_market"].map('{:,.0f}'.format)
        dataset.loc[:, "thirty_year_interest_rate"] = dataset["thirty_year_interest_rate"].map(str) + " %"
        dataset.loc[:, "thirty_year_interest_rate_five"] = dataset["thirty_year_interest_rate_five"].map(str) + " %"
        

        dataset.columns = ["County","Date","Med List Price","30 Yr Int Rate","30 Yr Int Rate (5lag)","Active Listings","Med Days on Market"]
        
        res = jsonify({'htmlresponse':render_template('modal/modal_county_dataset.html',county_name=county_name,
        tables=[dataset.to_html()],titles=[''])})
        return res

        # county_name = request.form["county_name"]

        # mao = ao(county_name)

        # dataset_json = mao.get_df_as_json() 


        # output_object = "var dataSet = " + dataset_json.replace("\'","'") + ";"


        # res = jsonify({'htmlresponse':render_template('modal/modal_county_dataset.html',
        #         county_name=county_name,
        #         dataset_json=output_object)})
                
        # return res



@section_5.route('/get_county_json', methods=['POST', 'GET'])
def get_county_json():

        args = request.args

        county_name = args.get("county_name")

        mao = ao(county_name)

        dataset_json =  mao.get_df_as_json()  


        print(dataset_json)

        output = dict()
        output["data"] = dataset_json

        print(json.dumps(output))

        res = jsonify(dataset_json)
                
        return res


@section_5.route('/test_jqgrid', methods=['POST', 'GET'])
def test_jqgrid():

        locale.setlocale( locale.LC_ALL, 'en_CA.UTF-8' )
        args = request.args

        county_name = args.get("county_name")

        mao = ao(county_name)

        dataset =  mao.get_county_df() 
        dataset.loc[:, "median_listing_price"] ='$'+ dataset["median_listing_price"].map('{:,.0f}'.format)
        dataset.loc[:, "active_listing_count"] =dataset["active_listing_count"].map('{:,.0f}'.format)
        dataset.loc[:, "thirty_year_interest_rate"] =dataset["thirty_year_interest_rate"].map(str) + " %"
        dataset.loc[:, "thirty_year_interest_rate_five"] =dataset["thirty_year_interest_rate_five"].map(str) + " %"


        #http://192.168.50.234:5023/test_jqgrid?county_name=los_angeles_ca

        dataset.columns = ["County","Date","Med List Price","30 Yr Int Rate","30 Yr Int Rate (5lag)","Active Listings"]

        # converting csv to html
        # data = pd.read_csv('sample_data.csv')
        # return render_template('table.html', tables=[data.to_html()], titles=[''])

        res = make_response(render_template('pages/placeholder.jqgrid.html',county_name=county_name,
        tables=[dataset.to_html()],titles=['']))
        return res
