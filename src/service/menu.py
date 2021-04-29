import os

from src.json.config import get_configs
from src.service.constants import Message, Map, Command
from src.service.mapper import mapping
from src.service.translator import translate


def show_menu():
    try:
        print(translate(Message.WELCOME))
        print(translate(Message.MENU))
        check_opt(int(input(translate(Message.GET_OPTION_MENU))))
    except OSError as error:
        print(error)


def check_opt(opt_menu):
    if 1 <= opt_menu <= 2:
        select_use_vars(opt_menu)
    elif opt_menu == 3:
        print("EDIT OPTIONS...")
    else:
        os.system(Command.EXIT)


def select_use_vars(opt_menu):
    try:
        get_configs(mapping(Map.VARS_MAP, opt_menu))
    except OSError as error:
        print(error)
