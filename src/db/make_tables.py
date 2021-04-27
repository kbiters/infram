import sqlite3

from src.db import conn
from src.service.constants import Vars, Database


def create_db_tables():
    try:
        for i in Database.DICT_MAKE_TABLES:
            conn.execute(i)

        set_data_db()

    except sqlite3.OperationalError as error:
        print(error)
    conn.close()


def set_data_db():
    for i in Database.LIST_TABLES:
        conn.execute(f"insert into {i}(WIN_MIN,WIN_MAX,TIME_END,TIME_TO_REPEAT,POWER_OFF) values (?,?,?,?,?)",
                     (Vars.WIN_MIN, Vars.WIN_MAX, Vars.TIME_END, Vars.TIME_TO_REPEAT, Vars.POWER_OFF))
    conn.commit()
    conn.close()
