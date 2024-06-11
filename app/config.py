import os


def get_pass():
    return os.environ.get('POSTPASS')


def get_username():
    return "app_server"


def get_host():
    return "localhost"


def get_port():
    return 5432


def get_db_name():
    return "MedApp"


class Config(object):
    SQLALCHEMY_DATABASE_URI = f'postgresql://{get_username()}:{get_pass()}@{get_host()}:{get_port()}/{get_db_name()}'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
