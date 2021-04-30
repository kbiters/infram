import json
from random import randint, uniform
from time import sleep

import pyautogui

from src.service.constants import Config, Data
from src.service.translator import translate


def find_image_click(paths, x_min=0, x_max=0, y_min=0, y_max=0, notification=False):
    validate = False
    try:
        if isinstance(paths, tuple):
            for path in paths:
                if pyautogui.locateOnScreen(path) is not None:
                    coorX, coorY = pyautogui.locateCenterOnScreen(path, confidence=0.7)
                    pyautogui.moveTo(coorX + randint(x_min, x_max), coorY + randint(y_min, y_max))
                    if notification:
                        Config.CLICKS += 1
                        print(translate("Ad detected and clicked, ads clicked: ") + Config.CLICKS)
                        save_clicks(Config.CLICKS)
                    sleep(uniform(0.2, 0.7))
                    pyautogui.click()
                    sleep(uniform(0.1, 0.3))
                    pyautogui.moveTo(0, 0)
                    sleep(uniform(0.4, 0.8))
                    validate = True
        return validate
    except OSError as error:
        print(translate(error))


def save_clicks(count_clicks):
    try:
        with open(Data.DATA_PATH + Data.CLICKS, 'r+') as file:
            data = json.load(file)
            data['CLICKS'] = {
                'Cantidad': count_clicks
            }
            file.seek(0)
            file.write(json.dumps(data, indent=4))
            file.truncate()
            file.close()
    except OSError as error:
        print(translate(error))
