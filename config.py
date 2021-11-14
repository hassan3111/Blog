import os


class Config:
    SECRET_KEY = 'DZO3PQkI_yJy8e-2u_7Feg'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://access:34567@localhost/hassan'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    QUOTES_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587 
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'aliimohamud185@gmail.com'
    MAIL_PASSWORD = '0746881243A'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI =SQLALCHEMY_DATABASE_URI.replace("postgres://","postgresql://",1)

class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://access:34567@localhost/hassan'
    
    DEBUG = True   

config_options = {
'development':DevConfig,
'production':ProdConfig
}
