import os
from flask import Flask
from flask_restful import Resource,Api
from application.config import LocalDevelopmentConfig
from flask_cors import CORS
app = None
api = None


def create_app():
    app = Flask(__name__, template_folder="templates")
    if os.getenv('ENV', "development") == "production":
      raise Exception("Currently no production config is setup.")
    else:
      print("Staring Local Development")
      app.config.from_object(LocalDevelopmentConfig)
    api = Api(app)
    
    cors = CORS(app, resources={r"/upload": {"origins": "*"}})
    app.app_context().push()  
    return app,api

app,api = create_app()

# Import all the controllers so they are loaded
from application.controllers import *

from application.api import *

api.add_resource(modelAPI, "/api/predict/<string:image>")

if __name__ == '__main__':
  # Run the Flask app
  app.run(host='0.0.0.0',port=8080)
