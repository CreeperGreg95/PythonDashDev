#Robot1Compiler

import pygame

# Initialisation de Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Charger les images
head_img = pygame.image.load("resources/iconkit/robots/robot_1/tête_1.png").convert_alpha()
legs_img = pygame.image.load("resources/iconkit/robots/robot_1/jambes_1.png").convert_alpha()
feet_img = pygame.image.load("resources/iconkit/robots/robot_1/pieds_1.png").convert_alpha()

# Taille des images
head_height = head_img.get_height()
legs_height = legs_img.get_height()
feet_height = feet_img.get_height()

# Position initiale
robot_x = 300
robot_y = 400  # Position du sol (base des pieds)
robot_jump = False
jump_velocity = -15
gravity = 1
vertical_velocity = 0

def draw_robot(base_x, base_y, jump_progress):
    """Dessine le robot avec toutes ses parties attachées."""
    # Position de la tête
    head_x = base_x
    head_y = base_y - legs_height 

    # Position des jambes
    legs_x = base_x
    legs_y = base_y - legs_height 

    # Position des pieds
    feet_x = base_x
    feet_y = base_y - feet_height

    # Dessiner les composants
    screen.blit(head_img, (head_x, head_y))
    screen.blit(legs_img, (legs_x, legs_y))
    screen.blit(feet_img, (feet_x, feet_y))

# Boucle principale
running = True
while running:
    screen.fill((30, 30, 30))  # Fond

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not robot_jump:
            robot_jump = True
            vertical_velocity = jump_velocity

    # Gestion du saut
    if robot_jump:
        vertical_velocity += gravity
        robot_y += vertical_velocity
        if robot_y >= 400:  # Revenir au sol
            robot_y = 400
            robot_jump = False
            vertical_velocity = 0

    # Calcul du progrès pour l'animation (non utilisé ici mais prêt pour des améliorations)
    jump_progress = -vertical_velocity if robot_jump else 0

    # Dessiner le robot
    draw_robot(robot_x, robot_y, jump_progress)

    # Mettre à jour l'écran
    pygame.display.flip()
    clock.tick(60)

pygame.quit()