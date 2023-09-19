from includes import *
from flask import Blueprint

section_1 = Blueprint('section_one', __name__)




@section_1.route("/videomodaldata",methods=["POST","GET"])
def render_video_modal():
    video_url = request.form["video_url"]
    video_title = request.form["title"]

    return jsonify({'htmlresponse': render_template('modal/video_modal.html',
                    video_url=video_url,
                    video_modal_title_text=video_title
                    )}
                )


@section_1.route("/videomodaldataparam",methods=["POST","GET"])
def render_video_modal_param():

    video_modal="videomodal_canned"
    return jsonify({'htmlresponse': render_template('modal/video_modal_param.html',
    video_modal=video_modal

    )})



@section_1.route('/intro', methods=['POST', 'GET'])
def intro():

    

    res = make_response(render_template('pages/section_content/placeholder.introduction.html',
            section_number="one"))
    return res

@section_1.route('/section_one', methods=['POST', 'GET'])
def section_one():
    res = make_response(render_template('pages/section_content/placeholder.mission_statement.html',
            section_number="one"))
    return res

from datetime import datetime
from libraries.analysis_object import analysis_object as ao

@section_1.route("/render_mission_statement",methods=["POST","GET"])
def render_mission_statement():

    t0 = datetime(1, 1, 1)
    now = datetime.utcnow()
    seconds = (now - t0).total_seconds()
    ticks = seconds * 10**7

    #my_altair = AltairRenderings()
    utility = Utility()
    print("render_mission_statement()")
    event_name = "mission_statement_section"
    slide_no="1"
    chart_json=None
    event_text=None
    slide_no = None
    mission_image=None
    event_texta=None
    event_textb=None
    mission_image_width=None
    mission_image_height=None
    tag = None    
    if request.method == 'POST':
        event_name = request.form["event_name"]
        slide_no = request.form["mission_slide_no"]

    try:
        file_name = event_name.lower() +"_"+ slide_no+".txt"
        load_file_name = os.path.join(utility.get_this_dir(),"data","mission_statement",file_name)
        print(load_file_name)
        event_text = utility.get_data_from_file(load_file_name)
        mission_image = event_name.lower() +"_"+ slide_no+".png" + "?"+str(ticks)
        mission_image = "./" + "static"+"/images"+"/mission_statement/"+mission_image

    except Exception as e:
        fido="dido"
        print(e)


    if slide_no == "1":
        tag = "Success: When Prepration Meets Opportunity -- The Program and The Market"
        fido="dido"
        mission_image_width=1096
        mission_image_height=600

    if slide_no == "2":
        tag = "Success: When Prepration Meets Opportunity -- The Signal"
        fido="dido"
        mission_image_width=1096
        mission_image_height=600


    event_texta = None    
    event_textb = None

        #print(event_texta)
    if slide_no == "3":
        tag = "Mission Statement: Help Homebuyers Understand Market Cyclicality"
        file_name = event_name.lower() +"_"+ slide_no+"a.txt"
        load_file_name = os.path.join(utility.get_this_dir(),"data","mission_statement",file_name)
        print(load_file_name)
        event_texta = utility.get_data_from_file(load_file_name)
        file_name = event_name.lower() +"_"+ slide_no+"b.txt"
        load_file_name = os.path.join(utility.get_this_dir(),"data","mission_statement",file_name)
        print(load_file_name)
        event_textb = utility.get_data_from_file(load_file_name)
        mission_image = None        

    if slide_no == "4":
        tag = "Mission Statement: Give Homebuyers Tools Previously Reserved for Big Players"
        fido="dido"
        mission_image_width=1096
        mission_image_height=600


    mission_slides_total = 4

    return jsonify({'htmlresponse': render_template('modal/mission_statement.html',event_name=event_name,
    tag=tag,
    mission_image=mission_image,
    event_text=event_text,
    event_texta=event_texta,
    event_textb=event_textb,
    mission_image_width=mission_image_width,
    mission_image_height=mission_image_height,
    mission_slide_no=slide_no,
    mission_slides_total=mission_slides_total)})    


def get_signal_icon(signal):
    print("signal=",signal)
    image_path = "./static/images/predict_icons/thumbs_"+ signal +".png"
    return image_path


