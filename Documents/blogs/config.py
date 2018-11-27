import os



class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'

        # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    '''
    General configuration parent class
    '''

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschoolcom:mids@localhost/blog'



class DevConfig(Config):

    '''
    Development  configuration child class
    '''
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschoolcom:mids@localhost/blog'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    '''
    Production  configuration child class
    '''


config_options={
'production':ProdConfig,
'development':DevConfig
}
