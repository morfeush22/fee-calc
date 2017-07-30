from fee_calc.database import db
from fee_calc.models import Fee
from fee_calc.reducer import generate_list, generate_report, generate_reduced_report
from flask import Blueprint, g, jsonify, redirect, request, url_for


blueprint = Blueprint('back', __name__.split('.')[0])


@blueprint.route('/api/root_user', methods=['GET'])
def root_user():
    return jsonify(g.root_user)


@blueprint.route('/api/users', methods=['GET'])
def users():
    return jsonify(g.users)


@blueprint.route('/api/list', methods=['GET'])
def list():
    return jsonify(generate_list())


@blueprint.route('/api/report', methods=['GET'])
def report():
    return jsonify(generate_report())


@blueprint.route('/api/summarized_report', methods=['GET'])
def summarized_report():
    return jsonify(generate_reduced_report())


@blueprint.route('/api/send_fee', methods=['GET'])
def send_fee():
    payee = request.args.get('payee')
    acceptor = request.args.get('acceptor')
    balance = float(request.args.get('balance'))
    description = request.args.get('description')
    with db.engine.transaction() as c:
        if not hasattr(c.root, 'fees'):
            c.root.fees = []
        c.root.fees.append(Fee(payee, acceptor, balance, description))
    return redirect(url_for('front.front'))
