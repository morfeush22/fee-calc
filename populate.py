#!/usr/bin/python3

from fee_calc import configuration_parser
from fee_calc.database import db, setup_db
from fee_calc.models import Fee
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


def populate_db():
    with db.engine.transaction() as c:
        c.root.fees = []
        fees = c.root.fees
        fees.append(Fee('a', 'k', 309.33))
        fees.append(Fee('a', 'm', 127.99))
        fees.append(Fee('k', 'a', 603.79))
        fees.append(Fee('k', 'm', 708.22))
        fees.append(Fee('m', 'a', 59.99))
        fees.append(Fee('m', 'k', 64.55))


def print_db():
    with db.engine.transaction() as c:
        for fee in c.root.fees:
            print(fee)


def main():
    args = get_args()
    json_config_path = get_json_config_path(args.CONFIG_FILE)
    json_conf = configuration_parser.parse(json_config_path)
    setup_db(json_conf['zodb'])
    populate_db()
    print_db()


if __name__ == '__main__':
    main()
