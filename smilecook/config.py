class Config:
    DEBUG: True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://felipe:fe123@localhost/smilecook'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'seuper-secret-key'
    JWT_ERROR_MESSAGE_KEY = 'message'

    #configuração para black-list
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECK = ['access','refresh']

