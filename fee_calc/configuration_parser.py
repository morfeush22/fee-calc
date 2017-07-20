from json import loads


def parse(config):
    conf = dict()
    for k, v in config.items():
        try:
            traverse(conf, k.split('.'), v)
        except:
            raise Exception("Check configuration file!")
    return conf


def traverse(config, key_path, value):
    if len(key_path) > 1:
        if key_path[0] not in config:
            config[key_path[0]] = dict()
        traverse(config[key_path[0]], key_path[1:], value)
    else:
        config[key_path[0]] = loads(value)
