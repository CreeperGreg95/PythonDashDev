# main.py version 9

import pygame                               # Pygame
from player import Player                   # player.py
from icons import load_player_icon          # icons.py
from obstacles import Obstacle              # obstacles.py
from options import GameOptions             # options.py
from keybinds import handle_event           # keybinds.py
from grounds import Ground                  # grounds.py
from backgrounds import Background          # backgrounds.py

# Initialisation de Pygame et des options de jeu
options = GameOptions()
pygame.init()
screen = pygame.display.set_mode((options.screen_width, options.screen_height))
pygame.display.set_caption("Python Dash")

# Chargement des ressources et initialisation des objets
player = Player(load_player_icon(), options.screen_height // 8, options.screen_height)  # Passer screen_height ici
ground = Ground(options.screen_width, options.screen_height, options.screen_height // 8, texture_count=5000)
background = Background(options.screen_width, options.screen_height, texture_count=5000)

# Liste des obstacles et chronomètre pour leur apparition
obstacles = []
obstacle_spawn_timer = 0  # Chronomètre pour générer les obstacles

# Variable pour contrôler la vitesse du background (modifiable facilement)
BACKGROUND_SPEED = options.obstacle_speed * options.background_speed_factor  # Le fond se déplace plus lentement

# Boucle de jeu
running = True
clock = pygame.time.Clock()

# Sauvegarde de la taille initiale de l'écran pour référence
initial_screen_height = options.screen_height

while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:  # Touche H
               player.toggle_inner_hitbox() 
        handle_event(event, player, options)

    # Si la fenêtre est agrandie (hauteur augmentée), ajuster la position du joueur
    new_screen_height = pygame.display.get_surface().get_height()
    if new_screen_height > initial_screen_height:  # Si l'écran est agrandi
        delta_y = (new_screen_height - initial_screen_height) // 10  # Décalage proportionnel
        player.y += delta_y  # Déplacer le joueur vers le bas uniquement quand l'écran est agrandi

        # Mettre à jour la taille de l'écran initial pour les futures comparaisons
        initial_screen_height = new_screen_height

    # Application de la gravité et déplacement des obstacles
    player.apply_gravity()

    # Gérer les obstacles (ajout et suppression)
    obstacle_spawn_timer += 1
    if obstacle_spawn_timer > 100:  # Générer un obstacle toutes les 100 frames environ
        obstacles.append(Obstacle(options.screen_width, options.screen_height, options.obstacle_speed, options.screen_height // 8))
        obstacle_spawn_timer = 0

    for obstacle in list(obstacles):  # Utilisation de list() pour éviter les conflits lors de la suppression
        obstacle.move()

        # Supprimer les obstacles qui sont hors écran
        if obstacle.is_off_screen():
            obstacles.remove(obstacle)

        # Vérifier les collisions avec le joueur
        if player.get_rect().colliderect(obstacle.get_rect()):
            print("Game Over!")

    # Nettoyer l'écran à chaque frame pour éviter les artefacts
    screen.fill((255, 255, 255))  # Fond blanc (ou une autre couleur de fond)

    # Déplacer et dessiner le fond à la vitesse contrôlée par BACKGROUND_SPEED
    background.move(BACKGROUND_SPEED)  # Utilisation de la vitesse modifiable
    background.draw(screen)  # Dessiner le fond

    # Dessin du joueur
    player.draw(screen)

    # Dessiner les obstacles
    for obstacle in obstacles:
        obstacle.draw(screen, options.show_hitboxes)

    # Déplacer et dessiner le sol
    ground.move(options.obstacle_speed)  # Déplace le sol à la vitesse normale
    ground.draw(screen)  # Dessiner le sol

    # Affichage des hitboxes si activées
    if options.show_hitboxes:
        pygame.draw.rect(screen, (0, 0, 139), player.get_rect(), 2)  # Hitbox du joueur en bleu foncé

    # Mise à jour de l'écran et limitation des FPS
    pygame.display.flip()
    clock.tick(options.fps_limit)  # Utilisation de la limite des FPS définie dans les options

# Quitter Pygame
pygame.quit()
 