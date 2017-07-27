from fee_calc.reducer import generate_list, generate_report, generate_reduced_report
from flask import Blueprint
from flask import g, jsonify, render_template


blueprint = Blueprint('front', __name__.split('.')[0])


@blueprint.route('/')
def front():
    list = generate_list()
    report = generate_report()
    reduced_report = generate_reduced_report()
    return render_template('front.html', list=list, report=report, reduced_report=reduced_report)
