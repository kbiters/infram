import subprocess
from random import randint, uniform
from time import sleep

from src.operations.functions import key
from src.operations.functions import start_alert
from src.operations.mouse import find_image_click
from src.operations.page import select_page
from src.service.constants import Brave, Key, Image, Vars, Config
from src.service.translator import translate

win_to_open = randint(Vars.WIN_MIN, Vars.WIN_MAX)
win_to_close = win_to_open + 1

wait_finish_opening = uniform(3.8, 7.2)
wait_to_start = uniform(3.4, 6.3)
wait_to_type = uniform(3.1, 5.4)
wait_to_close = uniform(3.3, 4.2)


def start_brave():
    """
    Function to open the Brave browser, first start an alert that the browser will run,
    and then we call the function to start the opening of tabs.
    """
    try:
        start_alert()
        subprocess.Popen(Brave.OPEN_LINK)
        sleep(wait_finish_opening)
        open_windows()
    except OSError as error:
        print(translate(error))


def open_windows():
    """
    Function to open all tabs, executing the 'key' function and passing it as parameters
    the constants 'Key.CTRL' and 'Key.T' then wait a while and call the function 'select_page',
    once 'i' equals the constant passed by parameter, the 'close_window' function is executed.
    """
    try:
        i = 1
        while i <= win_to_open:
            sleep(wait_to_start)
            if not find_image_click(Image.NOTIFICATION_PATH, -99, 97, -8, 7, True):
                key(Key.CTRL, Key.T)
            else:
                sleep(uniform(0.7, 1.3))
                find_image_click(Image.NEW_TAB_PATH)
            sleep(wait_to_type)
            select_page()
            i += 1
        close_windows()
    except OSError as error:
        print(translate(error))


def close_windows():
    """
    Function to close all tabs + 1, this '+1' refers to also closing the tab that initially
    opened the 'start_brave' function, waiting for a random time between tab and tab closure,
    to close we use the key combination 'Key.CTRL' + 'Key.W'.
    """
    try:
        i = 1
        while i <= win_to_close:
            sleep(wait_to_close)
            key(Key.CTRL, Key.W)
            i += 1
        sleep(2)
    except OSError as error:
        print(translate(error))
