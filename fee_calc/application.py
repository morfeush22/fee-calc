def application_factory():
    from flask import Flask
    return Flask(__name__.split('.')[0], static_url_path='/static')


def register_blueprints(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def register_teardowns(app, teardowns):
    for teardown in teardowns:
        @app.teardown_appcontext
        def helper(error):
            teardown()
