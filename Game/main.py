# main.py Version 2

import pygame
from player import Player
from icons import load_player_icon
from obstacles import Obstacle
from backgrounds import load_background, draw_background
from options import GameOptions

from keybinds import handle_event

# Initialisation de Pygame et des options de jeu
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Python Dash")

# Chargement des ressources et initialisation des objets
background = load_background()
icon = load_player_icon()
player = Player(icon)
options = GameOptions()
obstacle = Obstacle(800, options.obstacle_speed)

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

    player_pos = player.get_position()
    obstacle_pos = obstacle.get_position()

    # Calcul de l'offset entre le joueur et l'obstacle pour la détection de collision
    offset_x = obstacle_pos[0] - player_pos[0]
    offset_y = obstacle_pos[1] - player_pos[1]

    # Détection de collision
    if player.get_rect().colliderect(obstacle.get_rect()):
        print("Game Over!")
        # running = False - désactivé car relou lol

    
    # Nettoyer l'écran à chaque frame pour éviter les artefacts
    screen.fill((255, 255, 255))  # Fond blanc (ou une autre couleur de fond)

    # Dessin des éléments
    draw_background(screen, background) #Dessin L'arrière-plan
    player.draw(screen) #Dessin Le joueur
    obstacle.draw(screen, options.show_hitboxes) #Dessin L'obstacle

        # Affichage des hitboxes si activées
    if options.show_hitboxes:
        pygame.draw.rect(screen, (255, 0, 0), player.get_rect(), 2)  # Dessine la hitbox du joueur en rouge

    # Mise à jour de l'écran et limitation des FPS
    pygame.display.flip()
    clock.tick(60)

# Quitter Pygame
pygame.quit()
