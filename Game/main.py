# main.py version 6

import pygame
from player import Player
from icons import load_player_icon
from obstacles import Obstacle
from options import GameOptions
from keybinds import handle_event
from grounds import Ground  # Importation de la classe Ground
from backgrounds import Background  # Importation de la classe Background

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Python Dash")

# Chargement des ressources et initialisation des objets
options = GameOptions()

# Calcul du décalage du sol (1/8 de la hauteur de la fenêtre)
ground_height = 400 // 8  # 1/8 de la hauteur de l'écran

# Crée le joueur avec la position ajustée
player = Player(load_player_icon(), ground_height)

# Crée l'obstacle en passant également ground_height
obstacle = Obstacle(800, options.obstacle_speed, ground_height)

# Crée le sol avec 5000 textures
ground = Ground(800, 400, ground_height, texture_count=5000)

# Crée le background avec 5000 images
background = Background(800, 400, texture_count=5000)

# Variable pour contrôler la vitesse du background (modifiable facilement)
BACKGROUND_SPEED = options.obstacle_speed / 10  # Ici, le fond se déplace plus lentement que les obstacles

# Boucle de jeu
running = True
clock = pygame.time.Clock()

while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        handle_event(event, player, options)

    # Application de la gravité et déplacement des obstacles
    player.apply_gravity()
    obstacle.move()

    # Détection de collision
    if player.get_rect().colliderect(obstacle.get_rect()):
        print("Game Over!")

    # Nettoyer l'écran à chaque frame pour éviter les artefacts
    screen.fill((255, 255, 255))  # Fond blanc (ou une autre couleur de fond)

    # Déplacer et dessiner le fond à la vitesse contrôlée par BACKGROUND_SPEED
    background.move(BACKGROUND_SPEED)  # Utilisation de la vitesse modifiable
    background.draw(screen)  # Dessiner le fond

    # Dessin du joueur et de l'obstacle
    player.draw(screen)  # Dessin du joueur
    obstacle.draw(screen, options.show_hitboxes)  # Dessin de l'obstacle et de sa hitbox

    # Déplacer et dessiner le sol
    ground.move(options.obstacle_speed)  # Déplace le sol à la vitesse normale
    ground.draw(screen)  # Dessiner le sol

    # Affichage des hitboxes si activées
    if options.show_hitboxes:
        pygame.draw.rect(screen, (255, 0, 0), player.get_rect(), 2)  # Dessine la hitbox du joueur en rouge

    # Mise à jour de l'écran et limitation des FPS
    pygame.display.flip()
    clock.tick(60)

# Quitter Pygame
pygame.quit()