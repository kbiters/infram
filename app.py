from time import time, sleep

import pyautogui

from src.operations.functions import check_stop
from src.operations.mouse import find_image_click
from src.operations.windows import start_brave
from src.service.constants import Config, Message, Credentials, Vars, Image
from src.service.credentials import check_session
from src.service.menu import show_menu
from src.service.translator import select_language, translate
from src.service.utilities import check_data_created


def main():
    pyautogui.FAILSAFE = False
    Config.LANGUAGE = select_language()
    check_data_created()

    if check_session():
        show_menu()
        initial_time = time()

        while True:
            if check_stop(initial_time):
                print(f"{Message.FINISH}{time() - initial_time}")
                break

            start_brave()

            i, j, waiting = 0, Vars.TIME_TO_REPEAT, True
            while waiting:
                find_image_click(Image.NOTIFICATION_PATH, -100, 100, -8, 8)
                sleep(10)
                i += 10
                if i >= 60:
                    i, j = 0, j - i
                    if j <= Vars.TIME_TO_REPEAT:
                        waiting = False

    else:
        print(translate(Credentials.ERROR))


if __name__ == "__main__":
    main()
