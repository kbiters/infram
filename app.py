from time import time, sleep

import pyautogui

from src.operations.functions import check_stop
from src.operations.windows import start_brave
from src.service.constants import Message, Config, Brave
from src.service.translator import select_language, translate


def main():
    pyautogui.FAILSAFE = False
    Config.LANGUAGE = select_language()
    print(translate(Message.WELCOME))
    initial_time = time()

    while True:
        start_brave()
        if check_stop(initial_time):
            break

        sleep(Brave.TIME_TO_REPEAT)


if __name__ == "__main__":
    main()
