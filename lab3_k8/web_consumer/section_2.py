from includes import *
from flask import Blueprint

section_2 = Blueprint('section_2', __name__)



@section_2.route('/section_two', methods=['POST', 'GET'])
def section_two():

    res = make_response(render_template('pages/section_content/placeholder.data_section.html',
            section_number="two"))
    return res

from datetime import datetime
@section_2.route("/render_data_statement",methods=["POST","GET"])
def render_data_statement():
    t0 = datetime(1, 1, 1)
    now = datetime.utcnow()
    seconds = (now - t0).total_seconds()
    ticks = seconds * 10**7    
    #my_altair = AltairRenderings()
    utility = Utility()
    print("render_data_statement()")
    event_name = "data_section"
    slide_no="1"
    chart_json=None
    event_text=None
    slide_no = None
    tag = None    

    if request.method == 'POST':
        event_name = request.form["event_name"]
        slide_no = request.form["data_slide_no"]

    try:
        file_name = event_name.lower() +"_"+ slide_no+".txt"
        load_file_name = os.path.join(utility.get_this_dir(),"data","our_data",file_name)
        print(load_file_name)
        event_text = utility.get_data_from_file(load_file_name)
        data_image = event_name.lower() +"_"+ slide_no+".png" + "?" +str(ticks)
        data_image = "./" + "static"+"/images"+"/our_data/"+data_image

    except Exception as e:
        fido="dido"
        print(e)


    if slide_no == "1":
        tag = "Our Data: We started with a wide net of public free datasets."
        fido="dido"
        data_image_width=935
        data_image_height=567
    if slide_no == "2":
        tag = "Our Data: Aggregation, Engineering, and Training Pipeline."
        fido="dido"
        data_image_width=935
        data_image_height=567
    if slide_no == "3":
        data_image_width=800
        data_image_height=200

    data_slides_total = 2

    return jsonify({'htmlresponse': render_template('modal/our_data.html',event_name=event_name,
    data_image=data_image,
    tag=tag,
    event_text=event_text,
    data_image_width=data_image_width,
    data_image_height=data_image_height,
    data_slide_no=slide_no,
    data_slides_total=data_slides_total)})    
