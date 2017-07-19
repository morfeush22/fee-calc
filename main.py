#!/usr/bin/python

from collections import defaultdict
from itertools import permutations
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('FEE_FILE', type=str)


def get_args():
    return parser.parse_args()


def parse_line(line):
    return line.strip().split(',')


def generate_report(fee_file):
    rep = defaultdict(lambda: defaultdict(lambda: 0))
    with open(fee_file, 'r') as file:
        for line in file:
            acceptor, payee, balance = parse_line(line)
            rep[payee][acceptor] += float(balance)
    return rep


def print_report(rep):
    out = list()
    for payee, acceptors in rep.items():
        for acceptor, balance in acceptors.items():
            out.append("{} -> {}: {}".format(
                acceptor,
                payee,
                balance
            ))
    print('\n'.join(sorted(out)))


def find_max_payee(rep):
    sum_per_payee = defaultdict(lambda: 0)
    for payee, acceptors in rep.items():
        for balance in acceptors.values():
            sum_per_payee[payee] += balance
    return max(sum_per_payee, key=lambda i: sum_per_payee[i])


def reduce_self(rep, max_payee):
    for payee in (set(rep.keys()) - set(max_payee)):
        for acceptor in rep[payee]:
            if acceptor == max_payee:
                balance = rep[payee][acceptor]
                rep[acceptor][payee] -= balance
                rep[payee][acceptor] -= balance


def reduce_others(rep, max_payee):
    for payee, acceptor in permutations(set(rep.keys()) - set(max_payee)):
        balance = rep[payee][acceptor]
        rep[payee][acceptor] -= balance
        rep[max_payee][acceptor] += balance
        rep[max_payee][payee] -= balance


def reduce(rep):
    reduced = dict(rep)
    max_payee = find_max_payee(reduced)
    reduce_self(reduced, max_payee)
    reduce_others(reduced, max_payee)
    return {i: reduced[i] for i in max_payee if i == max_payee}


def main():
    args = get_args()
    rep = generate_report(args.FEE_FILE)
    print("REPORT")
    print_report(rep)
    reduced = reduce(rep)
    print("\nREDUCED REPORT")
    print_report(reduced)


if __name__ == '__main__':
    main()
