import os
import sqlite3

from src.service.constants import Database


def connect():
    """
    We execute the connection with the database, initializing the
    connection as 'None' and we set the PATH and the NAME of the database.
    """
    conn = None
    try:
        conn = sqlite3.connect(os.path.join(Database.DATA_PATH, Database.DB_FILE))
    except OSError as e:
        print(e)
    return conn