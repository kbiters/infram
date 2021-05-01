import json
import sys

from src.json import config
from src.operations.functions import command
from src.service.constants import Message, Command, Data
from src.service.translator import translate


def show_menu():
    try:
        command(Command.CLEAR)
        print(Message.WELCOME)
        print(translate(Message.MENU))
        opt = int(input(translate(Message.GET_OPTION_MENU)))
        if 2 <= opt <= 3:
            check_opt(opt)
        elif opt == 4:
            sys.exit()
    except OSError as error:
        print(error)


def check_opt(opt_menu):
    if opt_menu == 2:
        get_configs()
    elif opt_menu == 3:
        set_vars()


def set_vars():
    try:
        config.set_win_min(int(input(translate(Message.SET_WIN_MIN))))
        config.set_win_max(int(input(translate(Message.SET_WIN_MAX))))
        config.set_time_to_repeat(float(input(translate(Message.SET_TIME_TO_REPEAT))) * 60)
        config.set_time_end(float(input(translate(Message.SET_TIME_END))) * 3600)
        config.set_power_off(True if input(translate(Message.SET_POWER_OFF) +
                                           Message.CHECK_YES_NO).lower() == "y" else False)
        config.apply_config()
    except OSError as error:
        print(translate(error))


def get_configs():
    try:
        with open(Data.DATA_PATH + Data.CONFIGS) as file:
            data = json.load(file)
            config.set_win_min(data.get('WIN_MIN'))
            config.set_win_max(data.get('WIN_MAX'))
            config.set_time_to_repeat(data.get('TIME_TO_REPEAT'))
            config.set_time_end(data.get('TIME_END'))
            config.set_power_off(data.get('POWER_OFF'))
    except OSError as error:
        print(error)
