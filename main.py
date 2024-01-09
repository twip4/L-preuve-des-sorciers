from grille import *
from sorcier import *
from tkinter import *

grille = Grille(20, 20)
matrice = grille.get_matrice()
zone = [1280, 600]
taille = grille.get_taille()
width_case = zone[0] // taille[0]
height_case = zone[1] // taille[1]
start_pos = [0, 0]

root = Tk()
root.title("L'epreuce des sorciers")
root.geometry("1280x720")
root.resizable(False, False)

zone_grill = Canvas(root, width=1280, height=600)
zone_grill.pack()

for x in range(0, taille[0]):
    for y in range(0, taille[1]):
        if matrice[x][y].get_valeur() == ">" or matrice[x][y].get_valeur() == "*":
            color = "#D7DBDD"
        elif matrice[x][y].get_valeur() > 0:
            color = "#28B463"
        else:
            color = "#C0392B"

        zone_grill.create_rectangle(start_pos[0], start_pos[1], start_pos[0] + width_case,
                                    start_pos[1] + height_case, fill=color)

        val = str(matrice[x][y].get_valeur())
        zone_grill.create_text(start_pos[0] + width_case // 2, start_pos[1] + height_case // 2, text=val,
                               font=("Arial", 500 // max(taille)), fill="black")

        start_pos[1] = (start_pos[1] + height_case) % zone[1]

    start_pos[0] = (start_pos[0] + width_case) % zone[0]

root.mainloop()
