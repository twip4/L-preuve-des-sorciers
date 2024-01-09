from sorcier import *
from grille import *
from main_menu_page import *
import pygame

grille = Grille(20, 20)
matrice = grille.get_matrice()
zone = [1280, 600]
taille = grille.get_taille()
width_case = zone[0] // taille[0]
height_case = zone[1] // taille[1]
start_pos = [0, 0]

pygame.init()

font = pygame.font.Font(None, 500 // max(taille))

width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

main_page = Main_menu_page(screen)

main_page.run()

screen.fill((0, 0, 0))

for x in range(0, taille[0]):
    for y in range(0, taille[1]):
        print(start_pos)
        if matrice[x][y].get_valeur() == ">" or matrice[x][y].get_valeur() == "*":
            pygame.draw.rect(screen, (215, 219, 221), (start_pos[0], start_pos[1], width_case, height_case))
        elif matrice[x][y].get_valeur() > 0:
            pygame.draw.rect(screen, (40, 180, 99), (start_pos[0], start_pos[1], width_case, height_case))
        else:
            pygame.draw.rect(screen, (192, 57, 43), (start_pos[0], start_pos[1], width_case, height_case))

        text_surface = font.render(str(matrice[x][y].get_valeur()), True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (start_pos[0] + width_case // 2, start_pos[1] + height_case // 2)
        screen.blit(text_surface, text_rect)

        start_pos[1] = (start_pos[1] + height_case) % zone[1]

    start_pos[0] = (start_pos[0] + width_case) % zone[0]

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    pygame.time.Clock().tick(60)
