from datetime import datetime

from src.json.config import get_configs

fecha = "2021-04-28 14:36:21.812414"

if str(datetime.now()) >= fecha:
    print("excedito el tiempo!")
else:
    get_configs("EDITABLE")
"""    print("todavia no excede!!")
    save_setting(1000, 1000, 1000, 1000, False)"""
