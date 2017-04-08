from flask import Flask, request

from pyrachnid.assets import assets
from pyrachnid.config import app_config
from pyrachnid.main import main as main_blueprint


def create_app(app_env):
    app = Flask(__name__)
    app.config.from_object(app_config[app_env])

    app.register_blueprint(main_blueprint, url_prefix='')

    assets.init_app(app)

    @app.before_request
    def clear_cache():
        if 'localhost' in request.host_url:
            app.jinja_env.cache = {}

    return app