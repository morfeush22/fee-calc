from collections import defaultdict
from fee_calc.database import db
from flask import g
from itertools import permutations


def generate_list():
    fees = []
    with db.engine.transaction() as c:
        for fee in c.root.fees:
            payee, acceptor, balance, *others = fee.as_list()
            fees.append([acceptor, payee, balance])
    return fees


def generate_report():
    rep = defaultdict(lambda: defaultdict(lambda: 0))
    with db.engine.transaction() as c:
        for fee in c.root.fees:
            payee, acceptor, balance, *others = fee.as_list()
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
    for payee, acceptor in permutations(set(rep.keys()) - set(root_user)):
        balance = rep[payee][acceptor]
        rep[payee][acceptor] -= balance
        rep[root_user][acceptor] += balance
        rep[root_user][payee] -= balance


def generate_reduced_report():
    rep = generate_report()
    reduce_self(rep, g.root_user)
    reduce_others(rep, g.root_user)
    return rep[g.root_user]
