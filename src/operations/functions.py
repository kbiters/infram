import os
from time import time

import pyautogui

from src.json import config
from src.service.constants import Brave
from src.service.translator import translate


def key(first_key=None, second_key=None):
    try:
        if first_key:
            pyautogui.hotkey(first_key, second_key)
        else:
            pyautogui.hotkey(second_key)
    except OSError as error:
        print(translate(error))


def command(name_comm):
    try:
        os.system(name_comm)
    except OSError as error:
        print(translate(error))


def start_alert():
    try:
        pyautogui.alert(translate(Brave.STARTUP_ALERT),
                        translate(Brave.TITLE_ALERT),
                        timeout=10000)
    except OSError as error:
        print(translate(error))


def check_stop(initial_time):
    try:
        return time() - initial_time >= config.get_time_end()
    except OSError as error:
        print(translate(error))
