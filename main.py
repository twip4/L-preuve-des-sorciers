from sorcier import *
from grille import *
from main_menu_page import *
import pygame

grille = Grille(40)
matrice = grille.get_matrice()
zone = [1280, 600]
width_case = zone[0] // grille.get_size()
height_case = zone[1] // grille.get_size()
start_pos = [0, 60]

pygame.init()

width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

main_page = Main_menu_page(screen)

main_page.run()

screen.fill((0, 0, 0))

for x in range(0, grille.get_size()):
    for y in range(0, grille.get_size()):
        start_pos[1] = (start_pos[1] + height_case) % zone[1]
        if matrice[x][y].get_valeur() > 0:
            pygame.draw.rect(screen, (40, 180, 99), (start_pos[0], start_pos[1], width_case, height_case))
        else:
            pygame.draw.rect(screen, (192, 57, 43), (start_pos[0], start_pos[1], width_case, height_case))
    start_pos[0] = (start_pos[0] + width_case) % zone[0]
pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    pygame.time.Clock().tick(60)
