import subprocess
from datetime import datetime, timedelta
from random import randint, uniform, randrange, choice
from time import sleep

import pyautogui

from src.json import config
from src.operations.functions import key
from src.operations.functions import start_alert
from src.operations.mouse import find_image_click
from src.operations.page import select_page
from src.service.constants import Brave, Key, Image, Config
from src.service.translator import translate

wait_finish_opening = uniform(3.8, 7.2)
wait_to_start = uniform(3.4, 6.3)
wait_to_type = uniform(3.1, 5.4)
wait_to_close = uniform(3.3, 4.2)


def get_open_wins():
    return randint(config.win_min, config.win_max)


def start_brave():
    try:
        start_alert()
        if not Config.ACTIVE_BROWSER:
            subprocess.Popen(Brave.OPEN_BROWSER + choice(Brave.OPEN_LIST_VIDEO))
            Config.ACTIVE_BROWSER = True
            Config.TIME_NOW = datetime.now() + timedelta(minutes=30)
        sleep(wait_finish_opening)
        if pyautogui.locateOnScreen(Image.PLAY_LIST) is not None:
            key(second_key=Key.K)
        sleep(1)
        open_windows()
    except OSError as error:
        print(translate(error))


def open_windows():
    try:
        i = 1
        openWindows = get_open_wins()
        while i <= openWindows:
            sleep(wait_to_start)
            if not find_image_click(Image.NOTIFICATION_PATH, -99, 97, -8, 7, True):
                key(Key.CTRL, Key.T)
            else:
                sleep(uniform(0.7, 1.3))
                find_image_click(Image.NEW_TAB_PATH)
            sleep(wait_to_type)
            select_page()
            scroll_web()
            i += 1
        close_windows(openWindows)
    except OSError as error:
        print(translate(error))


def close_windows(openWindows):
    try:
        i = 1
        if datetime.now() >= Config.TIME_NOW:
            closeWindows = openWindows + 1
            Config.ACTIVE_BROWSER = False
        else:
            closeWindows = openWindows

        while i <= closeWindows:
            sleep(wait_to_close)
            key(Key.CTRL, Key.W)
            i += 1
        sleep(2)
    except OSError as error:
        print(translate(error))


def scroll_web():
    try:
        sleep(2)
        pyautogui.moveTo(randint(150, 750), randint(150, 500), uniform(0.1, 0.3), pyautogui.easeInOutQuad)
        for i in range(2, 5):
            sleep(0.01)
            pyautogui.scroll(randrange(-1200, -500))

        sleep(0.75)
        if randint(1, 100) >= 60:
            pyautogui.scroll(randrange(500, 1000))
    except OSError as error:
        print(translate(error))
