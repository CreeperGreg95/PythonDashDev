import pygame
import sys
import os

# Ajout du chemin du dossier contenant options.py et bg_color.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../Game')))
from options import GameOptions
from bg_color import apply_color_overlay

def main():
    pygame.init()

    # Création des options de jeu
    options = GameOptions()

    # Définir les dimensions de la fenêtre
    screen = pygame.display.set_mode((options.screen_width, options.screen_height))
    pygame.display.set_caption("Game Editor")

    # Charger et redimensionner l'image de fond
    bg_image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Resources/backgrounds/bg01.png'))
    bg_image = pygame.image.load(bg_image_path).convert_alpha()  # Assurez-vous que l'image supporte la transparence

    zoom_factor = 0.35  # Réduction de la taille
    bg_image = pygame.transform.scale(bg_image, (int(bg_image.get_width() * zoom_factor), int(bg_image.get_height() * zoom_factor)))

    # Appliquer la superposition de couleur sur l'image
    overlay_color = (40, 125, 255)  # Bleu pour la superposition
    overlay_opacity = 100  # Opacité de la superposition (transparence)
    filtered_bg = apply_color_overlay(bg_image, overlay_color, overlay_opacity)

    bg_width, bg_height = filtered_bg.get_size()

    # Couleurs
    DARK_GRAY = (50, 50, 50)
    TRANSPARENCY = 150  # Niveau de transparence pour le panneau (0-255)

    # Création du panneau
    panel_height = options.screen_height // 4
    panel_rect = pygame.Surface((options.screen_width, panel_height), pygame.SRCALPHA)
    panel_rect.fill((*DARK_GRAY, TRANSPARENCY))

    # Position et déplacement de la caméra
    cam_x, cam_y = 0, 0
    dragging = False
    last_mouse_x, last_mouse_y = 0, 0

    # Boucle principale
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = event.pos
                if mouse_y < options.screen_height - panel_height:
                    dragging = True
                    last_mouse_x, last_mouse_y = mouse_x, mouse_y

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                dragging = False

            if event.type == pygame.MOUSEMOTION and dragging:
                dx, dy = event.pos[0] - last_mouse_x, event.pos[1] - last_mouse_y
                cam_x += dx
                cam_y += dy
                last_mouse_x, last_mouse_y = event.pos

        # Effacer l'écran
        screen.fill((0, 0, 0))

        # Génération dynamique des images de fond
        min_x, max_x = (cam_x // bg_width) - 2, ((cam_x + options.screen_width) // bg_width) + 2
        min_y, max_y = (cam_y // bg_height) - 2, ((cam_y + options.screen_height) // bg_height) + 2

        for i in range(min_x, max_x + 1):
            for j in range(min_y, max_y + 1):
                screen.blit(filtered_bg, (i * bg_width - cam_x, j * bg_height - cam_y))

        # Dessiner le panneau en bas
        screen.blit(panel_rect, (0, options.screen_height - panel_height))

        pygame.display.flip()
        clock.tick(options.fps_limit)

    pygame.quit()

if __name__ == "__main__":
    main()
