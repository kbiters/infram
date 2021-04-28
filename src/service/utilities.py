import os.path

from src.json.config import make_configs_default
from src.json.credentials import make_credentials_default
from src.service.constants import Data


def check_data_created():
    if not os.path.isdir(Data.DATA_PATH):
        os.mkdir(Data.DATA_PATH)

    if not os.path.isdir(Data.DATA_PATH + "images/"):
        os.mkdir(Data.DATA_PATH + "images/")

    check_files_created()


def check_files_created():
    if not os.path.isfile(Data.DATA_PATH + Data.CONFIGS):
        make_configs_default()

    if not os.path.isfile(Data.DATA_PATH + Data.CREDENTIALS):
        make_credentials_default()
