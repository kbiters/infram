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


class Command:
    EXIT = "Exit"
    CLEAR = "cls"
    POWER_OFF = "shutdown.exe -s"


class Key:
    CTRL = "Ctrl"
    W = "w"
    T = "t"
    ENTER = "Enter"


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
