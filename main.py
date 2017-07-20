from fee_calc import application, configuration_parser
from fee_calc.blueprints import back, front
from flask import g


def build_application(config):
    app_instance = application.application_factory()
    app_instance.config.from_mapping(config)
    application.register_blueprints(app_instance, [back.blueprint, front.blueprint])
    return app_instance


def setup_app(app, app_config):
    @app.before_request
    def setup():
        g.users = app_config['users']
        g.fee_file = app_config['fee_file']


def wsgi(global_config, **local_config):
    config = configuration_parser.parse(local_config)
    flask_config = config['flask']
    app = build_application(flask_config)
    setup_app(app, config)
    return app
