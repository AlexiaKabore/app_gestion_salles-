import customtkinter as ctk
from services.service_salle import ServiceSalle

class ViewSalle(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("500x500")
        self.service_salle = ServiceSalle()

        self.cadreInfo = ctk.CTkFrame(self)
        self.cadreInfo.pack(pady=10)

        self.label_code = ctk.CTkLabel(self.cadreInfo, text="Code")
        self.label_code.grid(row=0, column=0)
        self.entry_code = ctk.CTkEntry(self.cadreInfo)
        self.entry_code.grid(row=0, column=1)

        self.label_libelle = ctk.CTkLabel(self.cadreInfo, text="Libellé")
        self.label_libelle.grid(row=1, column=0)
        self.entry_libelle = ctk.CTkEntry(self.cadreInfo)
        self.entry_libelle.grid(row=1, column=1)

        self.label_type = ctk.CTkLabel(self.cadreInfo, text="Type")
        self.label_type.grid(row=2, column=0)
        self.entry_type = ctk.CTkEntry(self.cadreInfo)
        self.entry_type.grid(row=2, column=1)

        self.label_cap = ctk.CTkLabel(self.cadreInfo, text="Capacité")
        self.label_cap.grid(row=3, column=0)
        self.entry_cap = ctk.CTkEntry(self.cadreInfo)
        self.entry_cap.grid(row=3, column=1)

        self.cadreActions = ctk.CTkFrame(self)
        self.cadreActions.pack(pady=10)

        self.btn_ajouter = ctk.CTkButton(self.cadreActions, text="Ajouter", command=self.ajouter_salle)
        self.btn_ajouter.grid(row=0, column=0, padx=5)

        self.btn_modifier = ctk.CTkButton(self.cadreActions, text="Modifier")
        self.btn_modifier.grid(row=0, column=1, padx=5)

        self.btn_supprimer = ctk.CTkButton(self.cadreActions, text="Supprimer")
        self.btn_supprimer.grid(row=0, column=2, padx=5)

        self.btn_rechercher = ctk.CTkButton(self.cadreActions, text="Rechercher")
        self.btn_rechercher.grid(row=0, column=3, padx=5)

    def ajouter_salle(self):
        code = self.entry_code.get()
        libelle = self.entry_libelle.get()
        type_s = self.entry_type.get()
        capacite = int(self.entry_cap.get())

        from Models.salle import Salle
        salle = Salle(code, libelle, type_s, capacite)

        resultat, message = self.service_salle.ajouter_salle(salle)
        print(message)