from libraries.analysis_object import analysis_object as ao
@section_1.route('/dealio', methods=['POST', 'GET'])
def dealio():

        mao = ao('los_angeles_ca')

        DOM_SIGNAL_DF,NO_MO_DOM_UP,NO_MO_DOM_DOWN,DOM_SIGNAL_GRAPH,DOM_SIGNAL,dom_this_year_count, dom_last_year_count,dom_this_year_higher,dom_pct_change = mao.do_dom_analysis()

        INT_SIGNAL_DF,NO_MO_INT_UP,NO_MO_INT_DOWN,INT_SIGNAL_GRAPH,INT_SIGNAL,int_this_year_count, int_last_year_count,int_this_year_higher,int_pct_change = mao.do_int_analysis()
        
        INV_SIGNAL_DF,NO_MO_INV_UP,NO_MO_INV_DOWN,INV_SIGNAL_GRAPH,INV_SIGNAL,inv_this_year_count, inv_last_year_count,inv_this_year_higher,inv_pct_change = mao.do_inv_analysis()

        PRICE_SIGNAL_DF,NO_MO_PRICE_UP,NO_MO_PRICE_DOWN,PRICE_SIGNAL_GRAPH,PRICE_SIGNAL,price_this_year_count, price_last_year_count,price_this_year_higher,price_pct_change = mao.do_price_analysis()

        inv_signal_gif = get_signal_icon(INV_SIGNAL)
        int_signal_gif = get_signal_icon(INT_SIGNAL)
        price_signal_gif = get_signal_icon(PRICE_SIGNAL)
        dom_signal_gif = get_signal_icon(DOM_SIGNAL)
        


        res = make_response(render_template('pages/placeholder.altair.html',
            section_number="one",
                chart_json = DOM_SIGNAL_GRAPH.to_json(),
                chart_json1=INT_SIGNAL_GRAPH.to_json(),
                chart_json2=INV_SIGNAL_GRAPH.to_json(),
                chart_json3=PRICE_SIGNAL_GRAPH.to_json(),
                inv_signal_gif=inv_signal_gif,
                int_signal_gif=int_signal_gif,
                price_signal_gif=price_signal_gif,
                dom_signal_gif=dom_signal_gif,
                overall_signal_gif=None))
        return res


@section_1.route('/section_onea', methods=['POST', 'GET'])
def section_onea():
    res = make_response(render_template('pages/section_content/placeholder.competition.html',
            section_number="one"))
    return res

from datetime import datetime


@section_1.route("/render_competition",methods=["POST","GET"])
def render_competition():
    #my_altair = AltairRenderings()
    utility = Utility()
    print("render_competition()")
    event_name = "competition_section"
    slide_no="1"
    chart_json=None
    event_text=None
    slide_no = None
    if request.method == 'POST':
        event_name = request.form["event_name"]
        slide_no = request.form["competition_slide_no"]

    t0 = datetime(1, 1, 1)
    now = datetime.utcnow()
    seconds = (now - t0).total_seconds()
    ticks = seconds * 10**7
    event_texta = None
    event_textb = None
    try:
        file_name = event_name.lower() +"_"+ slide_no+".txt"
        load_file_name = os.path.join(utility.get_this_dir(),"data","competition",file_name)
        print(load_file_name)
        event_text = utility.get_data_from_file(load_file_name)
        competition_image = event_name.lower() +"_"+ slide_no+".png?" + str(ticks)
        competition_image = "./" + "static"+"/images"+"/competition/"+competition_image
        file_name = event_name.lower() +"_"+ slide_no+"b.txt"
        load_file_name = os.path.join(utility.get_this_dir(),"data","competition",file_name)
        print(load_file_name)
        event_textb = utility.get_data_from_file(load_file_name)
        print(event_textb)


    except Exception as e:
        fido="dido"
        print(e)

    tag = "Competitive Landscape"
    slide_url = None
    if slide_no == "1":
        fido="dido"
        competition_image_width=1200
        competition_image_height=700
    if slide_no == "2":
        tag = "REDFIN"
        competition_image_width=1000
        competition_image_height=625
        slide_url = "https://www.redfin.com/CA/Sherman-Oaks/4637-Willis-Ave-91403/unit-107/home/4816069"
    if slide_no == "3":
        tag = "REALTOR"
        competition_image_width=1000
        competition_image_height=625
        slide_url = "https://www.realtor.com/realestateandhomes-detail/M1489559208"
    if slide_no == "4":
        tag = "ZILLOW"
        competition_image_width=1000
        competition_image_height=625
        slide_url = "https://www.zillow.com/homes/4637-Willis-Ave-Unit-107,-Sherman-Oaks,-CA-91403_rb/19982950_zpid/"
    if slide_no == "5":
        tag = "CORELOGIC"
        competition_image_width=1000
        competition_image_height=400        
    if slide_no == "6":
        tag = "The MIDS Home Market Advisor Advantage"
        competition_image_width=1000
        competition_image_height=625
        file_name = event_name.lower() +"_"+ slide_no+"a.txt"
        load_file_name = os.path.join(utility.get_this_dir(),"data","competition",file_name)
        print(load_file_name)
        event_texta = utility.get_data_from_file(load_file_name)
        competition_image = None
    if slide_no == "7":
        tag = "The MIDS Home Market Advisor Advantage"
        competition_image_width=1000
        competition_image_height=625
    if slide_no == "8":
        tag = "The MIDS Home Market Advisor Advantage"
        competition_image_width=1000
        competition_image_height=625
    if slide_no == "9":
        tag = "The MIDS Home Market Advisor Advantage"
        competition_image_width=1000
        competition_image_height=625

    same_app_url = None
    if slide_no == "10":
        tag = "The MIDS Home Market Advisor Advantage"
        same_app_url = "#section_five"
        competition_image_width=1000
        competition_image_height=625



    competition_slides_total = 10

    return jsonify({'htmlresponse': render_template('modal/competition.html',event_name=event_name,
    competition_image=competition_image,
    tag=tag,
    event_textb=event_textb,
    same_app_url=same_app_url,
    event_text=event_text,
    event_texta=event_texta,
    slide_url=slide_url,
    competition_image_width=competition_image_width,
    competition_image_height=competition_image_height,
    competition_slide_no=slide_no,
    competition_slides_total=competition_slides_total)})    


