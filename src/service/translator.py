from textblob import TextBlob

from src.service.constants import Message, Map, Config
from src.service.mapper import mapping


def translate(msg):
    """
    This function is used to receive a message as a parameter and if the constant
    'Config.LANGUAGE' is not none, then the message is translated into the language
    that contains said constant, but the message is returned with the language that came.
    """
    try:
        if Config.LANGUAGE is not None:
            return TextBlob(msg).translate(to=Config.LANGUAGE)
        else:
            return msg
    except OSError as error:
        print(error)


def select_language():
    """
    Function to select the language to be used in the whole program, we return
    the result taking as input the language that the user chose.
    """
    try:
        return mapping(Map.LANGUAGE_MAP, int(input(Message.SELECT_LANGUAGE)))
    except OSError as error:
        print(translate(error))
