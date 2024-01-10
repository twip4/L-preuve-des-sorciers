from sorcier import *
from grille import *
from copy import copy
from collections import deque
from time import time


def chemin_mana_min(grille: Grille, sorcier: Sorcier, mana_depense=0):
    """
    Chemin-mana-min
    Cette fonction permet de trouver le chemin qui demande moins de mana au départ pour parcourir la grille
    :return: liste des tuples des coordonnées des cases à parcourir
    """
    # Condition d'arrêt
    if grille.x < 1 and grille.y < 1:
        return mana_depense, deque()

    # Variables
    mana_droite, mana_bas = None, None
    list_case_chemin_droite, list_case_chemin_bas = deque(), deque()
    case_droite, case_bas = grille.get_case((0, 1)), grille.get_case((1, 0))

    # Continuation du chemin
    if case_droite and isinstance(case_droite.get_valeur(), int) and sorcier.mana + case_droite.get_valeur() > 0:
        sorcier_droite = copy(sorcier)
        sorcier_droite.mana += case_droite.get_valeur()
        mana_droite, list_case_chemin_droite = chemin_mana_min(grille.copie_partielle_grille((0, 1)),
                                                               sorcier_droite,
                                                               mana_depense + case_droite.get_valeur())

    if case_bas and isinstance(case_bas.get_valeur(), int) and sorcier.mana + case_bas.get_valeur() > 0:
        sorcier_bas = copy(sorcier)
        sorcier_bas.mana += case_bas.get_valeur()
        mana_bas, list_case_chemin_bas = chemin_mana_min(grille.copie_partielle_grille((1, 0)),
                                                         sorcier_bas,
                                                         mana_depense + case_bas.get_valeur())

    # Renvoie des valeurs avec test qi les valeurs sont None
    if mana_droite is None and mana_bas is None:
        return mana_depense, deque()

    elif (mana_droite is not None and mana_bas is None) or (
            mana_droite is not None and mana_bas is not None and mana_droite > mana_bas):
        list_case_chemin_droite.append(case_droite.get_position())
        return mana_depense + mana_droite, list_case_chemin_droite

    else:  # if (mana_droite is None and mana_bas is not None) or (mana_bas < mana_droite):
        list_case_chemin_bas.append(case_bas.get_position())
        return mana_depense + mana_bas, list_case_chemin_bas


def chemin_optimal():
    """
    Chemin-optimal
    Cette fonction permet de trouver le chemin minimal pour parcourir une grille avec un magicien
    :return: liste des tuples des coordonnées des cases à parcourir
    """
    pass


grille = Grille(5, 5)
grille.affichage_matrice()
sorcier = Sorcier(20)

start = time()
mana, list_case_chemin = chemin_mana_min(grille, sorcier)
stop = time()
print("time : ", stop - start)

for i in list_case_chemin:
    grille.remplacement_valeur_etoile(i)
print(mana)
print(list_case_chemin)
grille.affichage_matrice()
