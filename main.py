from services.service_salle import ServiceSalle
from Models.salle import Salle

service = ServiceSalle()

print("Liste des salles :")
salles = service.recuperer_salles()
for s in salles:
    s.afficher_infos()

s1 = Salle("S30", "Salle Info", "Laboratoire", 25)
resultat, message = service.ajouter_salle(s1)
print("Ajout :", message)

s1.libelle = "Salle Informatique"
s1.capacite = 35
resultat, message = service.modifier_salle(s1)
print("Modification :", message)

service.supprimer_salle("S30")
print("Salle supprimée")

salle = service.rechercher_salle("S30")
if salle:
    print("Salle trouvée :")
    salle.afficher_infos()
else:
    print("Salle non trouvée")

print("Liste après suppression :")
salles = service.recuperer_salles()
for s in salles:
    s.afficher_infos()