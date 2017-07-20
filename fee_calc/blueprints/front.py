from flask import Blueprint
from flask import render_template


blueprint = Blueprint('front', __name__.split('.')[0])


@blueprint.route('/')
def front():
    return render_template('front.html')
