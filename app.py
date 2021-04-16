import pyautogui

from autoupdate import auto_update


def main():
    pyautogui.FAILSAFE = False
    # Config.LANGUAGE = select_language()
    # set_use_mouse()
    auto_update()
    # if check_session():


"""  print(translate(Message.WELCOME))
  initial_time = time()

  while True:
      if check_stop(initial_time):
          break

      move_click_mouse()

      start_brave()
      sleep(Brave.TIME_TO_REPEAT)

  print(f"Finish after: {time() - initial_time}")"""
# else:
# print(translate(Credentials.ERROR))


if __name__ == "__main__":
    main()
