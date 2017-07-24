from fee_calc.reducer import generate_list, generate_report, reduce_report
from flask import Blueprint, g, jsonify, redirect, request, url_for


blueprint = Blueprint('back', __name__.split('.')[0])


@blueprint.route('/api/users', methods=['GET'])
def users():
    return jsonify(g.users)


@blueprint.route('/api/list', methods=['GET'])
def list():
    return jsonify(generate_list(g.fee_file))


@blueprint.route('/api/report', methods=['GET'])
def report():
    return jsonify(generate_report(g.fee_file))


@blueprint.route('/api/summarized_report', methods=['GET'])
def summarized_report():
    return jsonify(reduce_report(generate_report(g.fee_file)))


@blueprint.route('/api/send_fee', methods=['GET'])
def send_fee():
    payee = request.args.get('payee')
    acceptor = request.args.get('acceptor')
    fee = request.args.get('fee')
    with open(g.fee_file, "a") as file:
        file.write(','.join([payee, acceptor, fee]) + '\n')
    return redirect(url_for('front.front'))
