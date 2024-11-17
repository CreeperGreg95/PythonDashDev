# obstacles.py - version clean

import pygame
import random
from hitbox import Hitbox

class Obstacle:
    def __init__(self, screen_width, screen_height, speed, ground_height):
        # Sauvegarde des dimensions de l'écran
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Chargement de l'obstacle et de sa taille
        self.image = pygame.image.load("resources/editor/obstacles/spike01.png") # Choix aléatoire de l'image
        self.image = pygame.transform.scale(self.image, (45, 45))  # Taille fixe des obstacles
        
        # Position de l'obstacle, au bord droit de l'écran
        self.x = self.screen_width  # Position initiale à l'extrême droite
        self.y = self.screen_height - self.image.get_height() - ground_height  # Position au-dessus du sol
        
        # Vitesse du déplacement
        self.speed = speed

        # Création de la hitbox
        self.hitbox = Hitbox(self.x, self.y, self.image.get_width(), self.image.get_height())

    def move(self):
        """Déplace l'obstacle vers la gauche."""
        self.x -= self.speed
        self.hitbox.update(self.x, self.y, self.image.get_width(), self.image.get_height())  # Mise à jour de la hitbox

    def draw(self, screen, show_hitboxes):
        """Dessine l'obstacle sur l'écran."""
        screen.blit(self.image, (self.x, self.y))
        if show_hitboxes:
            self.hitbox.draw(screen)

    def get_rect(self):
        """Retourne un rectangle englobant l'obstacle."""
        return self.hitbox.get_rect()

    def is_off_screen(self):
        """Vérifie si l'obstacle est hors de l'écran."""
        return self.x < -self.image.get_width()  # L'obstacle est hors de l'écran si sa position x est inférieure à -sa largeur

