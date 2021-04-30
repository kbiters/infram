import sys

from src.json.config import get_configs, make_configs
from src.operations.functions import command
from src.service.constants import Message, Command, Vars
from src.service.translator import translate


def show_menu():
    try:
        command(Command.CLEAR)
        print(Message.WELCOME)
        print(translate(Message.MENU))
        opt = int(input(translate(Message.GET_OPTION_MENU)))
        if 1 <= opt <= 3:
            check_opt(opt)
        else:
            sys.exit()
    except OSError as error:
        print(error)


def check_opt(opt_menu):
    if opt_menu == 1:
        pass
    elif opt_menu == 2:
        Vars.WIN_MIN, Vars.WIN_MAX, Vars.TIME_TO_REPEAT, Vars.TIME_END, Vars.POWER_OFF = get_configs()
    elif opt_menu == 3:
        save_editable_vars()


def save_editable_vars():
    try:
        make_configs(set_win_min(), set_win_max(), set_time_to_repeat(),
                     set_time_end(), set_power_off())
        command(Command.CLEAR)
        show_menu()
    except OSError as error:
        print(translate(error))


def set_win_min():
    try:
        return int(input(translate(Message.SET_WIN_MIN)))
    except OSError as error:
        print(translate(error))


def set_win_max():
    try:
        return int(input(translate(Message.SET_WIN_MAX)))
    except OSError as error:
        print(translate(error))


def set_time_to_repeat():
    try:
        return float(input(translate(Message.SET_TIME_TO_REPEAT))) * 60
    except OSError as error:
        print(translate(error))


def set_time_end():
    try:
        return float(input(translate(Message.SET_TIME_END))) * 3600
    except OSError as error:
        print(translate(error))


def set_power_off():
    try:
        power_off = str(input(translate(Message.SET_POWER_OFF) + Message.CHECK_YES_NO))
        return power_off.lower() == "y"
    except OSError as error:
        print(translate(error))
