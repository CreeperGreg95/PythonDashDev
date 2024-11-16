import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_HEIGHT

class Ground:
    def __init__(self):
        self.image = pygame.image.load("assets/ground01.png")
        self.rect = self.image.get_rect()
        self.rect.y = SCREEN_HEIGHT - GROUND_HEIGHT

    def draw(self, screen):
        for x in range(0, SCREEN_WIDTH, self.rect.width):
            screen.blit(self.image, (x, self.rect.y))
