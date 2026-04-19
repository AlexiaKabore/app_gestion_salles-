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

    def insert_salle(self, salle):
            connexion = self.get_connection()
            cursor = connexion.cursor()

            cursor.execute ( "INSERT INTO salle VALUES (%s, %s, %s, %s)",
                          (salle.code, salle.libelle, salle.type, salle.capacite)
            )
            connexion.commit()
            print("Salle ajoutée")
            connexion.close()


    def delete_salle(self, code):
            connexion = self.get_connection()
            cursor = connexion.cursor()

            sql = "DELETE FROM salle WHERE code = %s"
            cursor.execute(sql, (code,))

            connexion.commit()
            print("Salle supprimée")

            cursor.close()
            connexion.close()



