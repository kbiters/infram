import random

import pyautogui

from src.operations.functions import key
from src.service.constants import Page, Key
from src.service.translator import translate


def select_page():
    try:
        typer(random.choice(Page.PAGES_LIST))
    except OSError as error:
        print(translate(error))


def typer(pag):
    try:
        pyautogui.typewrite(pag, interval=0.1)
        key(second_key=Key.ENTER)
    except OSError as error:
        print(translate(error))
