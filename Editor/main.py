import pygame
import sys
import os

# Ajout du chemin du dossier contenant options.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../Game')))
from options import GameOptions

def main():
    # Initialisation de Pygame
    pygame.init()

    # Création des options de jeu
    options = GameOptions()

    # Définir les dimensions de la fenêtre
    screen = pygame.display.set_mode((options.screen_width, options.screen_height))
    pygame.display.set_caption("Game Editor")

    # Charger le fichier de fond
    bg_image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Resources/backgrounds/bg01.png'))
    bg_image = pygame.image.load(bg_image_path).convert()
    bg_width = bg_image.get_width()
    bg_height = bg_image.get_height()

    # Couleurs
    DARK_GRAY = (50, 50, 50)
    BLUE_OVERLAY = (0, 0, 255, 50)  # Surcouche bleue avec transparence
    TRANSPARENCY = 128  # Niveau de transparence pour le panneau (0-255)

    # Création du panneau
    panel_height = options.screen_height // 4
    panel_width = options.screen_width
    panel_rect = pygame.Surface((panel_width, panel_height), pygame.SRCALPHA)  # Surface avec transparence
    panel_rect.fill((*DARK_GRAY, TRANSPARENCY))

    # Boucle principale
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Dessiner l'arrière-plan uniquement dans la zone au-dessus du panneau
        bg_area_height = options.screen_height - panel_height
        for i in range((options.screen_width // bg_width) + 2):
            screen.blit(bg_image, (i * bg_width, 0), area=pygame.Rect(0, 0, bg_width, bg_area_height))

        # Ajouter une surcouche bleue uniquement dans la zone au-dessus du panneau
        blue_overlay = pygame.Surface((options.screen_width, bg_area_height), pygame.SRCALPHA)
        blue_overlay.fill(BLUE_OVERLAY)
        screen.blit(blue_overlay, (0, 0))

        # Dessiner le panneau en bas
        screen.blit(panel_rect, (0, options.screen_height - panel_height))

        # Mettre à jour l'affichage
        pygame.display.flip()

        # Limiter les FPS
        clock.tick(options.fps_limit)

    # Quitter Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
