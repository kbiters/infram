from time import sleep

import pyautogui
from pynput import keyboard as kb

stop_key = kb.Key.esc
running = True

perc_width = 0.93
perc_high = 0.93


def keep_mouse():
    get_size_screen()


def move_mouse_pos():
    get_size_screen()


def get_size_screen():
    try:
        screen_size = pyautogui.size()
        width = screen_size[0]
        high = screen_size[1]
        set_new_size(width, high)
    except OSError as error:
        print(error)


def set_new_size(width, high):
    try:
        # 0.9 Porque manejo porcentaje de pantalla, asi va a funcionar en cualquier resolucion...
        new_width = width * perc_width
        new_high = high * perc_high
        move_mouse(new_width, new_high)
    except OSError as error:
        print(error)


def move_mouse(new_width, new_high):
    try:
        # Movemos el mouse a la direccion donde aparece el anuncio
        pyautogui.moveTo(new_width, new_high)
    except OSError as error:
        print(error)


def press_key(key):
    global running
    if key == stop_key:
        running = False


def main():
    move_mouse_pos()

    lis = kb.Listener(on_press=press_key)
    lis.start()

    while running:
        keep_mouse()
        print(pyautogui.position())
        print(pyautogui.click())
        sleep(1)


if __name__ == '__main__':
    main()
