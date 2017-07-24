from fee_calc.reducer import generate_list, generate_report, reduce_report
from flask import Blueprint
from flask import g, jsonify, render_template


blueprint = Blueprint('front', __name__.split('.')[0])


@blueprint.route('/')
def front():
    list = generate_list(g.fee_file)
    report = generate_report(g.fee_file)
    summarized_report = reduce_report(report)
    return render_template('front.html', list=list, report=report, summarized_report=summarized_report)
