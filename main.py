import tkinter as tk
from sorcier import *
from grille import *


class ParametresPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.parent = parent

        self.label_x = tk.Label(self, text="X:")
        self.label_y = tk.Label(self, text="Y:")
        self.label_mana = tk.Label(self, text="Mana:")

        self.entry_x = tk.Entry(self)
        self.entry_y = tk.Entry(self)
        self.entry_mana = tk.Entry(self)

        self.button_valider = tk.Button(self, text="Valider", command=self.valider_parametres)

        self.label_x.grid(row=0, column=0)
        self.label_y.grid(row=1, column=0)
        self.label_mana.grid(row=2, column=0)

        self.entry_x.grid(row=0, column=1)
        self.entry_y.grid(row=1, column=1)
        self.entry_mana.grid(row=2, column=1)

        self.button_valider.grid(row=3, columnspan=2)

    def valider_parametres(self):
        x = int(self.entry_x.get())
        y = int(self.entry_y.get())
        mana = int(self.entry_mana.get())
        self.app.changer_page(MainPage, x, y, mana)


class MainPage(tk.Frame):
    def __init__(self, parent, app, x, y, mana):
        super().__init__(parent)
        self.app = app
        self.parent = parent
        self.x = x
        self.y = y
        self.mana = mana

        # Générer la grille
        self.grille = Grille(self.x, self.y)
        self.matrice = self.grille.get_matrice()

        # Init sorcier
        self.sorcier = Sorcier(self.mana)

        # Zone de travail
        self.zone = [1280, 600]
        self.taille = self.grille.get_taille()

        # Taille de case
        self.width_case = self.zone[0] // self.x
        self.height_case = self.zone[1] // self.y
        self.start_pos = [0, 0]

        # Init zone d'affichage de la grille
        self.zone_grill = tk.Canvas(self, width=self.zone[0], height=self.zone[1], bg="white")
        self.zone_grill.pack()

        self.generer_grille()

        # Bouton pour revenir aux paramètres
        self.bouton_retour = tk.Button(self, text="Retour aux paramètres", command=self.retour_aux_parametres)
        self.bouton_retour.pack(side="right", padx=10, pady=10)

        # Texte indiquant le nombre de mana
        self.texte_mana = tk.Label(self, text=f"Mana: {self.mana}")
        self.texte_mana.pack(side="left", padx=10, pady=10)

    def generer_grille(self):
        for x in range(0, self.x):
            for y in range(0, self.y):
                # couleur de chaque case
                if self.matrice[x][y].get_valeur() == ">" or self.matrice[x][y].get_valeur() == "*":
                    color = "#D7DBDD"
                elif self.matrice[x][y].get_valeur() > 0:
                    color = "#28B463"
                else:
                    color = "#C0392B"

                self.zone_grill.create_rectangle(self.start_pos[0], self.start_pos[1],
                                                 self.start_pos[0] + self.width_case,
                                                 self.start_pos[1] + self.height_case, fill=color)

                # texte dans chaque case
                val = str(self.matrice[x][y].get_valeur())
                self.zone_grill.create_text(self.start_pos[0] + self.width_case // 2,
                                            self.start_pos[1] + self.height_case // 2, text=val,
                                            font=("Arial", 500 // max(self.taille)), fill="black")

                self.start_pos[1] = (self.start_pos[1] + self.height_case) % self.zone[1]

            self.start_pos[0] = (self.start_pos[0] + self.width_case) % self.zone[0]

    def retour_aux_parametres(self):
        self.app.changer_page(ParametresPage)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.page_actuelle = None
        self.title("L'epreuve des sorciers")
        self.geometry("1280x720")

        self.pages = {}
        self.changer_page(ParametresPage)

    def changer_page(self, page_classe, *args):
        if self.pages:
            self.pages[self.page_actuelle].pack_forget()

        self.page_actuelle = page_classe.__name__
        page = page_classe(self, self, *args)
        self.pages[self.page_actuelle] = page
        page.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
