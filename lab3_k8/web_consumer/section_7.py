from includes import *
from flask import Blueprint

section_7 = Blueprint('section_7', __name__)


@section_7.route('/section_seven', methods=['POST', 'GET'])
def section_seven():

    res = make_response(render_template('pages/section_content/placeholder.about.html',
            section_number="seven"))
    return res