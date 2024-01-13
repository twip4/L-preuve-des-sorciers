Cette SAÉ a été réalisé par Paul BAUDINOT et Maxime ICHOUNG-THOE.

# L'épreuve des sorciers

Pour réaliser cette SAÉ, nous avons décidé de choisir le langage Python avec de librairie standard pour que notre projet puisse s'exécuter facilement sur les ordinateurs de l'IUT sans problème.
Dans notre version de ce jeu, nous avons une grille 

## Exécution du projet

### Lancement

Pour lancer notre projet, il faut vérifier qu'une version de python 3 est installé sur votre ordinateur.
Ensuite, ouvrez un invite de commande placer vous dans le répertoire du projet avec la commande `ls` et lancez la commande suivante :

```bash
python main.py
```

### Utilisation

* **Lancement de l'application** : À l'ouverture de l'application, vous serez accueilli par une grille de démarrage de 2x2. Cette grille est le terrain de jeu où le sorcier doit optimiser son chemin.
* **Modification de la taille de la grille** : Pour changer la dimension de la grille, utilisez les deux curseurs situés sur le côté droit de la fenêtre. Le premier curseur ajuste le nombre de colonnes, tandis que le deuxième ajuste le nombre de lignes de la grille.
* **Génération de la nouvelle grille** : Après avoir défini les dimensions souhaitées avec les curseurs, cliquez sur le bouton situé à gauche des curseurs pour générer une grille à la taille choisie.
* **Analyse de la grille** : Les cases de la grille affichent des valeurs numériques. Les cases vertes représentent des valeurs positives, augmentant le mana du sorcier, tandis que les cases rouges représentent des valeurs négatives, réduisant son mana.
* **Calcul du chemin** : Vous pouvez maintenant utiliser les boutons en bas de la fenêtre pour calculer le chemin optimal pour le sorcier. Le bouton "Start minimum mana" calcule le chemin qui nécessite le moins de mana sans utiliser de potions, tandis que le bouton "Start minimum mana avec potion" permet d'inclure l'usage de potions pour optimiser le chemin.
* **Résultats** : Une fois le chemin calculé, la quantité de mana requise est affichée en bas à gauche de l'application, où "Mana" est la quantité de mana actuelle et "Mana minimum" est la quantité minimale nécessaire pour parcourir la grille sans perdre.

## Les principales fonctionnalités

Les fonctionnalités principales de notre projet sont :
* La génération de grille avec des valeurs positive et négatives en choisissant la plage de valeurs, mais aussi la proportion de nombre positif et négatif.
* Le parcours de grille pour trouver le meilleur chemin en utilisant ou nom des potions pour annuler des malus sur le mana du sorcier
* L'affichage des grilles et des parcours en fonction des algorithmes et de la taille de la grille.

## Explications des fonctions
Notre projet regroupe un certain nombre de fonctions plus ou moins complexe. 
Dans cette SAÉ les fonctions qui nous intéressent le plus sont les fonctions/méthodes servant à la génération et au parcours des grilles
C'est pour cela que nous avons choisi de vous faire une explication détaillée sur le fonctionnement des fonctions/méthodes suivantes : 
**`generation_matrice(self, pourcentage_negative)`**, **`calcul_cout_matrice(grille: Grille)`**, 
**`chemin_mana_min(grille: Grille)`**, **`chemin_potion(grille: Grille)`**, **`chemin_potion_k(grille: Grille, k)`**, 
**`cout_chemin(grille: Grille, chemin)`**, **`mana_min_requis(grille: Grille, chemin)`**.

### Generation_matrice
La fonction `calcul_cout_matrice` de la classe `Grille` est utilisée pour déterminer le coût associé à chaque case pour un personnage magicien se déplaçant dans une grille. La fonction est structurée comme suit :

* **Vérification des arguments** : 
   La fonction commence par s'assurer que les arguments fournis sont logiques et valides. Elle vérifie si la valeur minimale est inférieure à la valeur maximale, car il serait incohérent d'avoir une valeur minimale supérieure à la valeur maximale. Elle contrôle également que le pourcentage de cases négatives est compris entre 0 et 100 %.
