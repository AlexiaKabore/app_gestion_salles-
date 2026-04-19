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

    def update_salle(self, salle):

            connexion = self.get_connection()
            cursor = connexion.cursor()

            sql = """
            UPDATE salle
            SET libelle=%s, type=%s, capacite=%s
            WHERE code=%s
            """

            valeurs = (salle.libelle, salle.type, salle.capacite, salle.code)

            cursor.execute(sql, valeurs)
            connexion.commit()

            print("Salle modifiée")

            cursor.close()
            connexion.close()

    def get_salle(self, code):

            connexion = self.get_connection()
            cursor = connexion.cursor()

            sql = "SELECT * FROM salle WHERE code = %s"
            cursor.execute(sql, (code,))

            result = cursor.fetchone()

            cursor.close()
            connexion.close()

            if result:
                return Salle(result[0], result[1], result[2], result[3])
            else:
                return None


    def get_salles(self):

            connexion = self.get_connection()
            cursor = connexion.cursor()

            cursor.execute("SELECT * FROM salle")
            resultats = cursor.fetchall()

            salles = []

            for row in resultats:
                s = Salle(row[0], row[1], row[2], row[3])
                salles.append(s)

            cursor.close()
            connexion.close()

            return salles




