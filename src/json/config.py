import json

from src.service.constants import Data


def make_configs_default():
    try:
        with open(Data.DATA_PATH + Data.CONFIGS, 'w') as file:
            data = {
                "DEFAULT": {
                    "WIN_MIN": 5,
                    "WIN_MAX": 10,
                    "TIME_TO_REPEAT": 120,
                    "TIME_END": 3600,
                    "POWER_OFF": False
                },
                "EDITABLE": {
                    "WIN_MIN": 5,
                    "WIN_MAX": 10,
                    "TIME_TO_REPEAT": 120,
                    "TIME_END": 3600,
                    "POWER_OFF": False
                }
            }
            json.dump(data, file, indent=4)
    except OSError as error:
        print(error)


def get_configs(type_config):
    try:
        with open(Data.DATA_PATH + Data.CONFIGS) as file:
            data = json.load(file)
            win_min = data[type_config]['WIN_MIN']
            win_max = data[type_config]['WIN_MAX']
            time_to_repeat = data[type_config]['TIME_TO_REPEAT']
            time_end = data[type_config]['TIME_END']
            power_off = data[type_config]['POWER_OFF']
            file.close()
            return win_min, win_max, time_to_repeat, time_end, power_off
    except OSError as error:
        print(error)


def save_configs(win_min, win_max, time_to_repeat, time_end, power_off):
    try:
        with open(Data.DATA_PATH + Data.CONFIGS, 'r+') as file:
            data = json.load(file)
            data['EDITABLE'] = {
                'WIN_MIN': win_min,
                'WIN_MAX': win_max,
                'TIME_TO_REPEAT': time_to_repeat,
                'TIME_END': time_end,
                'POWER_OFF': power_off
            }
            file.seek(0)
            file.write(json.dumps(data, indent=4))
            file.truncate()
            file.close()
    except OSError as error:
        print(error)