* **Initialisation de la matrice de coût** : 
   Une matrice de coût est initialisée à zéro pour chaque case de la grille. Cette matrice est utilisée pour stocker le coût cumulatif pour atteindre chaque case à partir de la case de destination, qui est située en bas à droite de la grille.
* **Définition de la valeur de la case de départ** :
   La valeur de la case de départ est définie comme étant la valeur de la case située en bas à droite de la grille. C'est le point d'arrivée du magicien dans ce contexte.
* **Calcul des coûts pour les bords de la grille** : 
   Le coût pour la dernière ligne et la dernière colonne de la grille est calculé en se déplaçant de droite à gauche pour la ligne, et de bas en haut pour la colonne, en cumulant les valeurs des cases.
* **Calcul des coûts pour le reste de la grille** : 
   Pour les cases restantes, le coût est déterminé en prenant le maximum entre le coût de la case juste en dessous et celui de la case à droite, puis en y ajoutant la valeur de la case courante. Cela assure que le chemin choisi soit celui qui maximise le coût cumulatif à chaque étape, comme le jeu pourrait le requérir.
* **Retour de la matrice de coût** :
   La fonction retourne ensuite la matrice de coût complétée. Cette matrice peut être utilisée pour tracer le chemin optimal que le magicien peut emprunter pour se déplacer à travers la grille

### Calcul_cout_matrice
La fonction `calcul_cout_matrice` est utilisée pour déterminer le coût associé à chaque case pour un personnage magicien se déplaçant dans une grille. La fonction est structurée comme suit :

* **Vérification des arguments** : 
   La fonction commence par s'assurer que les arguments fournis sont logiques et valides. Elle vérifie si la valeur minimale est inférieure à la valeur maximale, car il serait incohérent d'avoir une valeur minimale supérieure à la valeur maximale. Elle contrôle également que le pourcentage de cases négatives est compris entre 0 et 100 %.
* **Initialisation de la matrice de coût** : 
   Une matrice de coût est initialisée à zéro pour chaque case de la grille. Cette matrice est utilisée pour stocker le coût cumulatif pour atteindre chaque case à partir de la case de destination, qui est située en bas à droite de la grille.
* **Définition de la valeur de la case de départ** :
   La valeur de la case de départ est définie comme étant la valeur de la case située en bas à droite de la grille. C'est le point d'arrivée du magicien dans ce contexte.
* **Calcul des coûts pour les bords de la grille** : 
   Le coût pour la dernière ligne et la dernière colonne de la grille est calculé en se déplaçant de droite à gauche pour la ligne, et de bas en haut pour la colonne, en cumulant les valeurs des cases.
* **Calcul des coûts pour le reste de la grille** : 
   Pour les cases restantes, le coût est déterminé en prenant le maximum entre le coût de la case juste en dessous et celui de la case à droite, puis en y ajoutant la valeur de la case courante. Cela assure que le chemin choisi soit celui qui maximise le coût cumulatif à chaque étape, comme le jeu pourrait le requérir.
* **Retour de la matrice de coût** :
   La fonction retourne ensuite la matrice de coût complétée. Cette matrice peut être utilisée pour tracer le chemin optimal que le magicien peut emprunter pour se déplacer à travers la grille

### Chemin_mana_min
La fonction `chemin_mana_min` est responsable de trouver le chemin qui nécessite le minimum de mana pour qu'un magicien puisse traverser une grille donnée. Elle utilise les informations de la matrice des coûts pour tracer un chemin optimal à travers la grille. Voici la procédure détaillée de cette fonction :

* **Calcul de la matrice des coûts** :
   La fonction commence par calculer la matrice des coûts en utilisant la fonction `calcul_cout_matrice`. Cette matrice contient le coût cumulatif pour atteindre chaque case depuis la case de départ en bas à droite de la grille, en se déplaçant uniquement vers le haut ou vers la gauche.

