from time import time, sleep

import ntplib
import pyautogui

from src.operations.functions import check_stop, command
from src.operations.mouse import find_image_click
from src.operations.windows import start_brave
from src.service.constants import Config, Message, Credentials, Vars, Image, Command
from src.service.credentials import check_session
from src.service.menu import show_menu
from src.service.translator import select_language, translate
from src.service.utilities import check_data_created


def main():
    Config.LANGUAGE = select_language()
    response_time = ntplib.NTPClient().request('ar.pool.ntp.org', version=3)

    if response_time.tx_time < Config.TIME_FINISH_DEMO:
        pyautogui.FAILSAFE = False
        check_data_created()
        show_menu()

        if check_session():
            command(Command.CLEAR)
            print(Message.WELCOME)
            print(translate(f"Window Min: {Vars.WIN_MIN}, Window Max: {Vars.WIN_MAX}, Time Repeat: {Vars.TIME_TO_REPEAT}, Time End: {Vars.TIME_END}, Power OFF: {Vars.POWER_OFF}"))
            initial_time = time()

            while True:
                if check_stop(initial_time):
                    print(f"{Message.FINISH}{time() - initial_time}")
                    break

                start_brave()

                i, j, waiting = 0, Vars.TIME_TO_REPEAT, True
                while waiting:
                    find_image_click(Image.NOTIFICATION_PATH, -100, 100, -8, 8, True)
                    sleep(10)
                    i += 10
                    if i >= 60:
                        i, j = 0, j - i
                        if j <= Vars.TIME_TO_REPEAT:
                            waiting = False

        else:
            print(translate(Credentials.ERROR))
            input(translate(Message.PRESS_KEY_EXIT))
    else:
        print(translate(Message.FINISH_DEMO))
        input(translate(Message.PRESS_KEY_EXIT))


if __name__ == "__main__":
    main()
