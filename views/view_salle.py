import customtkinter as ctk
from services.service_salle import ServiceSalle
from tkinter import ttk
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

        # Cadre Liste des salles
        self.cadreList = ctk.CTkFrame(self, corner_radius=10, width=400)
        self.cadreList.pack(pady=10, padx=10)

        self.treeList = ttk.Treeview(
            self.cadreList,
            columns=("code", "libelle", "type", "capacite"),
            show="headings"
        )

        # En-têtes
        self.treeList.heading("code", text="CODE")
        self.treeList.heading("libelle", text="LIBELLÉ")
        self.treeList.heading("type", text="TYPE")
        self.treeList.heading("capacite", text="CAPACITÉ")

        # Largeur des colonnes
        self.treeList.column("code", width=50)
        self.treeList.column("libelle", width=150)
        self.treeList.column("type", width=100)
        self.treeList.column("capacite", width=100)

        self.treeList.pack(expand=True, fill="both", padx=10, pady=10)
    def ajouter_salle(self):
        code = self.entry_code.get()
        libelle = self.entry_libelle.get()
        type_s = self.entry_type.get()
        capacite = int(self.entry_cap.get())

        from Models.salle import Salle
        salle = Salle(code, libelle, type_s, capacite)

        resultat, message = self.service_salle.ajouter_salle(salle)
        print(message)

    def modifier_salle(self):
        code = self.entry_code.get()
        libelle = self.entry_libelle.get()
        type_s = self.entry_type.get()
        capacite = int(self.entry_cap.get())

        from models.salle import Salle
        salle = Salle(code, libelle, type_s, capacite)

        resultat, message = self.service_salle.modifier_salle(salle)
        print(message)

    def supprimer_salle(self):
        code = self.entry_code.get()
        self.service_salle.supprimer_salle(code)
        print("Salle supprimée")

    def rechercher_salle(self):
        code = self.entry_code.get()
        salle = self.service_salle.rechercher_salle(code)

        if salle:
            self.entry_libelle.delete(0, "end")
            self.entry_libelle.insert(0, salle.libelle)

            self.entry_type.delete(0, "end")
            self.entry_type.insert(0, salle.type)

            self.entry_cap.delete(0, "end")
            self.entry_cap.insert(0, salle.capacite)

            self.btn_modifier.configure(command=self.modifier_salle)
            self.btn_supprimer.configure(command=self.supprimer_salle)
            self.btn_rechercher.configure(command=self.rechercher_salle)