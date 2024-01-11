import tkinter as tk
from sorcier import *
from grille import *
from parcours import *
from PIL import Image, ImageTk
import subprocess
import time


class ParametresPage(tk.Frame):
    def __init__(self, parent, appTk):
        super().__init__(parent)
        self.app = appTk
        self.parent = parent

        self.label_x = tk.Label(self, text="X:")
        self.label_y = tk.Label(self, text="Y:")
        self.label_mana = tk.Label(self, text="Mana:")

        self.scale_x = tk.Scale(self, from_=2, to=100, orient="horizontal")
        self.scale_y = tk.Scale(self, from_=2, to=100, orient="horizontal")
        self.scale_mana = tk.Scale(self, from_=1, to=100, orient="horizontal")

        self.button_valider = tk.Button(self, text="Valider", command=self.valider_parametres)

        self.label_x.grid(row=0, column=0)
        self.label_y.grid(row=1, column=0)
        self.label_mana.grid(row=2, column=0)

        self.scale_x.grid(row=0, column=1)
        self.scale_y.grid(row=1, column=1)
        self.scale_mana.grid(row=2, column=1)

        self.button_valider.grid(row=3, columnspan=2)

    def valider_parametres(self):
        x = int(self.scale_x.get())
        y = int(self.scale_y.get())
        mana = int(self.scale_mana.get())
        self.app.changer_page(MainPage, x, y, mana)


class MainPage(tk.Frame):
    def __init__(self, parent, appTk, x, y, mana):
        super().__init__(parent)
        self.mana_final = None
        self.chemin_mana_mini = None
        self.image_id = None
        self.app = app
        self.parent = parent
        self.x = x
        self.y = y
        self.mana = mana

        # Générer la grille
        self.grille = Grille(self.y, self.x)
        self.matrice = self.grille.get_matrice()

        # Init sorcier
        self.sorcier = Sorcier(self.mana)

        # Zone de travail
        self.zone = [1280, 600]
        self.taille = self.grille.get_taille()

        # Taille de case
        self.width_case = self.zone[0] / self.x
        self.height_case = self.zone[1] / self.y
        self.start_pos = [0, 0]

        # Init image sorcier
        self.image = Image.open("img/sorcier.png")
        self.image = self.image.resize((int(self.width_case), int(self.height_case)))
        self.photo = ImageTk.PhotoImage(self.image)

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

        # Bouton pour revenir aux paramètres
        self.bouton_start = tk.Button(self, text="Start", command=self.start)
        self.bouton_start.pack(side="bottom", padx=10, pady=10)

    def generer_grille(self):
        self.grille.affichage_matrice()
        x, y = self.start_pos  # Utilisez des variables locales pour la position de départ

        for ligne in self.matrice:
            for case in ligne:
                if isinstance(case.get_valeur(), int) and case.get_valeur() > 0:
                    fill_color = "#28B463"  # Vert
                elif isinstance(case.get_valeur(), int) and case.get_valeur() < 0:
                    fill_color = "#C0392B"  # Rouge
                else:
                    fill_color = "#D7DBDD"  # Gris

                self.zone_grill.create_rectangle(x, y, x + self.width_case, y + self.height_case, fill=fill_color)
                val = case.get_valeur()
                self.zone_grill.create_text(x + (self.width_case // 2), y + (self.height_case // 2), text=str(val), font=("Arial", 500 // max(self.taille)), fill="black")
                x += self.width_case  # Déplacer x pour la prochaine case

            y += self.height_case  # Déplacer y pour la prochaine ligne
            x = self.start_pos[0]  # Réinitialiser x au début de la ligne

    def retour_aux_parametres(self):
        self.app.changer_page(ParametresPage)

    def start(self):
        self.x = self.start_pos[0]
        self.y = self.start_pos[1]
        self.image_id = self.zone_grill.create_image(self.x, self.y, image=self.photo, anchor=tk.NW)
        self.mana_final, self.chemin_mana_mini = chemin_mana_min(self.grille,self.sorcier)
        self.deplacer_chemin(0)


    def lire_wav(self, num):
        # Chemin vers le fichier WAV
        chemin_wav = ["sound/minecraft_hit.wav", "sound/minecraft_drinking.wav", "sound/minecraft_levelup.wav"]

        # Lancer la commande afplay pour lire le fichier WAV
        subprocess.Popen(["afplay", chemin_wav[num]])

    def deplacer_chemin(self, index):
        if index < len(self.chemin_mana_mini):
            if index > 1 :
                pos = self.chemin_mana_mini[index-1]
                x, y = pos[0]*self.width_case, pos[1]*self.height_case

                self.zone_grill.create_rectangle(x, y, x + self.width_case, y + self.height_case, fill="#85C1E9")
                val = self.matrice[pos[1]][pos[0]].get_valeur()
                self.zone_grill.create_text(x + (self.width_case // 2), y + (self.height_case // 2), text=str(val),
                                            font=("Arial", 500 // max(self.taille)), fill="black")

            pos = self.chemin_mana_mini[index]
            val = self.matrice[pos[1]][pos[0]].get_valeur()
            if val != ">":
                self.mana += val
                self.texte_mana.config(text=f"Mana: {self.mana}")
                if val > 0:
                    self.lire_wav(2)
                if val < 0:
                    self.lire_wav(0)
            self.deplacer_image(pos[0], pos[1])
            self.zone_grill.after(1000, lambda: self.deplacer_chemin(index + 1))
    def deplacer_image(self, x, y):
        # Déplacer l'image vers la droite
        self.x = self.width_case * x
        self.y = self.height_case * y

        # Mettre à jour la position de l'image sur le canvas
        self.zone_grill.coords(self.image_id, self.x, self.y)


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
