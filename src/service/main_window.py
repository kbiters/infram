from src.operations.functions import command
from src.service.constants import Command, Message, Vars
from src.service.translator import translate


def show_main_window():
    command(Command.CLEAR)
    print(Message.WELCOME)
    print(translate(
        f"windows Min: {Vars.WIN_MIN}, "
        f"windows Max: {Vars.WIN_MAX}, "
        f"Time for Repeat: {Vars.TIME_TO_REPEAT / 60} minute, "
        f"Time for End: {Vars.TIME_END / 3600} hour, "
        f"Power OFF: {Vars.POWER_OFF}"))
