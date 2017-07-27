from json import load


def parse(config_path):
    with open(config_path) as file:
        json_conf = load(file)
    return json_conf
