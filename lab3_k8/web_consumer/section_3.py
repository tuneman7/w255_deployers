from includes import *
from flask import Blueprint

section_3 = Blueprint('section_3', __name__)



from libraries.data_objects import data_objects as do

@section_3.route('/section_three', methods=['POST', 'GET'])
def section_three():
        #print("mybozo")
        my_data = do()
        econ_concepts = my_data.get_world_event_data();
        #print(econ_concepts)
        #    return jsonify({'htmlresponse': render_template('pages/section_content/econ_concepts.html',econ_concepts=econ_concepts)})
        return jsonify({'htmlresponse': render_template('pages/section_content/econ_concepts.html',econ_concepts=econ_concepts)})


@section_3.route("/render_econ_descriptions",methods=["POST","GET"])
def render_world_event_graphs():
    #my_altair = AltairRenderings()
    utility = Utility()
    print("render_econ_descriptions()")
    event_name = "JCPOA"
    is_json_graph = True
    chart_json=None
    event_text=None
    slide_no = None
    image_path = None
    event_hyperlink = None
    flip_animation = False
    image_width = None
    image_height = None
    specify_heigh_width = False

    if request.method == 'POST':
        event_name = request.form["concept"]
        slide_no = request.form["slide_no"]

    try:
        file_name = event_name.lower().replace(" ","_") +"_"+ slide_no+".txt"
        load_file_name = os.path.join(utility.get_this_dir(),"data","econ_concepts",file_name)
        print(load_file_name)
        event_text = utility.get_data_from_file(load_file_name)
    except:
        fido="dido"

    if event_name.lower() == "economics":
        if slide_no == "1":
            print("event no=",slide_no)
            is_json_graph = False
            chart_json = None
            event_hyperlink = "https://eml.berkeley.edu/~jaya/lecture/Econ1_lecture1.pdf"
            image_path = "./static/images/econ_concepts/slide_1.jpeg"
            print(event_hyperlink)        

        if slide_no == "2":
            print("event no=",slide_no)
            is_json_graph = False
            chart_json = None
            image_width = 400
            image_height = 300
            specify_heigh_width = True            
            event_hyperlink = "https://eml.berkeley.edu/~jaya/lecture/Econ1_lecture1.pdf"
            image_path = "./static/images/econ_concepts/econ_overview.webp"
            print(event_hyperlink)        

        if slide_no == "3":
            print("event no=",slide_no)
            is_json_graph = False
            chart_json = None
            image_width = 550
            image_height = 400
            specify_heigh_width = True            
            event_hyperlink = "https://eml.berkeley.edu/~jaya/lecture/Econ1_lecture1.pdf"
            image_path = "./static/images/econ_concepts/micro.png"
            print(event_hyperlink)        

        if slide_no == "4":
            print("event no=",slide_no)
            is_json_graph = False
            chart_json = None
            image_width = 550
            image_height = 400
            specify_heigh_width = True            
            event_hyperlink = "https://eml.berkeley.edu/~jaya/lecture/Econ1_lecture1.pdf"
            image_path = "./static/images/econ_concepts/macro.png"
            print(event_hyperlink)        

        if slide_no == "5":
            print("event no=",slide_no)
            is_json_graph = False
            chart_json = None
            image_width = 750
            image_height = 650
            specify_heigh_width = True            
            event_hyperlink = "https://eml.berkeley.edu/~jaya/lecture/Econ1_lecture1.pdf"
            image_path = "./static/images/econ_concepts/macro_vs_micro.jpeg"
            print(event_hyperlink)        

        if slide_no == "6":
            print("event no=",slide_no)
            is_json_graph = False
            chart_json = None
            image_width = 550
            image_height = 650
            specify_heigh_width = True            
            event_hyperlink = "https://eml.berkeley.edu/~jaya/lecture/Econ1_lecture1.pdf"
            image_path = "./static/images/econ_concepts/rational_behavior_assumption.png"
            print(event_hyperlink)        


        #demand curve
    if event_name.lower() == "demandcurve":
        if slide_no == "1":
            print("event no=",slide_no)
            is_json_graph = False
            chart_json = None
            image_width = 550
            image_height = 300
            specify_heigh_width = True              
            event_hyperlink = "https://eml.berkeley.edu/~jaya/lecture/Econ1_lecture1.pdf"
            image_path = "./static/images/econ_concepts/pizza_demand_graph.png"
            print(event_hyperlink)        

        if slide_no == "2":
            print("event no=",slide_no)
            is_json_graph = False
            chart_json = None
            image_width = 550
            image_height = 300
            specify_heigh_width = True            
            event_hyperlink = "https://eml.berkeley.edu/~jaya/lecture/Econ1_lecture1.pdf"
            image_path = "./static/images/econ_concepts/pizza_demand_words.png"
            print(event_hyperlink)        

        if slide_no == "3":
            print("event no=",slide_no)
            is_json_graph = False
            chart_json = None
            image_width = 650
            image_height = 400
            specify_heigh_width = True            
            event_hyperlink = "https://eml.berkeley.edu/~jaya/lecture/Econ1_lecture1.pdf"
            image_path = "./static/images/econ_concepts/supply_and_demand_curves.jpeg"
            print(event_hyperlink)        

        if slide_no == "4":
            print("event no=",slide_no)
            is_json_graph = False
            chart_json = None
            image_width = 700
            image_height = 400
            specify_heigh_width = True            
            event_hyperlink = "https://en.wikipedia.org/wiki/Substitute_good"
            image_path = "./static/images/econ_concepts/substitute_chart.jpeg"
            print(event_hyperlink)        

        #carrying costs
    if event_name.lower() == "carryingcosts":
        if slide_no == "1":
            print("event no=",slide_no)
            is_json_graph = False
            chart_json = None
            image_width = 550
            image_height = 300
            specify_heigh_width = True              
            event_hyperlink = "https://en.wikipedia.org/wiki/Cost_of_carry"
            image_path = "./static/images/econ_concepts/carrying_costs.jpg"
            print(event_hyperlink)        

        if slide_no == "2":
            print("event no=",slide_no)
            is_json_graph = False
            chart_json = None
            image_width = 650
            image_height = 300
            specify_heigh_width = True            
            event_hyperlink = "https://en.wikipedia.org/wiki/Cost_of_carry"
            image_path = "./static/images/econ_concepts/property_holding_costs.jpeg"
            print(event_hyperlink)        

        if slide_no == "3":
            print("event no=",slide_no)
            is_json_graph = False
            chart_json = None
            image_width = 650
            image_height = 300
            specify_heigh_width = True            
            event_hyperlink = "https://en.wikipedia.org/wiki/Cost_of_carry"
            image_path = "./static/images/econ_concepts/what_carry_costs_should_be_2.jpeg"
            print(event_hyperlink)        

        #carrying costs
    if event_name.lower() == "leverage":
        if slide_no == "1":
            print("event no=",slide_no)
            is_json_graph = False
            chart_json = None
            image_width = 550
            image_height = 300
            specify_heigh_width = True              
            event_hyperlink = "https://en.wikipedia.org/wiki/Leverage_(finance)"
            image_path = "./static/images/econ_concepts/10_to_1_leverage.jpeg"
            print(event_hyperlink)        

        if slide_no == "2":
            print("event no=",slide_no)
            is_json_graph = False
            chart_json = None
            image_width = 750
            image_height = 300
            specify_heigh_width = True              
            event_hyperlink = "https://en.wikipedia.org/wiki/Leverage_(finance)"
            image_path = "./static/images/econ_concepts/leverage_example_gain_1.jpeg"
            print(event_hyperlink)        

        if slide_no == "3":
            print("event no=",slide_no)
            is_json_graph = False
            chart_json = None
            image_width = 750
            image_height = 300
            specify_heigh_width = True              
            event_hyperlink = "https://en.wikipedia.org/wiki/Leverage_(finance)"
            image_path = "./static/images/econ_concepts/leverage_example_loss.jpeg"
            print(event_hyperlink)        

        if slide_no == "4":
            print("event no=",slide_no)
            is_json_graph = False
            chart_json = None
            image_width = 650
            image_height = 300
            specify_heigh_width = True              
            event_hyperlink = "https://en.wikipedia.org/wiki/Leverage_(finance)"
            image_path = "./static/images/econ_concepts/lehman_leverage.png"
            print(event_hyperlink)        


        #carrying costs
    if event_name.lower() == "marketirrationality":
        if slide_no == "1":
            print("event no=",slide_no)
            is_json_graph = False
            chart_json = None
            image_width = 550
            image_height = 300
            specify_heigh_width = True              
            event_hyperlink = "https://www.investopedia.com/terms/i/irrationalexuberance.asp"
            image_path = "./static/images/econ_concepts/irrational_markets.png"
            print(event_hyperlink)        

        if slide_no == "2":
            print("event no=",slide_no)
            is_json_graph = False
            chart_json = None
            image_width = 550
            image_height = 300
            specify_heigh_width = True              
            event_hyperlink = "https://insights.som.yale.edu/insights/do-homebuyers-expectations-align-with-reality"
            image_path = "./static/images/econ_concepts/narrative-economics-summary.jpeg"
            print(event_hyperlink)        




    if event_name.lower() == "featuresofhousecost":
        if slide_no == "1":
            print("event no=",slide_no)
            is_json_graph = False
            chart_json = None
            image_width = 550
            image_height = 300
            specify_heigh_width = True              
            event_hyperlink = "https://en.wikipedia.org/wiki/Leverage_(finance)"
            image_path = "./static/images/econ_concepts/school_districts.jpeg"
            print(event_hyperlink)        

        if slide_no == "2":
            print("event no=",slide_no)
            is_json_graph = False
            chart_json = None
            image_width = 550
            image_height = 300
            specify_heigh_width = True              
            event_hyperlink = "https://en.wikipedia.org/wiki/Leverage_(finance)"
            image_path = "./static/images/econ_concepts/school_districts_1.jpeg"
            print(event_hyperlink)        

        if slide_no == "3":
            print("event no=",slide_no)
            is_json_graph = False
            chart_json = None
            image_width = 550
            image_height = 300
            specify_heigh_width = True              
            event_hyperlink = "https://en.wikipedia.org/wiki/Leverage_(finance)"
            image_path = "./static/images/econ_concepts/school_districts_2.jpg"
            print(event_hyperlink)        

        if slide_no == "4":
            print("event no=",slide_no)
            is_json_graph = False
            chart_json = None
            image_width = 550
            image_height = 300
            specify_heigh_width = True              
            event_hyperlink = "https://en.wikipedia.org/wiki/Leverage_(finance)"
            image_path = "./static/images/econ_concepts/foreclosures_1.jpeg"
            print(event_hyperlink)


        if slide_no == "5":
            print("event no=",slide_no)
            is_json_graph = False
            chart_json = None
            image_width = 550
            image_height = 300
            specify_heigh_width = True              
            event_hyperlink = "https://en.wikipedia.org/wiki/Leverage_(finance)"
            image_path = "./static/images/econ_concepts/foreclosures_2.jpeg"
            print(event_hyperlink)

        if slide_no == "6":
            print("event no=",slide_no)
            is_json_graph = False
            chart_json = None
            image_width = 550
            image_height = 300
            specify_heigh_width = True              
            event_hyperlink = "https://en.wikipedia.org/wiki/Leverage_(finance)"
            image_path = "./static/images/econ_concepts/foreclosures.jpg"
            print(event_hyperlink)

        if slide_no == "7":
            print("event no=",slide_no)
            is_json_graph = False
            chart_json = None
            image_width = 550
            image_height = 300
            specify_heigh_width = True              
            event_hyperlink = "https://en.wikipedia.org/wiki/Leverage_(finance)"
            image_path = "./static/images/econ_concepts/covid_1.jpeg"
            print(event_hyperlink)

        if slide_no == "8":
            print("event no=",slide_no)
            is_json_graph = False
            chart_json = None
            image_width = 550
            image_height = 300
            specify_heigh_width = True              
            event_hyperlink = "https://en.wikipedia.org/wiki/Leverage_(finance)"
            image_path = "./static/images/econ_concepts/covid_2.jpeg"
            print(event_hyperlink)

    return jsonify({'htmlresponse': render_template('modal/econ_concepts.html',
    event_name=event_name,
    chart_json=chart_json,
    event_text=event_text,
    event_hyperlink=event_hyperlink,
    image_path=image_path,
    flip_animation=flip_animation,
    specify_heigh_width=specify_heigh_width,
    image_width=image_width,
    image_height=image_height)})

