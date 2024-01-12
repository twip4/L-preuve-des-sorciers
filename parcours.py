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


def chemin_potion_k(grille: Grille, chemin, k):
    temp_pot = []

    def est_valide_et_negatif(pos):
        return grille.est_dans_grille(pos) and grille.get_case(pos).get_valeur() < 0

    for pos in chemin:
        for direction in [(1, 0), (0, 1)]:  # Directions: droite et bas
            suite = []
            for i in range(k):
                nouvelle_pos = (pos[0] + i * direction[0], pos[1] + i * direction[1])
                if est_valide_et_negatif(nouvelle_pos):
                    suite.append(nouvelle_pos)
                else:
                    if i == 0:
                        pos = (pos[0] + direction[0], pos[1] + direction[1])
                        nouvelle_pos = (pos[0] + i * direction[0], pos[1] + i * direction[1])
                        if est_valide_et_negatif(nouvelle_pos):
                            suite.append(nouvelle_pos)
                        else:
                            break
                    else:
                        break
            if suite:
                temp_pot.append(suite)

    grille_optimal = []
    for i in range(len(temp_pot)):
        grille_copie = grille.copie_partielle_grille((0, 0))
        grille_copie.remplacement_valeurs_etoile(temp_pot[i], 0)
        # grille_copie.affichage_matrice()
        # print("\n")
        temp_chemin = chemin_mana_min(grille_copie)
        grille_optimal.append([temp_chemin, cout_chemin(grille_copie, temp_chemin), temp_pot[i]])

    max = grille_optimal[0]
    for i in range(len(grille_optimal)):
        if max[1] < grille_optimal[i][1]:
            max = grille_optimal[i]

    return max


def cout_chemin(grille: Grille, chemin):
    count = 0
    for pos in chemin:
        count += grille.get_case(pos).get_valeur()

    return count
