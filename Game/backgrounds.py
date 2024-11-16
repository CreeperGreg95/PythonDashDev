import pygame

def load_background(path="resources/bg01.png"):
    background = pygame.image.load(path)
    background = pygame.transform.scale(background, (800, 400))
    return background

def draw_background(screen, background):
    screen.blit(background, (0, 0))
