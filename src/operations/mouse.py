from random import randint

import pyautogui


def find_image_click(paths, x_min=0, x_max=0, y_min=0, y_max=0):
    validate = False

    if isinstance(paths, tuple):
        for path in paths:
            if pyautogui.locateOnScreen(path) is not None:
                coorX, coorY = pyautogui.locateCenterOnScreen(path, confidence=0.7)
                pyautogui.moveTo(coorX + randint(x_min, x_max), coorY + randint(y_min, y_max))
                pyautogui.click()
                validate = True
    return validate
