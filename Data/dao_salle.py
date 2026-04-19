import mysql.connector
import json
from Models.salle import Salle

class DataSalle:

    def get_connection(self):
            with open("./data/config.json", "r", encoding="utf-8") as f:
                config = json.load(f)

            connexion = mysql.connector.connect(
                host=config["host"],
                user=config["user"],
                password=config["password"],
                database=config["database"]
            )

            return connexion

