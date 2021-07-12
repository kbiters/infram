import os.path
from msvcrt import getch
from time import time

from src.json import config
from src.json.credentials import make_credentials_default
from src.operations.functions import check_stop, command, key
from src.operations.mouse import make_clicks_default
from src.service.constants import Data, Message, Credentials, Command, Config, Key
from src.service.credentials import check_session
from src.service.translator import translate


def check_data_created():
    if not os.path.isdir(Data.DATA_PATH):
        os.mkdir(Data.DATA_PATH)

    if not os.path.isdir(Data.DATA_PATH + "images/"):
        os.mkdir(Data.DATA_PATH + "images/")

    check_files_created()


def check_files_created():
    if not os.path.isfile(Data.DATA_PATH + Data.CONFIGS):
        config.apply_config()

    if not os.path.isfile(Data.DATA_PATH + Data.CREDENTIALS):
        make_credentials_default()

    if not os.path.isfile(Data.DATA_PATH + Data.CLICKS):
        make_clicks_default()


def check_credentials():
    if not check_session():
        print(translate(Credentials.ERROR))
        press_key_exit()


def check_finish_bot(initial_time):
    if check_stop(initial_time):

        if Config.ACTIVE_BROWSER:
            key(Key.CTRL, Key.W)

        if config.power_off:
            command(Command.POWER_OFF)

        print(f"\n{translate(Message.FINISH)} {(int(time() - initial_time)) / 60} {translate('minutes.')}\n")
        press_key_exit()


def press_key_exit():
    print(translate(Message.PRESS_KEY_EXIT))
    getch()
    exit(0)
