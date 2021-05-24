import pyautogui
import requests

from src.operations.functions import key
from src.service.constants import Key, Config
from src.service.translator import translate


def typer(pag):
    try:
        pyautogui.typewrite(pag, interval=0.1)
        key(second_key=Key.ENTER)
    except OSError as error:
        print(translate(error))


class Pages:
    def __init__(self):
        self.page_list = []
        self.video_list = []

    def set_page_list(self, value):
        self.page_list = requests.get(Config.URL_GETS + 'page-list/' + value).json()['pages']

    def get_page_list(self):
        return self.page_list

    def set_video_list(self):
        self.video_list = requests.get(Config.URL_GETS + 'video-list/').json()['video_list']

    def get_video_list(self):
        return self.video_list

    def select_page(self):
        try:
            typer(self.get_page_list().pop())
        except OSError as error:
            print(translate(error))
