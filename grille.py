from random import randint


def randint_zero_exclu(val_min, val_max):
    while True:
        num = randint(val_min, val_max)
        if num != 0:
            return num


class Case:
    def __init__(self, val_min, val_max):
        # self.position = (0, 0)
        self.valeur = randint_zero_exclu(val_min, val_max)

    def get_valeur(self):
        return self.valeur

    def set_valeur(self, valeur):
        self.valeur = valeur


class Grille:
    """Classe Grille qui est une matrice qui représente une grille de nombre"""

    def __init__(self, taille, val_min=-5, val_max=5):
        self.taille = taille
        self.val_min = val_min
        self.val_max = val_max
        self.matrice = self.generation_matrice()

    def affichage_matrice(self):
        for ligne in self.matrice:
            ligne_formate = ' '
            for case in ligne:
                if isinstance(case.get_valeur(), int) and case.get_valeur() > 0:
                    ligne_formate += f'\033[92m{case.valeur: >3}\033[0m '
                elif isinstance(case.get_valeur(), int) and case.get_valeur() < 0:
                    ligne_formate += f'\033[91m{case.valeur: >3}\033[0m '
                else:
                    ligne_formate += f'{case.valeur: >3} '
            print(ligne_formate)

    def generation_matrice(self):
        return [[Case(self.val_min, self.val_max) for _ in range(self.taille)] for _ in range(self.taille)]

    def remplacement_valeur_etoile(self, x, y):
        self.matrice[x][y].set_valeur('*')


grille = Grille(20)
grille.affichage_matrice()
grille.remplacement_valeur_etoile(0, 0)
print("\n")
grille.affichage_matrice()
