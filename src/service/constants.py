class Config:
    LANGUAGE = None


class Message:
    WELCOME = """
+++++++++++++++++++++++++++++++++++++++++++++++++
----------- ¡Welcome to Infram Bot! -------------
------------- ¡Created by Kbiters! --------------
+++++++++++++++++++++++++++++++++++++++++++++++++
"""

    SYNTAX_ERROR = "Number not allowed, enter an option again ..."
    SELECT_LANGUAGE = "Select language [1- ingles | 2- español]: "
    CHECK_YES_NO = " [y/n]: "


class Map:
    MENU_MAP = {
        1: "USE modifiable settings",
        2: "USE default settings",
        3: "EDIT modifiable settings",
        4: "Exit",
    }

    LANGUAGE_MAP = {1: None, 2: "es"}

    ENCRYPTOR_MAP = {0: 'l', 1: 'e', 2: 'g', 3: 'u', 4: 'm', 5: 'i', 6: 'n', 7: 'o', 8: 's', 9: 'a'}


class Command:
    EXIT = "Exit"
    CLEAR = "cls"
    POWER_OFF = "shutdown.exe -s"


class Key:
    CTRL = "Ctrl"
    W = "w"
    T = "t"
    ENTER = "Enter"


class Mouse:
    USE_MSG = "You want to enable the mouse functionality (increases earnings, " \
              "but may cause discomfort if you want to use the mouse while the bot is running)"

    USE = False
    CLICK_NONE = "¡Click done correctly!"


class Brave:
    STARTUP_ALERT = "Infram will start in 10 sec, press OK or close this alert to start now ..."
    TITLE_ALERT = "Infram - Start Alert"
    PATH = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
    WIN_MIN = 5
    WIN_MAX = 10
    TIME_END = 600
    TIME_TO_REPEAT = 60


class Page:
    PAGES_LIST = [
        'www.facebook.com', 'www.youtube.com', 'www.twitter.com', 'www.instagram.com',
        'www.coinmarketcap.com', 'www.google.com', 'amazon.es', 'wikipedia.org', 'cars',
        'autos', 'motos', 'aviones', 'guitarras', 'bajos', 'baterias', 'trompetas', 'sol',
        'Calcetines', 'Zapatos', 'Camiseta', 'Remera', 'Camisa', 'vestido', 'Sombrero',
        'chamarra', 'Pantalones cortos', 'Chanclas', 'Uniforme', 'traje', 'abrigo', 'sueter',
        'mallas', 'zapatos', 'corbatas', 'chal', 'guantes', 'gorra', 'bufanda', 'boina', 'buzo',
        'cordones', 'pantuflas'
    ]


class Credentials:
    INFO = '\nIf you dont have the code to authorize INFRAM, you can get it here: ' \
           'https://discord.gg/z7AmYMMB, in the "AUTHORIZATION" section.'

    ERROR = 'Incorrect credentials, enter: https://discord.gg/z7AmYMMB in the ' \
            '"AUTHORIZATION" section you can get the code to run INFRAM.'

    OK = "Authorization code VALIDATED!\n"
    SET_FIRST = "Enter the code that is in the DISCORD group: "
    SET_SECOND = "Enter the second code that is in the DISCORD group: "
