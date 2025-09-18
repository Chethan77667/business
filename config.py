import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
    DEBUG = os.environ.get("FLASK_DEBUG", "1") == "1"


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True


config_by_name = {
    "development": DevelopmentConfig,
}


