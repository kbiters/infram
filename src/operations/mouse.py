from random import randint

import pyautogui

variation_x = randint(-150, 150)
variation_y = randint(-10, 10)


def find_image_click(paths):
    validate = False

    if isinstance(paths, tuple):
        for path in paths:
            if pyautogui.locateOnScreen(path) is not None:
                coorX, coorY = pyautogui.locateCenterOnScreen(path, confidence=0.7)
                pyautogui.moveTo(coorX + variation_x, coorY + variation_y)
                pyautogui.click()
                validate = True
    print(validate)



