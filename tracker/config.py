class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '123456'
    SQLALCHEMY_DATABASE_URI = "postgresql://tracker:123456@localhost/tracker"
