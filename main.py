from Data.dao_salle import DataSalle
from Models.salle import Salle

dao = DataSalle()

s1 = Salle("S10", "Salle Info", "Laboratoire", 30)
dao.insert_salle(s1)

s2 = Salle("S12", "Salle Reunion", "Bureau", 50)
dao.insert_salle(s2)

s3 = Salle("S11", "Grande Salle", "Classe", 60)
dao.insert_salle(s3)
