class Config:
    DEBUG: True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://felipe:fe123@localhost/smilecook'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'chave super secreta'
    JWT_ERROR_MESSAGE_KEY = 'mensagem'