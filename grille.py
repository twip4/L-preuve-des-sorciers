from random import randint


def randint_zero_exclu(val_min, val_max):
    """Fonction randint avec exclusion de la valeur 0"""
    while True:
        num = randint(val_min, val_max)
        if num != 0:
            return num


class Case:
    def __init__(self, val_min, val_max):
        """

        :param val_min: valeur minimum de la case
        :param val_max: valeur maximum de la case
        """
        # self.position = (0, 0)
        self.valeur = randint_zero_exclu(val_min, val_max)

    def get_valeur(self):
        """Retourne la valeur de la case"""
        return self.valeur

    def set_valeur(self, valeur):
        """Set la valeur de la case"""
        self.valeur = valeur


class Grille:
    """Classe Grille qui est une matrice qui représente une grille de nombre"""

    def __init__(self, x, y, val_min=-5, val_max=5):
        """
        :param x: nombre de lignes
        :param y: nombre de colonnes
        :param val_min: valeur minimum des cases
        :param val_max: valeur maximum des cases
        """
        self.x = x
        self.y = y
        self.val_min = val_min
        self.val_max = val_max
        self.matrice = self.generation_matrice()
        self.remplacement_valeur_etoile((0, 0), '>')

    def generation_matrice(self):
        """Génère une matrice de x ligne et y colonne"""
        return [[Case(self.val_min, self.val_max) for _ in range(self.y)] for _ in range(self.x)]

    def remplacement_valeur_etoile(self, position, char='*'):
        """Remplace une des valeurs de la matrice au coordonné x, y données avec le caractère char
        :param position : tuple x, y de la position de la valeur à remplacer
        :param char: caractère de remplacement
        : return True si remplacement fait sinon False
        """
        if position[0] < 0 or position[1] < 0 or position[0] >= self.x or position[1] >= self.y:
            return None
        self.matrice[position[0]][position[1]].set_valeur(char)
        return True

    def affichage_matrice(self):
        """
        Affiche la matrice en mettant en couleurs les caractère nécessaire :
            rouge les valeurs < 0 des cases
            vert les valeurs >0 des cases
            blanc le reste.
        """
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

    def get_matrice(self):
        """Retourne la matrice"""
        return self.matrice

    def get_taille(self):
        """Retourne la taille x, y de la matrice"""
        return self.x, self.y