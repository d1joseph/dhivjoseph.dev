import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev', # replace this with your own
        DATABASE=os.path.join(app.instance_path, 'mysite.sqlite'),
    )

    if test_config is None:
        # load the instance config, it it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    
    # validate instance folder
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def home():
        return 'Home page'

    @app.route('/hello')
    def index():
        return 'Hello, world!'
    
    return app