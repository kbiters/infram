from src.operations.win_operations.first_window import open_first_window
from src.service.constants import Msg
from src.service.translator import select_language

msg = Msg()


def main():
    print(msg.WELCOME)
    language = select_language()
    open_first_window()


if __name__ == '__main__':
    main()
