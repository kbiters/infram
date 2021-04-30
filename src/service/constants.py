class Config:
    LANGUAGE = None
    CLICKS = 0
    TIME_FINISH_DEMO = 1620615599

class Vars:
    # DEFAULT
    WIN_MIN = 7
    WIN_MAX = 16
    TIME_TO_REPEAT = 180
    TIME_END = 28800
    POWER_OFF = False


class Data:
    CONFIGS = "config.json"
    CREDENTIALS = "credentials.json"
    CLICKS = "clicked_notifications.json"
    DATA_PATH = "data/"


class Image:
    NOTIFICATION_PATH = ("data/images/notification.png",)

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
    FINISH_DEMO = "InfraBot testing time is over, stay informed in our discord group: https://discord.gg/PSs4c4pW"
    PRESS_KEY_EXIT = "Press key to exit..."

    SET_WIN_MIN = "Enter the MINIMUM number of tabs: "
    SET_WIN_MAX = "Enter the MAXIMUM number of tabs: "
    SET_TIME_TO_REPEAT = "Enter the TIME(min.) the process is REPEATED: "
    SET_TIME_END = "Enter the TIME(hours.) at which the process ENDS: "
    SET_POWER_OFF = "Enter whether or not to turn off the equipment after the processing time has elapsed "


class Map:
    MENU_MAP = {
        1: "USE default settings",
        2: "USE modifiable settings",
        3: "EDIT modifiable settings",
        4: "Exit"
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

    OPEN_LINKS = [
        "cmd /c start brave https://www.youtube.com/watch?v=PnJa6DQ6DKk --new-window",
        "cmd /c start brave https://www.youtube.com/watch?v=dbfb5DXvQqA --new-window"
    ]


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
