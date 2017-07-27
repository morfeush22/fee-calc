from fee_calc import application, configuration_parser
from fee_calc.blueprints import back, front
from fee_calc.database import setup_db
from flask import g


def build_application(config):
    app_instance = application.application_factory()
    app_instance.config.from_mapping(config)
    application.register_blueprints(app_instance, [back.blueprint, front.blueprint])
    return app_instance


def setup_app(app, config):
    @app.before_request
    def setup():
        g.root_user = config['root_user']
        g.users = config['users']


def wsgi(global_config, **local_config):
    json_config_path = local_config['json']
    config = configuration_parser.parse(json_config_path)
    app = build_application(config['flask'])
    setup_app(app, config['app'])
    setup_db(config['zodb'])
    return app
