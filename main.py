import pygame
import os
import subprocess

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 400, 300

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 122, 255)
DARK_BLUE = (0, 82, 204)

# Police
FONT = pygame.font.Font(None, 36)

# Créer la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PythonDash Launcher")

# Boutons (dimensions et positions)
button_width, button_height = 150, 50
playtesting_button_rect = pygame.Rect((WIDTH // 2 - button_width // 2, HEIGHT // 2 - 70), (button_width, button_height))
editor_button_rect = pygame.Rect((WIDTH // 2 - button_width // 2, HEIGHT // 2 + 20), (button_width, button_height))

def draw_button(screen, rect, text, hover):
    color = DARK_BLUE if hover else BLUE
    pygame.draw.rect(screen, color, rect, border_radius=10)
    text_surface = FONT.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

# Boucle principale
running = True
while running:
    screen.fill(WHITE)

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Clic gauche
            if playtesting_button_rect.collidepoint(event.pos):
                # Lancer Game/main.py
                subprocess.Popen(['python', os.path.join('Game', 'main.py')])
            elif editor_button_rect.collidepoint(event.pos):
                # Lancer Editor/main.py
                subprocess.Popen(['python', os.path.join('Editor', 'main.py')])

    # Vérifier le survol des boutons
    mouse_pos = pygame.mouse.get_pos()
    playtesting_hover = playtesting_button_rect.collidepoint(mouse_pos)
    editor_hover = editor_button_rect.collidepoint(mouse_pos)

    # Dessiner les boutons
    draw_button(screen, playtesting_button_rect, "Playtesting", playtesting_hover)
    draw_button(screen, editor_button_rect, "Editeur", editor_hover)

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
