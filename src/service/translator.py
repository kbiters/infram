from textblob import TextBlob

from src.service.constants import Message, Map, Config
from src.service.mapper import mapping


def translate(msg):
    try:
        if Config.LANGUAGE is not None:
            return TextBlob(msg).translate(to=Config.LANGUAGE)
        else:
            return msg
    except OSError as error:
        print(error)


def select_language():
    try:
        return mapping(Map.LANGUAGE_MAP, int(input(Message.SELECT_LANGUAGE)))
    except OSError as error:
        print(translate(error))
