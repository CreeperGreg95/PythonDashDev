import pygame                               # Pygame
from player import Player                   # player.py
from icons import load_player_icon          # icons.py
from obstacles import Obstacle              # obstacles.py
from options import GameOptions             # options.py
from keybinds import handle_event           # keybinds.py
from grounds import Ground                  # grounds.py
from backgrounds import Background          # backgrounds.py
from speeds_data import Speed               # speed.py

# Initialisation de Pygame et des options de jeu
options = GameOptions()
pygame.init()
screen = pygame.display.set_mode((options.screen_width, options.screen_height))
pygame.display.set_caption("Python Dash")

# Chargement des ressources et initialisation des objets
player = Player(load_player_icon(), options.screen_height // 8, options.screen_height)
ground = Ground(options.screen_width, options.screen_height, options.screen_height // 8, texture_count=5000)
background = Background(options.screen_width, options.screen_height, texture_count=5000)

# Listes des obstacles et des boosts
obstacles = []
speeds = []
obstacle_spawn_timer = 0
current_speed_factor = 1  # Facteur de vitesse initial

# Boucle de jeu
running = True
clock = pygame.time.Clock()

h_pressed = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h and not h_pressed:
                h_pressed = True
                options.toggle_hitboxes()
                print(f"Hitboxes {'activées' if options.show_hitboxes else 'désactivées'}.")
            elif event.key in (pygame.K_SPACE, pygame.K_UP): #Barre d'aspace et Flèche directionnelle du haut
                player.jump()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic gauche
                player.jump()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_h:
                h_pressed = False

    # Application de la gravité
    player.apply_gravity()

    # Ajustement des vitesses pour les obstacles et le fond
    adjusted_obstacle_speed = options.obstacle_speed * current_speed_factor
    # adjusted_background_speed = BACKGROUND_SPEED * current_speed_factor

    # Gérer les obstacles
    obstacle_spawn_timer += 1
    if obstacle_spawn_timer > 100:
        obstacles.append(Obstacle(options.screen_width, options.screen_height, adjusted_obstacle_speed, options.screen_height // 8))
        obstacle_spawn_timer = 0

    for obstacle in list(obstacles):
        obstacle.move()

        # Supprimer les obstacles hors écran
        if obstacle.is_off_screen():
            obstacles.remove(obstacle)

        # Vérifier les collisions avec le joueur
        if player.get_rect().colliderect(obstacle.get_rect()):
            print("Game Over!")
            running = False

    # Nettoyer l'écran
    screen.fill((255, 255, 255))

    # Déplacer et dessiner le fond avec la vitesse ajustée
    # background.move(adjusted_background_speed)
    background.draw(screen)

    # Dessiner le joueur
    player.draw(screen, options.show_hitboxes)
    # Déplacer et dessiner le sol
    ground.move(adjusted_obstacle_speed)
    ground.draw(screen)

    # Dessiner les obstacles et les boosts
    for obstacle in obstacles:
        obstacle.draw(screen, options.show_hitboxes)
    for speed in speeds:
        speed.draw(screen, options.show_hitboxes)

    # Mise à jour de l'écran et limitation des FPS
    pygame.display.flip()
    clock.tick(options.fps_limit)

pygame.quit()