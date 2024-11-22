import pygame

# Initialisation de Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Charger les images
head_img = pygame.image.load("resources/iconkit/robots/robot_1/tête_1.png").convert_alpha()
legs_img = pygame.image.load("resources/iconkit/robots/robot_1/jambes_1.png").convert_alpha()
feet_img = pygame.image.load("resources/iconkit/robots/robot_1/pieds_1.png").convert_alpha()

# Charger et redimensionner l'image de la flamme
flame_img = pygame.image.load("resources/iconkit/robots/flammet.png").convert_alpha()
flame_small = pygame.transform.scale(flame_img, (int(flame_img.get_width() * 0.06), int(flame_img.get_height() * 0.06)))

# Inverser la flamme verticalement
flame_small_inverted = pygame.transform.flip(flame_small, False, True)

# Taille des images
head_height = head_img.get_height()
legs_height = legs_img.get_height()
feet_height = feet_img.get_height()
robot_total_height = head_height + legs_height + feet_height  # Hauteur totale du robot
flame_height = flame_small.get_height()
flame_width = flame_small.get_width()

# Position initiale
robot_x = 300
robot_y = 300  # Position du sol (base des pieds)
robot_jump = False
jump_velocity = -15
gravity = 1
vertical_velocity = 0
max_jump_height = 300 - (20 * robot_total_height)  # Hauteur maximale du saut (3 fois la taille du robot au-dessus de lui)
can_jump = True  # Indique si le robot peut sauter

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

def draw_flame(base_x, base_y):
    """Dessine une flamme inversée sous les pieds du robot."""
    flame_x = base_x + feet_img.get_width() // 2 - flame_width // 2
    flame_y = base_y
    screen.blit(flame_small_inverted, (flame_x, flame_y))

# Boucle principale
running = True
space_pressed = False  # Indique si la touche espace est maintenue
while running:
    screen.fill((30, 30, 30))  # Fond

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            space_pressed = True
            if can_jump:  # Le saut est possible uniquement si can_jump est True
                robot_jump = True
                vertical_velocity = jump_velocity  # Définir la vitesse initiale du saut
                can_jump = False  # Empêcher un autre saut tant que le robot n'est pas au sol
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            space_pressed = False

    # Gestion du saut
    if robot_jump:
        # Le robot monte ou descend selon la vitesse verticale
        robot_y += vertical_velocity
        vertical_velocity += gravity

        # Si le robot atteint la hauteur maximale, stopper la montée
        if robot_y <= max_jump_height:
            robot_y = max_jump_height
            vertical_velocity = gravity  # Commencer immédiatement à redescendre

        # Si le robot touche le sol, arrêter le saut
        if robot_y >= 300:
            robot_y = 300
            robot_jump = False
            vertical_velocity = 0
            can_jump = True  # Autoriser à sauter à nouveau

    # Dessiner la flamme si le robot saute
    if robot_jump:
        draw_flame(robot_x, robot_y)

    # Dessiner le robot
    draw_robot(robot_x, robot_y, 0)

    # Mettre à jour l'écran
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
