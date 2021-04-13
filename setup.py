# --------------------------------------------------
# If you want, you can create a virtual enviroment,
# execute `python3 -m venv venv`
# and following execute setup.py
#
# To setup the project execute the command line:
# `python3 setup.py install`
# --------------------------------------------------

from setuptools import setup, find_packages

setup(
    name="infram",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["pyautogui", "pynput"],
)
