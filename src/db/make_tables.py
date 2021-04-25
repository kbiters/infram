import sqlite3

from src.db.connect import connect
from src.service.constants import Database


def create_db_tables():
    conn = connect()
    try:
        for i in Database.DICT_MAKE_TABLES:
            conn.execute(i)

        set_data_db()

    except sqlite3.OperationalError as error:
        print(error)
    conn.close()


def set_data_db():
    conn = connect()
    for i in Database.LIST_TABLES:
        conn.execute(f"insert into {i}(WIN_MIN,WIN_MAX,TIME_END,TIME_TO_REPEAT,POWER_OFF) values (?,?,?,?,?)",
                     (Database.WIN_MIN, Database.WIN_MAX, Database.TIME_END, Database.TIME_TO_REPEAT,
                      Database.POWER_OFF))
    conn.commit()
    conn.close()
