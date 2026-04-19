from Data.dao_salle import DataSalle
from Models.salle import Salle

dao = DataSalle()

s1 = Salle("S1", "Salle Info", "Laboratoire", 30)

dao.insert_salle(s1)