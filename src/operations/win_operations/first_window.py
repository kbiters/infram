import subprocess

from src.operations.key_writer import start_alert
from src.service.constants import Brave
from src.operations.win_operations.secondary_win import open_windows

def open_first_window():
    try:
        start_alert()
        subprocess.Popen([Brave.PATH, '-new-tab'])
        open_windows()
    except OSError as error:
        print(error)
