import random

import pyautogui

from src.operations.functions import key
from src.service.constants import Page, Key


def select_page():
    """
    We call the 'typer' function and pass it as a parameter a page that we randomly
    select, a page from the 'PAGES_LIST' list located in the 'Page' class of constants.
    """
    typer(random.choice(Page.PAGES_LIST))


def typer(pag):
    """
    We execute the 'typewrite' function from the 'pyautogui' library, as the first
    parameter the selected page and as the second the interval in 'seconds' between
    each keystroke.
    """
    pyautogui.typewrite(pag, interval=0.1)
    key(second_key=Key.ENTER)
