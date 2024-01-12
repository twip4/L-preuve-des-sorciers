from grille import *


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


def chemin_potion_k(grille: Grille, k):
    # premier chemin
    chemin = chemin_mana_min(grille)
    # position temporaire des potions
    temp_pot = []

    # test de la case si elle est valide et si elle est négative
    def est_valide_et_negatif(pos):
        return grille.est_dans_grille(pos) and grille.get_case(pos).get_valeur() < 0

    # pour toute les positions du chemin initial tester les potions
    for pos in chemin:
        # directions droite et bas
        for direction in [(1, 0), (0, 1)]:
            suite = []
            # pour le nombre de potions max
            for i in range(k):
                # position de la potion
                nouvelle_pos = (pos[0] + i * direction[0], pos[1] + i * direction[1])
                # si c'est posible
                if est_valide_et_negatif(nouvelle_pos):
                    # ajouter a la liste
                    suite.append(nouvelle_pos)

                # la case actuelle est une case positive
                else:
                    # si c'est la premiere
                    if i == 0:
                        # modifier la position
                        pos = (pos[0] + direction[0], pos[1] + direction[1])
                        nouvelle_pos = (pos[0] + i * direction[0], pos[1] + i * direction[1])
                        # refaire la verification pour les cases autour
                        if est_valide_et_negatif(nouvelle_pos):
                            suite.append(nouvelle_pos)
                        else:
                            break
                    else:
                        break
            # si la suite d'instruction n'est pas vide alors l'appende
            if suite:
                temp_pot.append(suite)

    grille_optimal = []
    # boucle sur le nombre de suite de potin possible
    for i in range(len(temp_pot)):
        # copie de la grille actuelle dans une nouvelle pour ne pas la modifier
        grille_copie = grille.copie_partielle_grille((0, 0))
        # remplacement des case de potion par des 0
        grille_copie.remplacement_valeurs_etoile(temp_pot[i], 0)
        # grille_copie.affichage_matrice()
        # print("\n")
        # nouveau calcul d'un chemin optimiser avec les 0
        temp_chemin = chemin_mana_min(grille_copie)
        # ajout des info dans la liste
        grille_optimal.append([temp_chemin, cout_chemin(grille_copie, temp_chemin), temp_pot[i], grille_copie])

    # recherche de la solution optimal ou si plusieur similaire de la plus proche du depart pour evité les morts au depart
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


def mana_min_requis(grille: Grille, chemin):
    val_min = 0
    cpt = 0

    for pos in chemin:
        case = int(grille.get_case(pos).get_valeur())
        val = cpt + int(grille.get_case(pos).get_valeur())
        if val < 0:
            cpt += abs(val)
            val_min += abs(val)
        cpt += case
    return val_min
