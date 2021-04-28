import json

from src.service.constants import Data


def make_configs_default():
    with open(Data.DATA_PATH + Data.CONFIGS, 'w') as f:
        data = {
            "DEFAULT": [{
                "WIN_MIN": 5,
                "WIN_MAX": 10,
                "TIME_END": 3600,
                "TIME_TO_REPEAT": 120,
                "POWER_OFF": 0
            }],
            "EDITABLE": [{
                "WIN_MIN": 5,
                "WIN_MAX": 10,
                "TIME_END": 3600,
                "TIME_TO_REPEAT": 120,
                "POWER_OFF": 0
            }]
        }

        json.dump(data, f, indent=4)


def get_configs(type_config):
    try:
        with open(Data.DATA_PATH + Data.CONFIGS) as file:
            dat = json.load(file)
            for config in dat[type_config]:
                Data.WIN_MIN = config['WIN_MIN']
                Data.WIN_MAX = config['WIN_MAX']
                Data.TIME_END = config['TIME_END']
                Data.TIME_TO_REPEAT = config['TIME_TO_REPEAT']
                Data.POWER_OFF = config['POWER_OFF']
    except OSError as error:
        print(error)


def save_configs(win_min, win_max, time_end, time_to_repeat, power_off):
    try:
        with open(Data.DATA_PATH + Data.CONFIGS, 'w') as f:
            data = {
                "DEFAULT": [{
                    "WIN_MIN": 5,
                    "WIN_MAX": 10,
                    "TIME_END": 3600,
                    "TIME_TO_REPEAT": 120,
                    "POWER_OFF": 0
                }],
                "EDITABLE": [{
                    "WIN_MIN": win_min,
                    "WIN_MAX": win_max,
                    "TIME_END": time_end,
                    "TIME_TO_REPEAT": time_to_repeat,
                    "POWER_OFF": power_off
                }]
            }
            json.dump(data, f, indent=4)
    except OSError as error:
        print(error)
