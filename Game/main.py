import pygame                               # Pygame
from player import Player                   # player.py
from icons import load_player_icon          # icons.py
from obstacles import Obstacle              # obstacles.py
from options import GameOptions             # options.py
from grounds import Ground                  # grounds.py
from backgrounds import Background          # backgrounds.py
from speeds_data import Speed               # speeds_data.py
from death import DeathManager              # death.py

# Initialisation de Pygame et des options de jeu
options = GameOptions()
pygame.init()
screen = pygame.display.set_mode((options.screen_width, options.screen_height))
pygame.display.set_caption("Python Dash - Playground Testing Game")

# Charger une icône pour la fenêtre
icon_path = "resources/UI/icon.jpeg"  # Remplacez "icon.png" par le chemin de votre icône
icon = pygame.image.load(icon_path)
pygame.display.set_icon(icon)  # Ajoute l'icône à la fenêtre du jeu

# Chargement des ressources et initialisation des objets
player = Player(load_player_icon(), options.screen_height // 8, options.screen_height)
ground = Ground(options.screen_width, options.screen_height, options.screen_height // 8, texture_count=5000)
background = Background(options.screen_width, options.screen_height, texture_count=5000)

# Listes des obstacles et des boosts
obstacles = []
speeds = []
obstacle_spawn_timer = 0
boost_spawn_timer = 0
spike_speed = options.obstacle_speed  # Vitesse fixe pour les `spikes` et `speeds`

# Boucle de jeu
running = True
clock = pygame.time.Clock()

h_pressed = False
mouse_held_down = False  # État pour suivre si le clic gauche est maintenu

while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h and not h_pressed:
                h_pressed = True
                options.toggle_hitboxes()
                print(f"Hitboxes {'activées' if options.show_hitboxes else 'désactivées'}.")
            elif event.key in (pygame.K_SPACE, pygame.K_UP):  # Saut (Barre d'espace ou Flèche du haut)
                player.jump()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic gauche
                mouse_held_down = True  # Début du maintien du clic
                player.jump()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Relâchement du clic gauche
                mouse_held_down = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_h:
                h_pressed = False

    # Gestion du saut continu avec clic gauche maintenu
    if mouse_held_down:
        player.jump()

    # Application de la gravité au joueur
    player.apply_gravity()

    # Ajustement de la vitesse des obstacles et du fond
    adjusted_obstacle_speed = spike_speed  # Utiliser la vitesse fixe des spikes

    # Spawn des obstacles
    obstacle_spawn_timer += 1
    if obstacle_spawn_timer > 100:  # Apparition toutes les 100 frames
        obstacles.append(Obstacle(options.screen_width, options.screen_height, adjusted_obstacle_speed, options.screen_height // 8))
        obstacle_spawn_timer = 0

    # Spawn des boosts (speeds), en évitant les positions des obstacles
    boost_spawn_timer += 1
    if boost_spawn_timer > 200:  # Apparition toutes les 200 frames
        spawn_valid = False
        while not spawn_valid:
            new_speed = Speed(options.screen_width + 50, options.screen_height, options.screen_height // 8, spike_speed)  # Utilise la vitesse des spikes
            spawn_valid = all(not new_speed.hitbox.intersects(obstacle.hitbox) for obstacle in obstacles)
        
        speeds.append(new_speed)
        boost_spawn_timer = 0

        # Message dans la console pour le type de speed apparu
        print(f"Le speed {new_speed.image_path.split('/')[-1].split('.')[0]} a apparu.")

    # Mise à jour des obstacles
    for obstacle in list(obstacles):
        obstacle.move()
        if obstacle.is_off_screen():
            obstacles.remove(obstacle)

    # Mise à jour des boosts
    for speed in list(speeds):
        speed.move()
        if speed.is_off_screen():
            speeds.remove(speed)
        elif player.check_collision(speed.hitbox):  # Collision avec le boost
            # Appliquer l'effet de vitesse du boost au joueur avec une limite
            new_speed = speed.apply_effect(player)
            spike_speed = min(new_speed, 2.0)  # Limiter la vitesse à un maximum raisonnable
            # Mise à jour des vitesses des obstacles existants
            for obstacle in obstacles:
                obstacle.speed = spike_speed
            speeds.remove(speed)

    # Mise à jour des vitesses des boosts
    for speed in list(speeds):
        speed.speed = spike_speed  # Assigner directement la vitesse des `speeds` à celle des obstacles

    # Vérification des collisions entre le joueur et les obstacles
    if DeathManager.check_collision(player.outer_hitbox, [obstacle.hitbox for obstacle in obstacles]):
        DeathManager.handle_death()
        running = False

    # Nettoyage de l'écran
    screen.fill((255, 255, 255))

    # Dessin des différents éléments
    background.draw(screen)  # Fond
    ground.move(adjusted_obstacle_speed)
    ground.draw(screen)  # Sol
    player.draw(screen, options.show_hitboxes)  # Joueur

    for obstacle in obstacles:
        obstacle.draw(screen, options.show_hitboxes)  # Obstacles

    for speed in speeds:
        speed.draw(screen, options.show_hitboxes)  # Boosts (Speeds)

    # Mise à jour de l'écran et limitation des FPS
    pygame.display.flip()
    clock.tick(options.fps_limit)

pygame.quit()
