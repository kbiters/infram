import os.path
from msvcrt import getch
from time import time

import ntplib

from src.json.config import make_configs
from src.json.credentials import make_credentials_default
from src.operations.functions import check_stop
from src.service.constants import Data, Config, Message, Credentials
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
        make_configs()

    if not os.path.isfile(Data.DATA_PATH + Data.CREDENTIALS):
        make_credentials_default()


def check_finish_demo():
    response_time = ntplib.NTPClient().request('ar.pool.ntp.org', version=3)
    if response_time.tx_time >= Config.TIME_FINISH_DEMO:
        print(translate(Message.FINISH_DEMO))
        press_key_exit()


def check_credentials():
    if not check_session():
        print(translate(Credentials.ERROR))
        press_key_exit()


def check_finish_bot(initial_time):
    if check_stop(initial_time):
        print(f"{translate(Message.FINISH)} {int(time() - initial_time)} {translate('seconds.')}")
        press_key_exit()


def press_key_exit():
    print(translate(Message.PRESS_KEY_EXIT))
    getch()
    exit(0)
