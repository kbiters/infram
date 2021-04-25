import json
import os.path

from src.db.make_tables import create_db_tables
from src.service.constants import Database


def check_data_created():
    if not os.path.isdir(Database.DATA_PATH):
        os.mkdir(Database.DATA_PATH)

    if not os.path.isdir(Database.DATA_PATH + "images/"):
        os.mkdir(Database.DATA_PATH + "images/")

    check_files_created()


def check_files_created():
    if not os.path.isfile(Database.DATA_PATH + Database.DB_FILE):
        create_db_tables()

    if not os.path.isfile(Database.DATA_PATH + Database.JSON_FILE):
        with open(Database.DATA_PATH + Database.JSON_FILE, 'w') as f:
            data = {'credentials': []}
            data["credentials"].append({
                'cred1': "None",
                'cred2': "None",
            })
            json.dump(data, f)
