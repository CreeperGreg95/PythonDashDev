import pygame
import random
import os

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Geometry Dash avec Pygame")

# Chargement des images
background = pygame.image.load("resources/bg01.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

cube_image = pygame.image.load("resources/iconkit/cube/cube01.png")
cube_size = 50
cube_image = pygame.transform.scale(cube_image, (cube_size, cube_size))

spike_image = pygame.image.load("resources/spike01.png")
spike_width, spike_height = 50, 50
spike_image = pygame.transform.scale(spike_image, (spike_width, spike_height))

# Paramètres du joueur
player_x = 100
player_y = SCREEN_HEIGHT - cube_size
player_velocity_y = 0
jump_strength = 15
gravity = 1
is_jumping = False
rotation_angle = 0

# Paramètres de l'obstacle
obstacle_x = SCREEN_WIDTH
obstacle_y = SCREEN_HEIGHT - spike_height
obstacle_speed = 5

# Boucle de jeu
running = True
clock = pygame.time.Clock()

while running:
    screen.blit(background, (0, 0))

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True
                player_velocity_y = -jump_strength

    # Gravité et saut
    if is_jumping:
        player_y += player_velocity_y
        player_velocity_y += gravity
        rotation_angle += 15  # Rotation du cube en saut
        if player_y >= SCREEN_HEIGHT - cube_size:
            player_y = SCREEN_HEIGHT - cube_size
            is_jumping = False
            rotation_angle = 0  # Réinitialiser la rotation une fois au sol

    # Rotation et affichage du cube
    rotated_cube = pygame.transform.rotate(cube_image, rotation_angle)
    cube_rect = rotated_cube.get_rect(center=(player_x + cube_size // 2, player_y + cube_size // 2))
    screen.blit(rotated_cube, cube_rect.topleft)

    # Déplacement de l'obstacle
    obstacle_x -= obstacle_speed
    if obstacle_x < -spike_width:
        obstacle_x = SCREEN_WIDTH
        obstacle_speed += 0.5  # Augmente la vitesse des obstacles pour augmenter la difficulté

    # Affichage de l'obstacle
    screen.blit(spike_image, (obstacle_x, obstacle_y))

    # Détection de collision
    player_rect = pygame.Rect(player_x, player_y, cube_size, cube_size)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, spike_width, spike_height)

    if player_rect.colliderect(obstacle_rect):
        print("Game Over!")
        running = False  # Arrête le jeu en cas de collision

    # Mise à jour de l'écran et limitation des FPS
    pygame.display.flip()
    clock.tick(30)

# Quitter Pygame
pygame.quit()
