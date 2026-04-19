from Data.dao_salle import DataSalle

dao = DataSalle()

salles = dao.get_salles()

for s in salles:
    s.afficher_infos()