import json

from src.service.constants import Data


def make_configs(win_min=5, win_max=10, time_to_repeat=180,
                 time_end=7200, power_off=False):
    try:
        with open(Data.DATA_PATH + Data.CONFIGS, 'w') as file:
            data = {
                "EDITABLE": {
                    "WIN_MIN": win_min,
                    "WIN_MAX": win_max,
                    "TIME_TO_REPEAT": time_to_repeat,
                    "TIME_END": time_end,
                    "POWER_OFF": power_off
                }
            }
            json.dump(data, file, indent=4)
    except OSError as error:
        print(error)


def get_configs():
    try:
        with open(Data.DATA_PATH + Data.CONFIGS) as file:
            data = json.load(file)
            win_min = data['EDITABLE']['WIN_MIN']
            win_max = data['EDITABLE']['WIN_MAX']
            time_to_repeat = data['EDITABLE']['TIME_TO_REPEAT']
            time_end = data['EDITABLE']['TIME_END']
            power_off = data['EDITABLE']['POWER_OFF']
            file.close()
            return win_min, win_max, time_to_repeat, time_end, power_off
    except OSError as error:
        print(error)
