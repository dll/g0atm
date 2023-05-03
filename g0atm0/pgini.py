# pip install python_dotenv
import os
from dotenv import find_dotenv, load_dotenv


class PgIni:
    def __init__(self):
        load_dotenv(find_dotenv("pg.env"))

    def get_pg_host(self):
        return os.getenv("host")

    def get_pg_port(self):
        return os.getenv("port")

    def get_pg_user(self):
        return os.getenv("user")

    def get_pg_pwd(self):
        return os.getenv("password")

    def get_pg_dbname(self):
        return os.getenv("dbname")
