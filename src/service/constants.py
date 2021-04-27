class Config:
    LANGUAGE = None


class Vars:
    WIN_MIN = 0
    WIN_MAX = 0
    TIME_END = 0
    TIME_TO_REPEAT = 0
    POWER_OFF = False

    TEST = 0


class Database:
    DB_FILE = "DataBase.db"
    JSON_FILE = "credentials.json"
    JSON_TEST = "test.json"
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


class Image:
    NOTIFICATION_PATH = ("data/images/notification.png",
                         "data/images/notification2.png"
                         )

    NEW_TAB_PATH = ("data/images/more.png",)


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
    GET_TYPE_DB_USE = "Enter the configuration you want to use 1. DEFAULT | 2. EDITABLE: "


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

    TYPE_DB_MAP = {
        1: "defaultConfigs",
        2: "editableConfigs"
    }

    LANGUAGE_MAP = {1: None, 2: "es"}

    ENCRYPTOR_MAP = {0: 'l', 1: 'e', 2: 'g', 3: 'u', 4: 'm', 5: 'i', 6: 'n', 7: 'o', 8: 's', 9: 'a'}


class Command:
    EXIT = "exit"
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


class Brave:
    STARTUP_ALERT = "Infram will start in 10 sec, press OK or close this alert to start now ..."
    TITLE_ALERT = "Infram - Start Alert"
    # PATH = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
    OPEN_LINK = "cmd /c start brave https://github.com/gianca1994 --new-window"


class Page:
    PAGES_LIST = [
        "jabon", "cepillo", "tenedor", "cuchillo", "peine", "paragua", "almohada", "botiquin",
        "cama", "clip", "flor", "shampoo", "pila", "bateria", "pasta", "billete", "moneda",
        "capsula", "cafe", "te", "chicle", "botella", "cuchara", "aceite", "agua", "fuego",
        "tierra", "aire", "ozono", "rayo", "tierra", "sol", "luna", "marte", "planeta",
        "mercurio", "jupiter", "saturno", "urano", "neptuno", "pluton", "galaxia", "via lactea",
        "sistema solar", "estrella", "satelite", "lunes", "martes", "miercoles", "jueves",
        "viernes", "sabado", "domingo", "luz", "film", "tazas", "jarra", "vaso", "vela",
        "petroleo", "gas", "nafta", "gas oil", "corriente", "electricidad", "intensidad",
        "fuerza", "modulo", "ampere", "voltaje", "tension", "campo electrico", "campo magnetico",
        "magnetismo", "hidrogeno", "helio", "litio", "berilio", "boro", "carbono", "nitrogeno",
        "oxigeno", "fluor", "neon", "sodio", "magnesio", "aluminio", "silicio", "fosforo",
        "azufre", "cloro", "argon", "potasio", "calcio", "escandio", "titanio", "vanadio",
        "cromo", "manganeso", "hierro", "cobalto", "niquel", "cobre", "zinc", "galio", "germanio",
        "arsenico", "selenio", "bromo", "kripton", "rubidio", "estroncio", "itrio", "circonio",
        "niobio", "molibdeno", "tecnecio", "rutenio", "rodio", "paladio", "plata", "cadmio",
        "indio", "estaño", "antimonio", "telurico", "yodo", "xenon", "cesio", "bario", "hafnio",
        "tantalo", "wolframio", "renio", "osmio", "iridio", "platino", "oro", "mercurio", "talio",
        "plomo", "bismuto", "polonio", "astato", "radon", "francio", "radio", "rutherfordio",
        "dubnio", "seaborgio", "bohrio", "hasio", "meitnerio", "darmastatio", "roentgenio",
        "copernicio", "nihonio", "flerovio", "moscovio", "livermorio", "teneso", "oganeson",
        "latano", "cerio", "praseodimio", "neodimio", "prometio", "samarino", "europio",
        "gadolinio", "terbio", "disprosio", "holmio", "erbio", "tulio", "iterbio", "lutecio",
        "actinio", "torio", "proactinio", "uranio", "neptunio", "plutonio", "americio", "curio",
        "berkelio", "californio", "einstenio", "fermio", "mendelevio", "nobelio", "lawrencio",
        "cable", "aislante", "conductor", "zapatilla", "zapatos", "borcegos", "botas", "panchas",
        "mocasines", "sandalias", "ojotas", "zuecos", "campera", "remera", "buzo", "sweater",
        "cardigan", "jean", "chomba", "camisa", "pantalon", "jogging", "bermuda", "short", "bluza",
        "camiseta", "pelota", "canasta", "silbato", "bicicleta", "meta", "raqueta", "red", "banca",
        "paragua", "porteria", "cancha", "tablero", "estadio", "vestuario", "arbitro", "jugador",
        "uva", "lima", "limon", "cereza", "arandano", "banana", "manzana", "sandia", "melocoton",
        "piña", "fresa", "naranja", "coco", "pera", "albaricoque", "aguacate", "zarzamora", "pomelo",
        "kiwi", "mango", "ciruela", "frambuesa", "granada", "higo", "maracuya", "mandarina", "zandia",
        "mochila", "libro", "librero", "recreo", "cafeteria", "calculadora", "calendario", "tiza",
        "pizzarron", "clase", "aula", "crayon", "escritorio", "diploma", "examen", "pegamento",
        "calificacion", "gimnasio", "perforadora", "tarea", "laboratorio", "biblioteca", "mapa",
        "boligrafo", "lapiz", "lapicera", "sacapuntas", "cartel", "director", "profesor", "prueba",
        "regla", "beca", "tijeras", "semestre", "engrapadora", "contabilidad", "arqueologia",
        "arquitectura", "arte", "astronomia", "biologia", "quimica", "economia", "ingenieria",
        "geografia", "geologia", "historia", "literatura", "matematica", "lengua", "musica",
        "filosofia", "fisica", "psicologia", "sociologia", "teologia", "ingles", "chino", "español",
        "frances", "arabe", "ruso", "bengali", "portugues", "indonesio", "aleman", "japones", "turco",
        "italiano"
    ]


class Credentials:
    INFO = '\nIf you dont have the code to authorize INFRAM, you can get it here: ' \
           'https://discord.gg/JgzeAwKYNA, in the "AUTHORIZATION" section.'

    ERROR = 'Incorrect credentials, enter: https://discord.gg/JgzeAwKYNA in the ' \
            '"AUTHORIZATION" section you can get the code to run INFRAM.'

    OK = "Authorization code VALIDATED!\n"
    SET_FIRST = "Enter the code that is in the DISCORD group: "
    SET_SECOND = "Enter the second code that is in the DISCORD group: "
