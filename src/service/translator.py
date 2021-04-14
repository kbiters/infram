from textblob import TextBlob
from src.service.constants import Message, Map
from src.service.mapper import mapping


def print_txt(language, msg, check_input):
    try:
        msg_blob = TextBlob(msg)

        if len(language) > 0:
            translation = msg_blob.translate(from_lang='en', to=language)
            if check_input:
                return translation
            else:
                print(translation)
        else:
            if check_input:
                return msg_blob
            else:
                print(msg_blob)
    except OSError as error:
        print_txt(language, error, False)


def select_language():
    try:
        opt = int(input(Message.SELECT_LANGUAGE))
        selected_lang = mapping(Map.LANGUAGE_MAP, opt)
        return selected_lang
    except OSError as error:
        print(error)
