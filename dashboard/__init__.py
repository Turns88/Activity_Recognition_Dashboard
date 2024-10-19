from flask import Flask
from flask_bootstrap import Bootstrap5
from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

def create_app():
    app = Flask(__name__)  
    app.debug = True

    # MongoDB client setupclient
    client = MongoClient(os.getenv("CONN_STR")) 
    db = client.assignment2b  
    app.config['db'] = db  # store db in config to access elsewhere

    from . import views
    app.register_blueprint(views.mainbp)
    return app

