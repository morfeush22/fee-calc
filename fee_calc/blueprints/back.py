from fee_calc.reducer import generate_report, reduce_report
from flask import Blueprint, g, jsonify


blueprint = Blueprint('back', __name__.split('.')[0])


@blueprint.route('/api/users', methods=['GET'])
def users():
    return jsonify(g.users)


@blueprint.route('/api/report', methods=['GET'])
def report():
    return jsonify(generate_report('./example.txt'))


@blueprint.route('/api/summarized_report', methods=['GET'])
def summarized_report():
    return jsonify(reduce_report(generate_report('./example.txt')))
