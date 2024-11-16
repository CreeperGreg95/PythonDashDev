# grounds.py Version 1

import pygame

class Ground:
    def __init__(self, width, height, ground_height):
        self.width = width
        self.height = height
        self.ground_height = ground_height
        self.image = pygame.image.load("resources/ground01.png")  # Assure-toi d'avoir une image pour le sol
        self.image = pygame.transform.scale(self.image, (self.width, self.ground_height))  # Redimensionner l'image du sol
        self.y = self.height - self.ground_height  # Positionner le sol au bas de l'écran

    def draw(self, screen):
        screen.blit(self.image, (0, self.y))  # Dessiner le sol sur l'écran


    def get_rect(self):
        """Retourne un rectangle englobant le sol."""
        return pygame.Rect(0, self.y, self.image.get_width(), self.image.get_height())
