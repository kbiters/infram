from time import sleep
from src.service.constants import Brave, Key
from src.operations.key_writer import key
from random import randint, randrange

win_to_open = randint(Brave.WIN_MIN, Brave.WIN_MAX)
win_to_close = win_to_open + 1

wait_to_start = randint(2, 4)
wait_to_type = randint(1, 3)


def open_windows():
    try:
        i = 1
        while i <= win_to_open:
            sleep(wait_to_start)
            key(Key.CTRL, Key.T)
            # sleep(wait_to_type)
            # pagine.select_pagine()
            i += 1
        close_windows()
    except OSError as error:
        print(error)


def close_windows():
    try:
        i = 1
        while i <= win_to_close:
            sleep(wait_to_start)
            key(Key.CTRL, Key.W)
            i += 1
    except OSError as error:
        print(error)
