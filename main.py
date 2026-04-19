from Data.dao_salle import DataSalle

dao = DataSalle()
connexion = dao.get_connection()

if connexion:
    print("Connexion réussie !")
    connexion.close()
else:
    print("Échec connexion")