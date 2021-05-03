import os

from flask import Flask, render_template, url_for


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'djd.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # if it's in testing then it'll grab the test config
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
 
    """
    # db init
    from . import db
    db.init_app(app)

    return app    
    """


    # index view
    @app.route('/')
    def index():
        return render_template('index.html')
    

    # blog read view
    @app.route('/blog')
    def blog():
        return 'This is my blog. These thoughts are my own.'
    
    return app
