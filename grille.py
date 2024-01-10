from random import randint


def randint_zero_exclu(val_min, val_max):
    """Fonction randint avec exclusion de la valeur 0"""
    while True:
        num = randint(val_min, val_max)
        if num != 0:
            return num


class Case:
    def __init__(self, position, val_min, val_max):
        """

        :param val_min: valeur minimum de la case
        :param val_max: valeur maximum de la case
        """
        self.position = position
        self.valeur = randint_zero_exclu(val_min, val_max)

    def get_valeur(self):
        """Retourne la valeur de la case"""
        return self.valeur

    def set_valeur(self, valeur):
        """Set la valeur de la case"""
        self.valeur = valeur

    def get_position(self):
        """Retourne la position de la case"""
        return self.position

class Grille:
    """Classe Grille qui est une matrice qui représente une grille de nombre"""
    matrice = None

    def __init__(self, x, y, val_min=-5, val_max=5):
        """
        :param x: nombre de lignes
        :param y: nombre de colonnes
        :param val_min: valeur minimum des cases
        :param val_max: valeur maximum des cases
        """
        self.val_min = val_min
        self.val_max = val_max
        if x > 0 and y > 0:
            self.x = x
            self.y = y
            self.generation_matrice()
            self.remplacement_valeur_etoile((0, 0), '>')
            self.remplacement_valeur_etoile((x-1, y-1), '>')

    def generation_matrice(self):
        """Génère une matrice de x ligne et y colonne"""
        self.matrice = [[Case((y, x), self.val_min, self.val_max) for x in range(self.x)] for y in range(self.y)]

    def remplacement_valeur_etoile(self, position, char='*'):
        """Remplace une des valeurs de la matrice au coordonné x, y données avec le caractère char
        :param position : tuple x, y de la position de la valeur à remplacer
        :param char: caractère de remplacement
        : return True si remplacement fait sinon False
        """
        if position[0] < 0 or position[1] < 0 or position[0] >= self.y or position[1] >= self.x:
            return None
        self.matrice[position[1]][position[0]].set_valeur(char)

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
                    ligne_formate += f'\033[92m{case.valeur: >5}\033[0m '
                elif isinstance(case.get_valeur(), int) and case.get_valeur() < 0:
                    ligne_formate += f'\033[91m{case.valeur: >5}\033[0m '
                else:
                    ligne_formate += f'{case.valeur: >5} '
            print(ligne_formate)

    def copie_partielle_grille(self, position):
        """
        Copie partielle de la grille à partir d'un point

        exemple :
         > | 4 |-1
        -4 |-1 | 2
         3 | 2 |-1
        -4 | 3 |-5

        copie à partir de (1, 1) :
         -1 | 2
          2 |-1
          3 |-5

        copie à partir de (2, 1)
        2 |-1
        3 |-5

        :return: Grille
        """
        retour = Grille(0, 0)
        retour.y = self.y - position[1]
        retour.x = self.x - position[0]
        retour.matrice = [[element for j, element in enumerate(ligne) if j >= position[0]]
                          for i, ligne in enumerate(self.matrice) if i >= position[1]]
        return retour

    def get_matrice(self):
        """Retourne la matrice"""
        return self.matrice

    def get_taille(self):
        """Retourne la taille x, y de la matrice"""
        return self.x, self.y

    def get_case(self, position):
        """Retourne la case en fonction de la position"""
        if (position[1] >= 0 and position[0] >= 0) and (position[1] < self.x and position[0] < self.y):
            return self.matrice[position[1]][position[0]]
        return False
