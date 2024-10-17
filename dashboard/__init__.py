# import flask module from Flask package
from flask import Flask 

# import flask - from the package import a module
from flask import Flask

def create_app():
    print(__name__)  # let us be curious - what is this __name__
    app = Flask(__name__)  # this is the name of the module/package that is calling this app
    app.debug = True
    # add the Blueprint
    from . import views
    app.register_blueprint(views.mainbp)
    return app

