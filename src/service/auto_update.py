import subprocess
import sys

import requests

from src.service.constants import Config

url_check_version = "https://raw.githubusercontent.com/inframbot/inframbot-autodownloader/main/README.md"


def latest_version_check():
    r_version = requests.get(url_check_version, stream=True)
    if float(r_version.text) > Config.VERSION:
        subprocess.Popen("cmd /c start InframUpdater.exe")
        sys.exit(0)
