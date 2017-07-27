#!/usr/bin/python3

from fee_calc import configuration_parser
from fee_calc.database import db, setup_db
from fee_calc.models import Fee
from itertools import permutations
import argparse
import configparser


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('CONFIG_FILE', type=str)
    return parser.parse_args()


def get_json_config_path(config_path):
    parser = configparser.ConfigParser()
    parser.optionxform = lambda item: item
    parser.read(config_path)
    return parser['app:main']['json']


def populate_db(users):
    with db.engine.transaction() as c:
        c.root.fees = []
        fees = c.root.fees
        for payee, acceptor in permutations(users, 2):
            fees.append(Fee(payee, acceptor, 100))


def print_db():
    with db.engine.transaction() as c:
        for fee in c.root.fees:
            print(fee)


def main():
    args = get_args()
    json_config_path = get_json_config_path(args.CONFIG_FILE)
    json_conf = configuration_parser.parse(json_config_path)
    setup_db(json_conf['zodb'])
    populate_db(json_conf['app']['users'])
    print_db()


if __name__ == '__main__':
    main()
