from random import randint, uniform
from time import sleep

import pyautogui


def find_image_click(paths, x_min=0, x_max=0, y_min=0, y_max=0):
    validate = False

    if isinstance(paths, tuple):
        for path in paths:
            if pyautogui.locateOnScreen(path) is not None:
                coorX, coorY = pyautogui.locateCenterOnScreen(path, confidence=0.7)
                pyautogui.moveTo(coorX + randint(x_min, x_max), coorY + randint(y_min, y_max))
                sleep(uniform(0.2, 0.7))
                pyautogui.click()
                sleep(uniform(0.1, 0.3))
                pyautogui.moveTo(0, 0)
                sleep(uniform(0.4, 0.8))
                validate = True
    return validate
