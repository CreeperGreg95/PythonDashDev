import pygame

def load_player_icon(path="resources/iconkit/cube/cube01.png"):
    icon = pygame.image.load(path)
    icon = pygame.transform.scale(icon, (50, 50))
    return icon
