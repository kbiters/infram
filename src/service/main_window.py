from src.json import config
from src.operations.functions import command
from src.service.constants import Command, Message
from src.service.translator import translate


def show_main_window():
    command(Command.CLEAR)
    print(Message.WELCOME)
    print(translate(
        f"windows Min: {config.win_min}, "
        f"windows Max: {config.win_max}, "
        f"Time for Repeat: {config.time_to_repeat / 60} minute, "
        f"Time for End: {config.time_end / 3600} hour, "
        f"Power OFF: {config.power_off}"))
