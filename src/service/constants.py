class Config:
    VERSION = 0.02
    LANGUAGE = None
    CLICKS = 0
    ACTIVE_BROWSER = False
    TIME_NOW = None
    URL_GETS = 'https://infram-api.herokuapp.com/'


class Data:
    CONFIGS = "config.json"
    CREDENTIALS = "credentials.json"
    CLICKS = "mouse.json"
    DATA_PATH = "data/"


class Image:
    NOTIFICATION_PATH = ("data/images/notification.png",)

    PLAY_LIST = "data/images/check.png"

    NEW_TAB_PATH = ("data/images/more_black.png", "data/images/more_white.png")


class Message:
    WELCOME = """+++++++++++++++++++++++++++++++++++++++++++++++++
----------- ¡Welcome to Infram Bot! -------------
------------- ¡Created by Kbiters! --------------
+++++++++++++++++++++++++++++++++++++++++++++++++
"""

    MENU = """1. USE default settings
2. USE modifiable settings
3. EDIT modifiable settings
4. Exit
"""

    SYNTAX_ERROR = "Number not allowed, enter an option again ..."
    SELECT_LANGUAGE = "Select language [1- ingles | 2- español]: "
    CHECK_YES_NO = " [y/n]: "
    FINISH = "Finish after: "
    GET_TYPE_DB_USE = "Enter the configuration you want to use 1. DEFAULT | 2. EDITABLE: "
    GET_OPTION_MENU = "Enter the option you wish to perform: "
    PRESS_KEY_EXIT = "Press key to exit..."

    SET_WIN_MIN = "Enter the MINIMUM number of tabs: "
    SET_WIN_MAX = "Enter the MAXIMUM number of tabs: "
    SET_TIME_TO_REPEAT = "Enter the TIME(min.) the process is REPEATED: "
    SET_TIME_END = "Enter the TIME(hours.) at which the process ENDS: "
    SET_POWER_OFF = "Enter whether or not to turn off the equipment after the " \
                    "processing time has elapsed "

    AD_DETECTED = "Ad detected and clicked!..."
    AD_CLICKED_IN_SESSION = "Ads clicked in this session: "
    AD_CLICKED_TOTAL = "Total number of clicked ads: "


class Map:
    MENU_MAP = {
        1: "USE default settings",
        2: "USE modifiable settings",
        3: "EDIT modifiable settings",
        4: "Exit"
    }

    LANGUAGE_MAP = {1: None, 2: "es"}
    ENCRYPTOR_MAP = {0: 'l', 1: 'e', 2: 'g', 3: 'u',
                     4: 'm', 5: 'i', 6: 'n', 7: 'o',
                     8: 's', 9: 'a'}


class Command:
    EXIT = "exit"
    CLEAR = "cls"
    POWER_OFF = "shutdown.exe -s"


class Key:
    CTRL = "Ctrl"
    W = "w"
    T = "t"
    K = "k"
    ENTER = "Enter"


class Mouse:
    USE_MSG = "You want to enable the mouse functionality (increases earnings, " \
              "but may cause discomfort if you want to use the mouse while the bot is running)"

    USE = False


class Brave:
    STARTUP_ALERT = "Infram will start in 10 sec, press OK or close this alert to start now ..."
    TITLE_ALERT = "Infram - Start Alert"

    OPEN_BROWSER = "cmd /c start brave --new-window "


class Credentials:
    INFO = '\nIf you dont have the code to authorize INFRAM, you can get it here: ' \
           'https://discord.gg/JgzeAwKYNA, in the "AUTHORIZATION" section.'

    ERROR = 'Incorrect credentials, enter: https://discord.gg/JgzeAwKYNA in the ' \
            '"AUTHORIZATION" section you can get the code to run INFRAM.'

    OK = "Authorization code VALIDATED!\n"
    SET_FIRST = "Enter the code that is in the DISCORD group: "
    SET_SECOND = "Enter the second code that is in the DISCORD group: "
