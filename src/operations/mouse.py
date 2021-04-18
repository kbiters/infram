import pyautogui

from src.service.constants import Mouse, Message
from src.service.translator import translate

perc_width = 0.85431918
perc_high = 0.88932292


def move_click_mouse():
    """
    In case the constant "USE" has been modified by user command, then it performs
    the functions of moving the mouse to the desired position and clicking.
    :return:
    """
    try:
        if Mouse.USE:
            get_size_screen()
            pyautogui.click()
    except OSError as error:
        print(error)


def get_size_screen():
    """
    We identify the size of the resolution that the user has and call the function
    set_new_size(), passing as parameters the width and height.
    :return:
    """
    try:
        screen_size = pyautogui.size()
        width = screen_size[0]
        high = screen_size[1]
        set_new_size(width, high)
    except OSError as error:
        print(translate(error))


def set_new_size(width, high):
    """
    We receive the parameters and multiply them by the percentage of width and something,
    with which, we calculate the exact place where the ad will be.
    :param width:
    :param high:
    :return:
    """
    try:
        new_width = width * perc_width
        new_high = high * perc_high
        move_mouse(new_width, new_high)
    except OSError as error:
        print(translate(error))


def move_mouse(new_width, new_high):
    """
    We move the mouse to the position entered by the parameters
    :param new_width:
    :param new_high:
    :return:
    """
    try:
        pyautogui.moveTo(new_width, new_high)
    except OSError as error:
        print(translate(error))


def set_use_mouse():
    """
    With this function we take the option of whether or not to use the mouse in the bot
    in case of being "y" or "Y" we change the constant "USE" from False to True.
    :return:
    """
    try:
        opt = str(input(translate(Mouse.USE_MSG) + Message.CHECK_YES_NO))
        if opt == "y" or opt == "Y":
            Mouse.USE = True
    except OSError as error:
        print(translate(error))


"""def press_key(key):
    ***
    Function to check if the key entered by keyboard is equal to the constant "STOP_KEY"
    in case it is, we set the variable globa running as False.
    :param key:
    :return:
    ***
    global running
    if key == STOP_KEY:
        running = False"""
