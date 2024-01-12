from random import randint, shuffle
from copy import *


class Case:
    def __init__(self, position, valeur):
        self.position = position
        self.valeur = valeur

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

    def __init__(self, x, y, rand_matrice=True, pourcentage_negative=70, val_min=-5, val_max=5):
        """
        :param x: nombre de lignes
        :param y: nombre de colonnes
        :param val_min: valeur minimum des cases
        :param val_max: valeur maximum des cases
        """
        self.val_min = val_min
        self.val_max = val_max
        self.x = x
        self.y = y
        self.matrice = [[Case((i, j), 0) for j in range(self.y)] for i in range(self.x)]
        if rand_matrice:
            self.generation_matrice(pourcentage_negative)

    def generation_matrice(self, pourcentage_negative):
        """Génère une matrice de x ligne et y colonne"""
        # Erreur de valeur
        if self.val_min > self.val_max:
            raise ValueError("val_min > val_max")
        if pourcentage_negative < 0 or pourcentage_negative > 100:
            raise ValueError("pourcentage_negative < 0 ou pourcentage_negative > 100")

        nb_val = self.x * self.y

        if self.val_min > 0 or self.val_max < 0:
            self.matrice = [[Case((x, y), randint(self.val_min, self.val_max)) for y in range(self.y)]
                            for x in range(self.x)]
        elif self.val_min == self.val_max:
            self.matrice = [[Case((x, y), self.val_min) for y in range(self.y)] for x in range(self.x)]
        else:
            nb_val_negative = int(nb_val * pourcentage_negative / 100)
            nb_val_positive = nb_val - nb_val_negative

            val_negative = [randint(self.val_min, -1) for _ in range(nb_val_negative)]
            val_positive = [randint(1, self.val_max) for _ in range(nb_val_positive)]

            tab_valeur = val_positive + val_negative
            shuffle(tab_valeur)
            self.matrice = [[Case((x, y), tab_valeur[x * self.y + y]) for y in range(self.y)] for x in range(self.x)]

    def remplacement_valeur_etoile(self, position, char='*'):
        """Remplace une des valeurs de la matrice au coordonné x, y données avec le caractère char
        :param position : tuple x, y de la position de la valeur à remplacer
        :param char: caractère de remplacement
        : return True si remplacement fait sinon False
        """
        if position[0] < 0 or position[1] < 0 or position[0] >= self.x or position[1] >= self.y:
            raise ValueError("La position n'est pas dans la grille")
        self.matrice[position[0]][position[1]].set_valeur(char)

    def remplacement_valeurs_etoile(self, positions, char='*'):
        """Remplace une des valeurs de la matrice au coordonné x, y données avec le caractère char
        :param positions : tuple x, y de la position de la valeur à remplacer
        :param char: caractère de remplacement
        : return True si remplacement fait sinon False
        """
        for pos in positions:
            self.remplacement_valeur_etoile(pos, char)

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
        retour.x = self.x - position[0]
        retour.y = self.y - position[1]
        retour.matrice = [[copy(element) for j, element in enumerate(ligne) if j >= position[1]]
                          for i, ligne in enumerate(self.matrice) if i >= position[0]]
        return retour

    def get_matrice(self):
        """Retourne la matrice"""
        return self.matrice

    def get_taille(self):
        """Retourne la taille x, y de la matrice"""
        return self.x, self.y

    def get_case(self, position):
        """Retourne la case en fonction de la position"""
        if (position[0] >= 0 and position[1] >= 0) and (position[0] < self.x and position[1] < self.y):
            return self.matrice[position[0]][position[1]]
        raise ValueError("La position n'est pas par")

    def set_grille(self, valeurs):
        """Set le grille avec des valeurs données"""
        if len(valeurs) < self.x:
            raise ValueError("Tailles de la matrice valeurs incorrect")
        for valeur_y in valeurs:
            if len(valeur_y) != self.y:
                raise ValueError("Tailles de la matrice valeurs incorrect")

        for i in range(len(valeurs)):
            for j in range(len(valeurs[i])):
                self.matrice[i][j].set_valeur(valeurs[i][j])
