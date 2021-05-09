import subprocess
import sys
from time import sleep

import requests

from src.service.constants import Config, Message
from src.service.translator import translate

url_check_version = "https://raw.githubusercontent.com/inframbot/inframbot-autodownloader/main/README.md"


def latest_version_check():
    r_version = requests.get(url_check_version, stream=True)
    if float(r_version.text) > Config.VERSION:
        print(translate(Message.NEW_VERSION_DETECTED))
        sleep(3)
        subprocess.Popen("cmd /c start InframUpdater.exe")
        sys.exit(0)
