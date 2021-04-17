import os
from time import time

import pyautogui

from src.service.constants import Brave
from src.service.translator import translate


def key(first_key=None, second_key=None):
    """
    We execute the 'hotkey' function from the 'pyautogui' library, to begin with, both parameters
    are initialized as 'None' which will help us to know if a combination of keys or it is only 1
    key that comes as a parameter, in case both parameters are not 'None', the first conditional
    is met and we can execute the combination. For example: 'pyautogui.hotkey ("Alt", "F4")',
    otherwise it means that it is a 1 key press. For example: 'pyautogui.hotkey ("Enter")'.
    """
    try:
        if first_key:
            pyautogui.hotkey(first_key, second_key)
        else:
            pyautogui.hotkey(second_key)
    except OSError as error:
        print(translate(error))


def command(name_comm):
    """
    Simple function, we only give as a parameter the name of the command we want to execute,
    We invoke the method 'system' of the module 'os' and as a parameter the name of the command
    a run. For example: 'os.system ("exit")'.
    """
    try:
        os.system(name_comm)
    except OSError as error:
        print(translate(error))


def start_alert():
    """
    We execute the 'alert' function from the 'pyautogui' library, as the first parameter
    We indicate the message that the alert message will contain, as a second parameter
    We indicate the title that the poster will carry and as a third parameter, the maximum
    time, means that if the poster is shown for '10000ms' or '10s', it closes and the program
    keep going.
    """
    try:
        pyautogui.alert(translate(Brave.STARTUP_ALERT),
                        translate(Brave.TITLE_ALERT),
                        timeout=10000)
    except OSError as error:
        print(translate(error))


def check_stop(initial_time):
    """
    Function to check if the time with which the bot started equaled or exceeded
    the time that it had been predetermined to work in case the 'final - initial'
    time is equal to or greater than the set time to stop, 'True' returns.
    """
    try:
        if time() - initial_time >= Brave.TIME_END:
            return True
    except OSError as error:
        print(error)