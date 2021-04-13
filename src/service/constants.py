class Msg:
    WELCOME = '''
+++++++++++++++++++++++++++++++++++++++++++++++++
----------- ¡Welcome to Infram Bot! -------------
------------- ¡Created by Kbiters! --------------
+++++++++++++++++++++++++++++++++++++++++++++++++
'''

    SYNTAX_ERROR = 'Number not allowed, enter an option again ...'
    SELECT_LANGUAGE = 'Select language [1- ingles | 2- español]: '
    CHECK_YES_NO = " [y/n]: "


class Map:
    MENU_MAP = {
        1: 'USE modifiable settings',
        2: 'USE default settings',
        3: 'EDIT modifiable settings',
        4: 'Exit'
    }

    LANGUAGE_MAP = {
        1: '',
        2: 'es'
    }


class Command:
    EXIT = 'Exit'
    CLEAR = 'cls'
    POWER_OFF = 'shutdown.exe -s'


class Key:
    CTRL = 'Ctrl'
    W = 'w'
    T = 't'
    ENTER = 'Enter'


class Brave:
    STARTUP_ALERT = 'Infram will start in 15 sec, press OK or close this alert to start now ...'
    TITLE_ALERT_ = 'Infram - Start Alert'
    PATH = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
    WIN_MIN = 5
    WIN_MAX = 10
