# obstacles.py

import pygame
from hitbox import Hitbox

class Obstacle:
    def __init__(self, x, speed):
        self.image = pygame.image.load("resources/spike01.png")
        self.image = pygame.transform.scale(self.image, (45, 45))  # Redimensionne à 45x45 pixels
        self.x = x
        self.y = 400 - self.image.get_height()  # Place l'obstacle au niveau du sol
        self.speed = speed

        # Crée une hitbox triangulaire pour l'obstacle
        self.hitbox = Hitbox(self.x, self.y, self.image.get_width(), self.image.get_height())

    def move(self):
        self.x -= self.speed
        self.hitbox.update(self.x, self.y, self.image.get_width(), self.image.get_height())  # Met à jour la position de la hitbox
        if self.x < -45:
            self.x = 800  # Réinitialise la position de l'obstacle à droite de l'écran
            self.hitbox.update(self.x, self.y, self.image.get_width(), self.image.get_height())  # Réinitialise aussi la hitbox

    def draw(self, screen, show_hitboxes):
        # Dessine l'image de l'obstacle
        screen.blit(self.image, (self.x, self.y))

        # Si show_hitboxes est activé, dessiner la hitbox triangulaire
        if show_hitboxes:
            self.hitbox.draw(screen)  # Dessine la hitbox triangulaire

    def get_rect(self):
        """Retourne un rectangle englobant l'obstacle."""
        return self.hitbox.get_rect()

    def get_position(self):
        return self.x, self.y
