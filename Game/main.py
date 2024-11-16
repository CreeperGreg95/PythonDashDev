# main.py version 5

import pygame
from player import Player
from icons import load_player_icon
from obstacles import Obstacle
from backgrounds import load_background, draw_background
from options import GameOptions
from keybinds import handle_event
from grounds import Ground  # Importation de la classe Ground

# Initialisation de Pygame et des options de jeu
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Python Dash")

# Chargement des ressources et initialisation des objets
background = load_background()
icon = load_player_icon()
options = GameOptions()

# Calcul du décalage du sol (1/8 de la hauteur de la fenêtre)
ground_height = 400 // 8  # 1/8 de la hauteur de l'écran

# Crée le joueur avec la position ajustée
player = Player(icon, ground_height)

# Crée l'obstacle en passant également ground_height
obstacle = Obstacle(800, options.obstacle_speed, ground_height)

# Crée le sol avec 5000 textures
ground = Ground(800, 400, ground_height, texture_count=5000)

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

    # Dessin des éléments
    draw_background(screen, background)  # Dessin de l'arrière-plan
    player.draw(screen)  # Dessin du joueur
    obstacle.draw(screen, options.show_hitboxes)  # Dessin de l'obstacle et de sa hitbox

    # Déplacer et dessiner le sol
    ground.move(options.obstacle_speed)  # Déplace le sol à la vitesse de l'obstacle
    ground.draw(screen)  # Dessiner le sol

    # Affichage des hitboxes si activées
    if options.show_hitboxes:
        pygame.draw.rect(screen, (255, 0, 0), player.get_rect(), 2)  # Dessine la hitbox du joueur en rouge

    # Mise à jour de l'écran et limitation des FPS
    pygame.display.flip()
    clock.tick(60)

# Quitter Pygame
pygame.quit()
