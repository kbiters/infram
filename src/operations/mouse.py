import json
from random import randint, uniform
from time import sleep

import pyautogui

from src.service.constants import Config, Data, Message
from src.service.translator import translate


def find_image_click(paths, x_min=0, x_max=0, y_min=0, y_max=0, notification=False):
    validate = False
    with open(Data.DATA_PATH + Data.CLICKS, 'r+') as file:
        total_amount = json.load(file)['Clicks']['Total_amount']
    try:
        if isinstance(paths, tuple):
            for path in paths:
                if pyautogui.locateOnScreen(path) is not None:
                    coorX, coorY = pyautogui.locateCenterOnScreen(path, confidence=0.7)
                    pyautogui.moveTo(coorX + randint(x_min, x_max), coorY + randint(y_min, y_max))
                    if notification:
                        Config.CLICKS += 1
                        print(translate(Message.AD_DETECTED))
                        print(translate(Message.AD_CLICKED_IN_SESSION) + str(Config.CLICKS) +
                              ", " + translate(Message.AD_CLICKED_TOTAL) + str(total_amount))
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
            total_amount = data['Clicks']['Total_amount']
            data['Clicks'] = {
                'Partial_amount': count_clicks,
                'Total_amount': total_amount + count_clicks
            }
            file.seek(0)
            file.write(json.dumps(data, indent=4))
            file.truncate()
    except OSError as error:
        print(translate(error))


def make_clicks_default():
    try:
        with open(Data.DATA_PATH + Data.CLICKS, 'w') as f:
            data = {'Clicks': {
                'Partial_amount': "0",
                'Total_amount': "0"
            }}
            json.dump(data, f, indent=4)
    except OSError as error:
        print(translate(error))
