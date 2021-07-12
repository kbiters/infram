import json

from src.service.constants import Data
from src.service.translator import translate


def make_credentials_default():
    try:
        with open(Data.DATA_PATH + Data.CREDENTIALS, 'w') as f:
            data = {'credentials': []}
            data["credentials"].append({
                'cred1': "None",
                'cred2': "None",
            })
            json.dump(data, f, indent=4)
    except OSError as error:
        print(translate(error))


def get_credentials():
    try:
        with open(Data.DATA_PATH + Data.CREDENTIALS) as file:
            dat = json.load(file)
            for credentials in dat["credentials"]:
                first_hash = credentials['cred1']
                second_hash = credentials['cred2']
            return list(first_hash.lower()), list(second_hash.lower())
    except OSError as error:
        print(translate(error))


def save_credentials(credential1, credential2):
    try:
        data = {'credentials': []}
        data["credentials"].append({
            'cred1': credential1,
            'cred2': credential2,
        })

        with open(Data.DATA_PATH + Data.CREDENTIALS, 'w') as f:
            json.dump(data, f, indent=4)
    except OSError as error:
        print(translate(error))
