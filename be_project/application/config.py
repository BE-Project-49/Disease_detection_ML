import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class LocalDevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:omsharayu@localhost/DB"
    DEBUG = False
    UPLOAD_FOLDER ="./static/uploaded_images"
    ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])