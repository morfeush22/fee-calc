from collections import defaultdict
from fee_calc.database import db
from flask import g
from itertools import permutations


def generate_list():
    fees = []
    with db.engine.transaction() as c:
        for fee in c.root.fees:
            d = fee.as_dict()
            fees.append({
                'acceptor': d['acceptor'],
                'payee': d['payee'],
                'balance': d['balance'],
                'description': d['description'] if 'description' in d else ''
            })
    return fees


def generate_report():
    users = g.users
    rep = defaultdict(lambda: defaultdict(lambda: 0))
    for payee, acceptor in permutations(users, 2):
        rep[payee][acceptor] = 0
    with db.engine.transaction() as c:
        for fee in c.root.fees:
            payee, acceptor, balance, *others = fee.as_dict().values()
            rep[payee][acceptor] += balance
    return rep


def reduce_self(rep, root_user):
    for payee in (set(rep.keys()) - set(root_user)):
        for acceptor in rep[payee]:
            if acceptor == root_user:
                balance = rep[payee][acceptor]
                rep[acceptor][payee] -= balance
                rep[payee][acceptor] -= balance


def reduce_others(rep, root_user):
    for payee, acceptor in permutations(set(rep.keys()) - {root_user}, 2):
        balance = rep[payee][acceptor]
        rep[payee][acceptor] -= balance
        rep[root_user][acceptor] += balance
        rep[root_user][payee] -= balance


def generate_reduced_report():
    rep = generate_report()
    reduce_self(rep, g.root_user)
    reduce_others(rep, g.root_user)
    return rep[g.root_user]
