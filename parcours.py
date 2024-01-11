from grille import *
from sorcier import *


def calcul_cout_matrice(grille: Grille):
    """
    Chemin-optimal
    Cette fonction permet de trouver le chemin minimal pour parcourir une grille avec un magicien
    :return: liste des tuples des coordonnées des cases à parcourir
    """
    x, y = grille.get_taille()
    cout = [[0 for _ in range(y)] for _ in range(x)]

    # Initialisation de la position de départ
    cout[0][0] = grille.get_case((0, 0)).get_valeur()

    # Calcul des coûts
    # Première ligne
    for j in range(1, y):
        cout[0][j] = cout[0][j - 1] + grille.get_case((0, j)).get_valeur()

    # Première colonne
    for i in range(1, x):
        cout[i][0] = cout[i - 1][0] + grille.get_case((i, 0)).get_valeur()

    # Autres cases
    for i in range(1, x):
        for j in range(1, y):
            cout[i][j] = max(cout[i - 1][j], cout[i][j - 1]) + grille.get_case((i, j)).get_valeur()
    return cout


def calcul_cout_matrice_inverse(grille: Grille):
    """
    Chemin-optimal
    Cette fonction permet de trouver le chemin minimal pour parcourir une grille avec un magicien
    :return: liste des tuples des coordonnées des cases à parcourir
    """
    x, y = grille.get_taille()
    cout = [[0 for _ in range(y)] for _ in range(x)]

    # Initialisation de la position de départ
    cout[x-1][y-1] = grille.get_case((x - 1, y - 1)).get_valeur()

    # Calcul des coûts
    # Dernière ligne
    for j in range(y - 2, -1, -1):
        cout[x - 1][j] = cout[x - 1][j + 1] + grille.get_case((x - 1, j)).get_valeur()

    # Dernière colonne
    for i in range(x - 2, -1, -1):
        cout[i][y - 1] = cout[i + 1][y - 1] + grille.get_case((i, y - 1)).get_valeur()

    # Autres cases
    for i in range(x - 2, -1, -1):
        for j in range(y - 2, -1, -1):
            cout[i][j] = max(cout[i + 1][j], cout[i][j + 1]) + grille.get_case((i, j)).get_valeur()
    return cout


def chemin_optimal(grille: Grille):
    cout = calcul_cout_matrice(grille)
    # Retracer le chemin
    chemin = []
    x, y = grille.get_taille()
    i, j = x - 1, y - 1
    while i >= 0 and j >= 0:
        chemin.append((i, j))
        if i == 0 and j == 0:
            break
        elif i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        else:
            if cout[i - 1][j] > cout[i][j - 1]:
                i -= 1
            else:
                j -= 1

    return chemin[::-1]


def chemin_mana_min(grille: Grille):
    cout = calcul_cout_matrice_inverse(grille)
    # Retracer le chemin
    chemin = []
    x, y = grille.get_taille()
    i, j = 0, 0
    while i <= x - 1 and j <= y - 1:
        chemin.append((i, j))
        if i == x - 1 and j == y - 1:
            break
        elif i == x - 1:
            j += 1
        elif j == y - 1:
            i += 1
        else:
            if cout[i + 1][j] > cout[i][j + 1]:
                i += 1
            else:
                j += 1

    return chemin