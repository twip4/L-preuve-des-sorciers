import pygame


class Main_menu_page:
    def __init__(self, screen):
        # Initialise la page du menu
        self.font = pygame.font.Font(None, 36)
        self.screen = screen

    def run(self):
        pygame.display.set_caption("Menu Principal")
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Clic gauche de la souris
                        if button_rect.collidepoint(event.pos):  # Vérifie si le clic est à l'intérieur du bouton
                            running = False

            # Efface l'écran
            self.screen.fill((255, 255, 255))  # Fond blanc

            text = self.font.render("Menu Principal", True, (0, 0, 0))
            text_rect = text.get_rect(center=(self.screen.get_width() // 2, (self.screen.get_height() // 2) - 100))
            self.screen.blit(text, text_rect)

            button_rect = self.create_button((self.screen.get_width() // 2), (self.screen.get_height() // 2), 80, 50,
                                             (133, 193, 233),
                                             (255, 255, 255), "Play")

            pygame.display.flip()

        return "quitter"

    def create_button(self, x, y, width, height, button_color, text_color, text):
        font = pygame.font.Font(None, 36)
        button_rect = pygame.Rect(x - width // 2, y - height // 2, width, height)

        pygame.draw.rect(self.screen, button_color, button_rect)
        pygame.draw.rect(self.screen, (0, 0, 0), button_rect, 2)

        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=button_rect.center)
        self.screen.blit(text_surface, text_rect)

        return button_rect




