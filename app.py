from time import time, sleep

import pyautogui

from src.json import config
from src.operations.mouse import find_image_click
from src.operations.windows import start_brave
from src.service.constants import Config, Image
from src.service.main_window import show_main_window
from src.service.menu import show_menu
from src.service.translator import select_language
from src.service.utilities import check_data_created, check_finish_demo, check_credentials, check_finish_bot


def main():
    Config.LANGUAGE = select_language()
    pyautogui.FAILSAFE = False

    check_finish_demo()
    check_data_created()
    check_credentials()

    show_menu()
    show_main_window()
    time_to_repeat = config.get_time_to_repeat()

    initial_time = time()

    while True:
        check_finish_demo()
        check_finish_bot(initial_time)

        start_brave()

        i, j, waiting = 0, time_to_repeat, True
        while waiting:
            find_image_click(Image.NOTIFICATION_PATH, -100, 100, -8, 8, True)
            sleep(10)
            i += 10
            if i >= 30:
                j, i = j - i, 0
                if j <= 0:
                    waiting = False


if __name__ == "__main__":
    main()
