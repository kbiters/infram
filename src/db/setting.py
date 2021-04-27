from src.db import conn
from src.service.constants import Vars, Map, Message
from src.service.mapper import mapping
from src.service.translator import translate


def load_setting():
    try:
        cur = conn.cursor()
        opt = mapping(Map.TYPE_DB_MAP, int(input(Message.GET_TYPE_DB_USE)))
        cur.execute(f'SELECT WIN_MIN, WIN_MAX, TIME_END, TIME_TO_REPEAT, POWER_OFF FROM {opt}')
        rows = cur.fetchall()
        for row in rows:
            Vars.WIN_MIN, Vars.WIN_MAX, Vars.TIME_END, Vars.TIME_TO_REPEAT, Vars.POWER_OFF = row
    except OSError as error:
        print(translate(error))


def save_setting():
    return "proximamente..."
