from time import sleep

import pyautogui


def find_image_click(paths):
    sleep(0.5)
    for path in paths:
        if pyautogui.locateOnScreen(path) is not None:
            coorX, coorY = pyautogui.locateCenterOnScreen(path, confidence=0.9)
            pyautogui.moveTo(coorX, coorY)
            pyautogui.click()
            return True
        return False
