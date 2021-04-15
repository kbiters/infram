from time import time, sleep

import pyautogui

from src.operations.functions import check_stop
from src.operations.windows import start_brave
from src.service.constants import Message, Config, Brave
from src.service.credentials import check_session
from src.service.translator import select_language, translate


def main():
    pyautogui.FAILSAFE = False
    Config.LANGUAGE = select_language()

    if check_session():

        print(translate(Message.WELCOME))
        initial_time = time()

        while True:
            if check_stop(initial_time):
                break

            start_brave()
            sleep(Brave.TIME_TO_REPEAT)

        print(f"Finish after: {time() - initial_time}")
    else:
        print(translate(
            'Incorrect credentials, enter: https://discord.gg/z7AmYMMB, '
            'in the "AUTHORIZATION" section you can get the code to run INFRAM.'))


if __name__ == "__main__":
    main()