* **Initialisation du chemin** :
   Un tableau `chemin` est initialisé pour stocker les coordonnées des cases que le magicien devra traverser. On récupère également les dimensions de la grille (`x` pour le nombre de lignes et `y` pour le nombre de colonnes) et on initialise les indices `i` et `j` à 0 pour commencer le tracé du chemin depuis le coin supérieur gauche de la grille.
* **Construction du chemin** :
   La boucle `while` construit le chemin en ajoutant les coordonnées actuelles à la liste `chemin`. Elle continue jusqu'à ce que le coin inférieur droit de la grille soit atteint.
* **Détermination de la direction** :
   À chaque étape, la fonction décide si elle doit se déplacer horizontalement ou verticalement. Elle rompt la boucle si la destination finale est atteinte. Si le magicien est sur la dernière ligne, il ne peut que se déplacer horizontalement. Si le magicien est sur la dernière colonne, il ne peut que se déplacer verticalement. Dans les autres cas, la fonction choisit la direction en comparant les coûts des cases adjacentes : elle se déplace vers la case qui a le coût le plus élevé, en supposant que le magicien cherche à maximiser les coûts (ou les points, ou le mana, selon la logique du jeu).
* **Retour du chemin** :
   Enfin, après avoir traversé la grille, la fonction retourne la liste `chemin` qui contient les coordonnées des cases formant le chemin optimal de mana minimal pour le magicien.

### Chemin_potion
La fonction `chemin_potion` calcule le chemin optimal qu'un magicien peut emprunter en utilisant une potion magique dans une grille de jeu. La potion a le pouvoir de transformer la valeur de la case la plus défavorable (la plus basse) en une valeur neutre (zéro), ce qui pourrait potentiellement offrir un meilleur chemin. Voici les étapes détaillées de cette fonction :

* **Trouver le chemin initial sans potion** :
   La fonction commence par trouver le chemin nécessitant le moins de mana pour traverser la grille sans l'utilisation de potions, en utilisant la fonction `chemin_mana_min`.
* **Collecte des valeurs des cases du chemin** :
   Ensuite, pour chaque case du chemin initial, la fonction collecte les valeurs associées à ces cases dans une liste `case_val`.
* **Identification de la case avec la valeur minimale** :
   La fonction détermine ensuite la valeur la plus basse sur le chemin, qui représente la case la plus pénalisante pour le magicien.
