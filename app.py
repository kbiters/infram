from src.service.constants import Msg
from src.service.translator import select_language

msg = Msg()


def main():
    print(msg.WELCOME)
    language = select_language()


if __name__ == '__main__':
    main()
