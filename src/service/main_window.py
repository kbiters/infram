from src.json import config
from src.operations.functions import command
from src.service.constants import Command, Message
from src.service.translator import translate


def show_main_window():
    command(Command.CLEAR)
    print(Message.WELCOME)
    print(translate(
        f"window Min: {config.win_min}\n"
        f"window Max: {config.win_max}\n"
        f"Time for Repeat: {'{0:.2f}'.format(config.time_to_repeat / 60)} minute\n"
        f"Time for End: {'{0:.2f}'.format(config.time_end / 3600)} hour\n"
        f"Power OFF: {config.power_off}\n"))
