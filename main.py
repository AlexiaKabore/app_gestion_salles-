from Data.dao_salle import DataSalle
from Models.salle import Salle

dao = DataSalle()

s1= Salle("S1", "Salle Info", "Laboratoire", 30)
dao.insert_salle(s1)

s1.libelle = "Salle Modifiée"
s1.capacite = 50

dao.update_salle(s1)