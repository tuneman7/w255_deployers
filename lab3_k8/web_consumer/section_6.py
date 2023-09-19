from includes import *
from flask import Blueprint

section_6 = Blueprint('section_6', __name__)


# @section_6.route('/section_six', methods=['POST', 'GET'])
# def section_six():

#     res = make_response(render_template('pages/section_content/placeholder.section.html',
#             section_number="six"))
#     return res

@section_6.route('/section_six', methods=['POST', 'GET'])
def section_one():
    res = make_response(render_template('pages/section_content/placeholder.post_mortem.html',
            section_number="one"))
    return res

from datetime import datetime
from libraries.analysis_object import analysis_object as ao

@section_6.route("/render_post_mortem",methods=["POST","GET"])
def render_post_mortem():

    t0 = datetime(1, 1, 1)
    now = datetime.utcnow()
    seconds = (now - t0).total_seconds()
    ticks = seconds * 10**7

    #my_altair = AltairRenderings()
    utility = Utility()
    print("render_post_mortem()")
    event_name = "post_mortem_section"
    slide_no="1"
    chart_json=None
    event_text=None
    slide_no = None
    post_mortem_image=None
    event_texta=None
    event_textb=None
    post_mortem_image_width=None
    post_mortem_image_height=None
    tag = None    
    if request.method == 'POST':
        event_name = request.form["event_name"]
        slide_no = request.form["post_mortem_slide_no"]

    try:
        file_name = event_name.lower() +"_"+ slide_no+".txt"
        load_file_name = os.path.join(utility.get_this_dir(),"data","post_mortem",file_name)
        print(load_file_name)
        event_text = utility.get_data_from_file(load_file_name)
        post_mortem_image = event_name.lower() +"_"+ slide_no+".png" + "?"+str(ticks)
        post_mortem_image = "./" + "static"+"/images"+"/post_mortem/"+post_mortem_image

    except Exception as e:
        fido="dido"
        print(e)


    if slide_no == "1":
        tag = "Post Mortem: Improvements to Model Interaction"
        fido="dido"
        post_mortem_image_width=1096
        post_mortem_image_height=600

    if slide_no == "2":
        tag = "Post Mortem: Better and More Data"
        fido="dido"
        post_mortem_image_width=1096
        post_mortem_image_height=600


    event_texta = None    
    event_textb = None

        #print(event_texta)
    if slide_no == "3":
        tag = "Post Mortem: Better and More Data"
        fido="dido"
        post_mortem_image_width=1096
        post_mortem_image_height=600

    if slide_no == "4":
        tag = "Post Mortem: Effect of Rental Market on Homebuying Market"
        fido="dido"
        post_mortem_image_width=1093
        post_mortem_image_height=434

    if slide_no == "5":
        tag = "Post Mortem: Personalized Advice With Tax Carrying Cost Included"
        fido="dido"
        post_mortem_image_width=1093
        post_mortem_image_height=434


    post_mortem_slides_total = 5

    return jsonify({'htmlresponse': render_template('modal/post_mortem.html',event_name=event_name,
    tag=tag,
    post_mortem_image=post_mortem_image,
    event_text=event_text,
    event_texta=event_texta,
    event_textb=event_textb,
    post_mortem_image_width=post_mortem_image_width,
    post_mortem_image_height=post_mortem_image_height,
    post_mortem_slide_no=slide_no,
    post_mortem_slides_total=post_mortem_slides_total)})    