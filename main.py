import tkinter as tk
from parcours import *
from PIL import Image, ImageTk
import subprocess
from grille import *
from sorcier import *


class MainPage(tk.Frame):
    def __init__(self, parent, appTk):
        super().__init__(parent)
        self.app = appTk
        self.parent = parent
        self.initialize_variables()
        self.initialize_ui()

    def initialize_variables(self):
        # Initialisation des variables
        self.pos_potion = None
        self.mana_final = None
        self.chemin_mana_mini = None
        self.image_id = None
        self.x = 2
        self.y = 2
        self.mana = 1
        self.mana_mini = None
        self.mana_start = 1
        self.flag_parcour = 0
        self.potion = 1

        # Création de la grille et initialisation du sorcier
        self.grille = Grille(self.y, self.x)
        self.start_grill = self.grille
        self.matrice = self.grille.get_matrice()
        self.sorcier = Sorcier(self.mana)

        # Configuration de la zone de travail
        self.zone = [1280, 600]
        self.taille = self.grille.get_taille()
        self.width_case = self.zone[0] / self.x
        self.height_case = self.zone[1] / self.y
        self.start_pos = [0, 0]

    def initialize_ui(self):
        # Configuration des éléments de l'interface utilisateur
        self.configure_image()
        self.configure_canvas()
        self.configure_controls()

    def configure_image(self):
        # Chargement et configuration de l'image du sorcier
        self.image = Image.open("img/sorcier.png")
        self.image = self.image.resize((int(self.width_case), int(self.height_case)))
        self.photo = ImageTk.PhotoImage(self.image)

    def configure_canvas(self):
        # Configuration du canvas pour la grille
        self.zone_grill = tk.Canvas(self, width=self.zone[0], height=self.zone[1], bg="white")
        self.zone_grill.pack()
        self.generer_grille()

    def configure_controls(self):
        # Slider pour le mana
        self.texte_mana = tk.Label(self, text=f"Mana : {self.mana}")
        self.texte_mana.pack(side="left", padx=10, pady=10)

        self.texte_mana_mini = tk.Label(self, text=f"Mana minimun : {self.mana_mini}")
        self.texte_mana_mini.pack(side="left", padx=10, pady=10)

        self.genere_min_mana_requis()

        self.slider_mana = tk.Scale(self, from_=1, to=50, orient="horizontal", command=self.maj_mana)
        self.slider_mana.set(self.mana)
        self.slider_mana.pack(side="left", padx=10, pady=10)

        # Boutons pour les algorithmes
        self.bouton_start1 = tk.Button(self, text="Start minimum mana",
                                       command=self.start_chemin_mana_depart_min)
        self.bouton_start1.pack(side="left", padx=3, pady=3)

        self.bouton_start2 = tk.Button(self, text="Start minimum mana avec potion",
                                       command=self.start_chemin_mana_depart_min_potion)
        self.bouton_start2.pack(side="left", padx=3, pady=3)

        self.slider_potion = tk.Scale(self, from_=1, to=20, orient="horizontal", label="nb potion",
                                      command=self.k_potion)
        self.slider_potion.set(self.y)
        self.slider_potion.pack(side="left", padx=10, pady=10)

        # Bouton pour la régénération et sliders pour la taille de la grille
        self.bouton_regenere = tk.Button(self, text="🔄", command=self.regenere)
        self.bouton_regenere.pack(side="left", padx=10, pady=10)

        self.slider_taille_x = tk.Scale(self, from_=2, to=100, orient="horizontal", label="Largeur Grille",
                                        command=self.maj_taille_grille_y)
        self.slider_taille_x.set(self.x)
        self.slider_taille_x.pack(side="left", padx=10, pady=10)

        self.slider_taille_y = tk.Scale(self, from_=2, to=100, orient="horizontal", label="Hauteur Grille",
                                        command=self.maj_taille_grille_x)
        self.slider_taille_y.set(self.y)
        self.slider_taille_y.pack(side="left", padx=10, pady=10)

    def regenere(self):
        self.recharge_grill()
        self.mana = self.mana_start
        self.texte_mana.config(text=f"Mana: {self.mana}")

    def maj_mana(self, val):
        self.mana = int(val)
        self.mana_start = self.mana
        self.texte_mana.config(text=f"Mana: {self.mana}")

    def maj_taille_grille_x(self, val):
        self.x = int(val)

    def maj_taille_grille_y(self, val):
        self.y = int(val)

    def recharge_grill(self):
        self.zone_grill.delete("all")
        self.width_case = self.zone[0] / self.x
        self.height_case = self.zone[1] / self.y
        self.image = self.image.resize((int(self.width_case), int(self.height_case)))
        self.photo = ImageTk.PhotoImage(self.image)
        self.grille = Grille(self.y, self.x)
        self.taille = self.grille.get_taille()
        self.start_grill = self.grille
        self.matrice = self.grille.get_matrice()
        self.generer_grille()
        self.genere_min_mana_requis()

    def k_potion(self, val):
        self.potion = int(val)

    def genere_min_mana_requis(self):
        self.chemin_mana_mini = chemin_mana_min(self.grille)
        self.mana_mini = mana_min_requis(self.grille,self.chemin_mana_mini)
        self.texte_mana_mini.config(text=f"Mana minimun : {self.mana_mini}")
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
                self.zone_grill.create_text(x + (self.width_case // 2), y + (self.height_case // 2), text=str(val),
                                            font=("Arial", 500 // max(self.taille)), fill="black")
                x += self.width_case  # Déplacer x pour la prochaine case

            y += self.height_case  # Déplacer y pour la prochaine ligne
            x = self.start_pos[0]  # Réinitialiser x au début de la ligne

    def start_chemin_mana_depart_min(self):
        self.flag_parcour = 0
        self.grille = self.start_grill
        self.matrice = self.grille.get_matrice()
        self.generer_grille()
        self.mana = self.mana_start
        self.texte_mana.config(text=f"Mana: {self.mana}")
        self.image_id = self.zone_grill.create_image(self.start_pos[0],
                                                     self.start_pos[1],
                                                     image=self.photo,
                                                     anchor=tk.NW)
        self.chemin_mana_mini = chemin_mana_min(self.grille)
        # or pos in self.chemin_mana_mini:
        # self.grille.remplacement_valeur_etoile(pos)
        self.deplacer_chemin(0)

    def start_chemin_mana_depart_min_potion(self):
        self.flag_parcour = 0
        self.grille = self.start_grill
        self.matrice = self.grille.get_matrice()
        self.generer_grille()
        self.mana = self.mana_start
        self.texte_mana.config(text=f"Mana: {self.mana}")
        self.image_id = self.zone_grill.create_image(self.start_pos[0],
                                                     self.start_pos[1],
                                                     image=self.photo,
                                                     anchor=tk.NW)
        temp = chemin_potion_k(self.grille,self.potion)
        self.grille = temp[3]
        self.matrice = self.grille.get_matrice()
        self.pos_potion = temp[2]
        self.chemin_mana_mini = temp[0]
        self.deplacer_chemin(0)

    # def start_chemin_plus_rapide_mana(self):
    #     self.flag_parcour = 0
    #     self.generer_grille()
    #     self.mana = self.mana_start
    #     self.texte_mana.config(text=f"Mana: {self.mana}")
    #     self.image_id = self.zone_grill.create_image(self.start_pos[0],
    #                                                  self.start_pos[1],
    #                                                  image=self.photo,
    #                                                  anchor=tk.NW)
    #     self.chemin_mana_mini = chemin_optimal(self.grille)
    #     self.deplacer_chemin(0)

    def lire_wav(self, num):
        # Chemin vers le fichier WAV
        chemin_wav = ["sound/minecraft_hit.wav", "sound/minecraft_drinking.wav", "sound/minecraft_levelup.wav"]

        # Lancer la commande afplay pour lire le fichier WAV
        subprocess.Popen(["afplay", chemin_wav[num]])

    def deplacer_chemin(self, index):
        if self.flag_parcour == 1:
            return
        if index < len(self.chemin_mana_mini):
            if index >= 1:
                pos = self.chemin_mana_mini[index - 1]
                x, y = pos[1] * self.width_case, pos[0] * self.height_case
                if self.pos_potion is not None and (pos[0], pos[1]) in self.pos_potion:
                    self.zone_grill.create_rectangle(x, y, x + self.width_case, y + self.height_case, fill="#A569BD")
                    try:
                        # self.lire_wav(1)
                        pass
                    except:
                        pass
                else:
                    self.zone_grill.create_rectangle(x, y, x + self.width_case, y + self.height_case, fill="#85C1E9")
                val = self.matrice[pos[0]][pos[1]].get_valeur()
                self.zone_grill.create_text(x + (self.width_case // 2), y + (self.height_case // 2), text=str(val),
                                            font=("Arial", 500 // max(self.taille)), fill="black")

            pos = self.chemin_mana_mini[index]
            val = self.matrice[pos[0]][pos[1]].get_valeur()
            if val != ">":
                self.mana += val
                self.texte_mana.config(text=f"Mana: {self.mana}")
                if val > 0:
                    try:
                        # self.lire_wav(2)
                        pass
                    except:
                        pass

                if val < 0:
                    try:
                        # self.lire_wav(0)
                        pass
                    except:
                        pass
            self.deplacer_image(pos[1], pos[0])
            if self.mana >= 0:
                self.zone_grill.after(500, lambda: self.deplacer_chemin(index + 1))
            else:
                # Text de game over
                self.pos_potion = None
                self.zone_grill.create_text(640, 300, text="Game Over !!!",
                                            font=("Arial", 100), fill="black")
        else:
            # Text de win
            self.pos_potion = None
            self.zone_grill.create_text(640, 300, text="You Win !!!",
                                        font=("Arial", 100), fill="black")

    def deplacer_image(self, x, y):
        # Mettre à jour la position de l'image sur le canvas
        self.zone_grill.coords(self.image_id, self.width_case * x, self.height_case * y)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.page_actuelle = None
        self.title("L'epreuve des sorciers")
        self.geometry("1280x720")

        self.pages = {}
        self.changer_page(MainPage)

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
