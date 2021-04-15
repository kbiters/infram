from time import time, sleep

import pyautogui

from src.operations.functions import check_stop
from src.operations.mouse import move_click_mouse, set_use_mouse
from src.operations.windows import start_brave
from src.service.constants import Message, Config, Brave, Credentials
from src.service.credentials import check_session
from src.service.translator import select_language, translate


def main():
    pyautogui.FAILSAFE = False
    Config.LANGUAGE = select_language()
    set_use_mouse()

    if check_session():
        print(translate(Message.WELCOME))
        initial_time = time()

        while True:
            if check_stop(initial_time):
                break

            move_click_mouse()

            start_brave()
            sleep(Brave.TIME_TO_REPEAT)

        print(f"Finish after: {time() - initial_time}")
    else:
        print(translate(Credentials.ERROR))


if __name__ == "__main__":
    main()
