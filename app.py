from time import time, sleep

import pyautogui

from src.db.setting import load_setting
from src.operations.functions import check_stop
from src.operations.windows import start_brave
from src.service.constants import Config, Message, Credentials, Vars
from src.service.credentials import check_session
from src.service.translator import select_language, translate
from src.service.utilities import check_data_created


def main():
    pyautogui.FAILSAFE = False
    Config.LANGUAGE = select_language()
    check_data_created()

    if check_session():
        print(translate(Message.WELCOME))
        initial_time = time()

        load_setting()

        while True:
            if check_stop(initial_time):
                print(f"{Message.FINISH}{time() - initial_time}")
                break

            start_brave()
            sleep(Vars.TIME_TO_REPEAT)

    else:
        print(translate(Credentials.ERROR))


if __name__ == "__main__":
    main()
