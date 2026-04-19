from Data.dao_salle import DataSalle

dao = DataSalle()

salle = dao.get_salle("S2")

if salle:
    salle.afficher_infos()
else:
    print("Salle non trouvée")