import pyautogui
from time import sleep


def main():
    while True:
        position = pyautogui.position()
        x = position[0]
        y = position[1]

        print(f'POSICION X: {x} | POSICION Y: {y} ')
        sleep(0.05)


if __name__ == '__main__':
    main()
