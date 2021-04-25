class Database:
    DB_FILE = "DataBase.db"
    JSON_FILE = "credentials.json"
    DATA_PATH = "data/"

    LIST_TABLES = {
        "defaultConfigs",
        "editableConfigs"
    }

    DICT_MAKE_TABLES = {
        "create table defaultConfigs (id integer primary key autoincrement, "
        "WIN_MIN int, WIN_MAX int, TIME_END int, TIME_TO_REPEAT int, POWER_OFF boolean)",
        "create table editableConfigs (id integer primary key autoincrement, "
        "WIN_MIN int, WIN_MAX int, TIME_END int, TIME_TO_REPEAT int, POWER_OFF boolean)"
    }

    WIN_MIN = 5
    WIN_MAX = 10
    TIME_END = 1500
    TIME_TO_REPEAT = 60
    POWER_OFF = False


class Image:
    NOTIFICATION_PATH = ("data/images/notification.png",
                         "data/images/notification2.png")

    NEW_TAB_PATH = ("data/images/more.png",)


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
    FINISH = "Finish after: "


class Map:
    MAKE_TABLES = {
        "defaultConfigs": "insert into defaultConfigs(WIN_MIN, WIN_MAX, TIME_END, "
                          "TIME_TO_REPEAT, POWER_OFF) values (?,?,?,?,?)",
        "editableConfigs": "insert into editableConfigs(WIN_MIN, WIN_MAX, TIME_END, "
                           "TIME_TO_REPEAT, POWER_OFF) values (?,?,?,?,?)"
    }

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


class Page:
    PAGES_LIST = [
        "https://www.instagram.com", "https://www.amazon.es", "https://archive.org/",
        "https://es.simplesite.com/pages/pagelist.aspx", "https://duckduckgo.com/",
        "https://www.jamendo.com/", "https://soundcloud.com/", "https://www.libro-s.com/",
        "https://dissolve.com/community", "https://www.infoempleo.com/",
        "https://soprasteria.ofertas-trabajo.infojobs.net/", "https://www.coursera.org/",
        "https://www.futurelearn.com/", "https://www.idealo.es/", "https://livestream.com/",
        "https://wiseplay.es/descargar/", "https://www.c-date.es/", "https://tinder.com/?lang=es-ES",
        "https://3somerapp.com/", "https://badoo.com/es/", "https://bumble.com/es/",
        "https://www.eharmony.com/", "https://www.gentechat.net/", "https://www.grindr.com/",
        "https://www.haterdater.com/", "https://www.jaumo.com/es/", "https://es.lovoo.com/",
        "https://www.meetic.es/", "https://es.www.meetme.com/#home", "https://www.liruch.com/"
    ]


class Credentials:
    INFO = '\nIf you dont have the code to authorize INFRAM, you can get it here: ' \
           'https://discord.gg/JgzeAwKYNA, in the "AUTHORIZATION" section.'

    ERROR = 'Incorrect credentials, enter: https://discord.gg/JgzeAwKYNA in the ' \
            '"AUTHORIZATION" section you can get the code to run INFRAM.'

    OK = "Authorization code VALIDATED!\n"
    SET_FIRST = "Enter the code that is in the DISCORD group: "
    SET_SECOND = "Enter the second code that is in the DISCORD group: "
