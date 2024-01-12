from grille import *
from sorcier import *


def calcul_cout_matrice_inverse(grille: Grille):
    """
    Chemin-optimal
    Cette fonction permet de trouver le chemin minimal pour parcourir une grille avec un magicien
    :return: liste des tuples des coordonnées des cases à parcourir
    """
    x, y = grille.get_taille()
    cout = [[0 for _ in range(y)] for _ in range(x)]

    # Initialisation de la position de départ
    cout[x - 1][y - 1] = grille.get_case((x - 1, y - 1)).get_valeur()

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


def chemin_potion(grille: Grille):
    chemin = chemin_mana_min(grille)
    case_val = []

    for count in chemin:
        case_val.append(grille.get_case(count).get_valeur())

    min_val = min(case_val)
    positions = [index for index, val in enumerate(case_val) if val == min_val]

    grille_optimal = []
    for i in range(len(positions)):
        grille_copie = grille.copie_partielle_grille((0, 0))
        grille_copie.remplacement_valeur_etoile(chemin[positions[i]], 0)
        temp_chemin = chemin_mana_min(grille_copie)
        grille_optimal.append([temp_chemin, cout_chemin(grille_copie, temp_chemin), chemin[positions[i]], grille_copie])

    return grille_optimal[0]


def cout_chemin(grille: Grille, chemin):
    count = 0
    for pos in chemin:
        count += grille.get_case(pos).get_valeur()

    return count
