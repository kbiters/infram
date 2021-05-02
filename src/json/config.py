import json

from src.service.constants import Data


class Configs:
    def __init__(self):
        self.win_min = 7
        self.win_max = 13
        self.time_to_repeat = 300
        self.time_end = 28800
        self.power_off = False

    def get_win_min(self):
        return self.win_min

    def set_win_min(self, value):
        self.win_min = value

    def get_win_max(self):
        return self.win_max

    def set_win_max(self, value):
        self.win_max = value

    def get_time_to_repeat(self):
        return self.time_to_repeat

    def set_time_to_repeat(self, value):
        self.time_to_repeat = value

    def get_time_end(self):
        return self.time_end

    def set_time_end(self, value):
        self.time_end = value

    def get_power_off(self):
        return self.power_off

    def set_power_off(self, value):
        self.power_off = value

    def apply_config(self):
        try:
            with open(Data.DATA_PATH + Data.CONFIGS, 'w') as file:
                data = {
                    "WIN_MIN": self.win_min,
                    "WIN_MAX": self.win_max,
                    "TIME_TO_REPEAT": self.time_to_repeat,
                    "TIME_END": self.time_end,
                    "POWER_OFF": self.power_off
                }
                json.dump(data, file, indent=4)
        except OSError as error:
            print(error)

    def __str__(self):
        return "%s, %s, %s, %s, %s" % (self.win_min, self.win_max, self.time_to_repeat,
                                       self.time_end, self.power_off)
