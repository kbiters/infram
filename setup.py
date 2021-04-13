# --------------------------------------------------
# If you want, you can create a virtual enviroment,
# execute `python3 -m venv venv`
# and following execute setup.py
#
# To setup the project execute the command line:
# `python3 setup.py install`
# --------------------------------------------------

import io
from setuptools import setup, find_packages

with io.open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="infram",
    version="0.0.1",
    description="A small bot for Brave",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    zip_safe=False,
    install_requires=["pyautogui", "pynput"],
    python_requires="~=3.6",
    author="",
    author_email="",
    url="https://github.com/kbiters/infram",
)
