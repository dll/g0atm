# pip install python_dotenv
import os
from dotenv import load_dotenv

load_dotenv();
def get_pg_host():
    return os.getenv("host");
def get_pg_port():
    return os.getenv("port");
def get_pg_user():
    return os.getenv("user");
def get_pg_pwd():
    return os.getenv("password");
def get_pg_dbname():
    return os.getenv("dbname");
