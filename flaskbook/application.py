from flask import Flask
from flask.ext.mongoengine import MongoEngine

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    
    from user.views import user_app
    app.register_blueprint(user_app)
    
    return app
    