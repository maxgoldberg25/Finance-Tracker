class Config:
    SECRET_KEY = 'dev'  # Use a dynamic environment variable in production
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False