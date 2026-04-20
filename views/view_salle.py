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