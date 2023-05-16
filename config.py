import os

class Config(object):
    USERNAME = os.getenv('DB_USERNAME')
    PASSWORD = os.getenv('DB_PASSWORD')
    HOST = os.getenv('DB_HOST')
    DATABASE = os.getenv('DB_DATABASE')
    #dialect://username:password@host:port/database
    SQLALCHEMY_DATABASE_URI = 'postgresql://' +USERNAME+':'+PASSWORD+'@'+HOST+'/'+DATABASE
    # SQLALCHEMY_TRACK_MODIFICATION = False
    # SQLALCHEMY_RECORD_QUERIES = True

