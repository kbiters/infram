import os
import pyautogui
from src.service.constants import Brave


def key(first_key, second_key):
    try:
        if len(first_key) > 0:
            pyautogui.hotkey(first_key, second_key)
        else:
            pyautogui.hotkey(second_key)
    except OSError as error:
        print(error)


def command(name_comm):
    try:
        os.system(name_comm)
    except OSError as error:
        print(error)


def start_alert():
    try:
        pyautogui.alert(Brave.STARTUP_ALERT, Brave.TITLE_ALERT_, timeout=10000)
    except OSError as error:
        print(error)