* **Optimisation du chemin avec la potion** :
   Pour chaque position dans le chemin où la valeur minimale est rencontrée, la fonction crée une copie de la grille, remplace la valeur de cette case par zéro (simulant l'effet de la potion), puis recalcule le chemin de mana minimal dans cette grille modifiée.
* **Retourner le meilleur chemin après utilisation de la potion** :
   Finalement, après avoir évalué les chemins avec les positions transformées, la fonction retourne le premier chemin optimal trouvé comme le meilleur chemin possible avec l'utilisation d'une potion.

### Chemin_potion_k
La fonction `chemin_potion_k` est conçue pour déterminer le chemin optimal qu'un personnage, tel qu'un magicien, peut emprunter en utilisant un nombre spécifique de potions magiques pour neutraliser les cases négatives sur une grille. Voici un descriptif détaillé de la fonction :

* **Calcul du chemin initial sans potion** :
   La fonction débute par le calcul du chemin nécessitant le moins de mana sans l'utilisation de potions, en appelant `chemin_mana_min`.
* **Initialisation de la liste des positions temporaires des potions** :
   Une liste `temp_pot` est créée pour stocker les emplacements potentiels où les potions pourraient être utilisées.
* **Définition d'une fonction pour tester la validité et la négativité d'une case** :
   La fonction interne `est_valide_et_negatif` vérifie si une case donnée est à l'intérieur des limites de la grille et si sa valeur est négative.
* **Exploration des positions pour l'utilisation des potions** :
   La fonction parcourt le chemin initial et examine chaque case pour déterminer si l'utilisation d'une potion est possible, en considérant la direction droite et bas depuis la position actuelle.
   Pour chaque case, la fonction vérifie jusqu'à `k` positions dans les directions spécifiées pour identifier les suites de cases négatives qui pourraient être neutralisées par l'utilisation des potions.
* **Construction des chemins optimisés avec l'utilisation des potions** :
   Pour chaque ensemble de positions de potions identifiées, la fonction crée une copie de la grille, remplace les valeurs négatives par zéro pour simuler l'effet des potions, et recalcule le chemin de mana minimal.
* **Sélection du meilleur chemin optimisé** :
   Parmi tous les chemins optimisés générés, la fonction sélectionne celui avec le coût le plus élevé, en supposant que le magicien cherche à maximiser son gain. Si plusieurs chemins ont le même coût optimal, elle choisit celui qui est le plus proche du départ pour minimiser les risques de "mort" précoce.
* **Retour du chemin optimal** :
   Enfin, le chemin sélectionné comme optimal, avec l'usage de jusqu'à `k` potions, est retourné.

### Cout_chemin
La fonction `cout_chemin` est une fonction utilitaire qui calcule le coût total d'un chemin à travers une grille pour un personnage de jeu tel qu'un magicien. Voici une explication pas à pas de cette fonction :

* **Initialisation du compteur de coût** :
   La fonction démarre avec l'initialisation d'une variable `count` à 0. Cette variable servira à cumuler les valeurs des cases tout au long du chemin parcouru par le magicien.
* **Parcours des cases du chemin** :
   La fonction itère ensuite sur chaque position dans la liste `chemin` fournie en argument. Pour chaque position, elle récupère la valeur de la case correspondante dans la grille.
   Au cours de cette itération, elle additionne la valeur de chaque case rencontrée sur le chemin à la variable `count`. Cette valeur peut être positive ou négative en fonction de la nature de la case : une case positive augmente le total (représentant un gain pour le magicien), tandis qu'une case négative le diminue (représentant un coût ou une perte de mana, par exemple).
* **Retour du coût total du chemin** :
   Après avoir parcouru toutes les cases du chemin, la fonction retourne la valeur cumulée dans `count`, qui représente le coût total du chemin pour le personnage.


### Mana_min_requis
La fonction `mana_min_requis` est conçue pour déterminer la quantité minimale de mana requise pour un personnage, tel qu'un magicien, pour parcourir un chemin spécifique dans une grille de jeu. Voici une explication détaillée de son fonctionnement :

* **Initialisation des compteurs** :
   La fonction commence par initialiser deux variables, `val_min` et `cpt`. `val_min` sera utilisée pour stocker la quantité totale de mana minimum requise, tandis que `cpt` servira à suivre le mana cumulatif tout au long du chemin.
* **Parcours du chemin** :
   Ensuite, la fonction itère sur chaque position dans le chemin. Pour chaque case sur le chemin, elle récupère la valeur de cette case à partir de la grille.
* **Calcul du mana nécessaire** :
   Pour chaque case, la fonction calcule `val`, qui est la somme du mana cumulatif actuel (`cpt`) et la valeur de la case actuelle. Si `val` est négatif, cela signifie que le personnage a besoin de mana supplémentaire pour continuer à parcourir le chemin sans épuiser son mana.
   Dans ce cas, la fonction ajoute la valeur absolue de `val` à `cpt` pour rétablir le mana à zéro ou plus, et ajoute également cette valeur à `val_min`, la quantité totale de mana supplémentaire requise.
* **Mise à jour du mana cumulatif** :
   Après avoir traité chaque case, la fonction met à jour `cpt` en y ajoutant la valeur de la case actuelle, qu'elle soit positive ou négative.
* **Retour de la quantité minimale de mana requise** :
   Enfin, après avoir parcouru tout le chemin, la fonction retourne `val_min`, qui est la quantité totale de mana minimum nécessaire pour que le personnage puisse parcourir le chemin sans épuiser son mana.
