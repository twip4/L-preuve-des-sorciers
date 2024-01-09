from random import randint


def randint_zero_exclu(min, max):
    while True:
        num = randint(min, max)
        if num != 0:
            return num


class Grille:
    """Classe Grille qui est une matrice qui représente une grille de nombre"""
    matrice = None

    def __init__(self, taille, val_min=-5, val_max=5):
        self.taille = taille
        self.val_min = val_min
        self.val_max = val_max
        self.matrice = self.generation_matrice()

    def affichage_matrice(self):
        for ligne in self.matrice:
            ligne_formattee = ' '.join([
           f'\033[92m{element: >3}\033[0m' if element > 0 else f'\033[91m{element: >3}\033[0m' if element < 0 else f'{element: >3}'for element in ligne])
            print(ligne_formattee)

    def generation_matrice(self):
        return [[randint_zero_exclu(self.val_min, self.val_max, ) for _ in range(self.taille)] for _ in range(self.taille)]

    def remplacement_valeur_etoile(self, x, y):
        self.matrice[x][y] = 0


grille = Grille(20)
grille.affichage_matrice()
grille.remplacement_valeur_etoile(0,0)
print("\n")
grille.affichage_matrice()
