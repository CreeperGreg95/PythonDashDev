#backgrounds.py version 3

import pygame

class Background:
    def __init__(self, screen_width, screen_height, texture_count=5000):
        # Charger l'image du fond
        self.image = pygame.image.load("resources/backgrounds/bg01.png")
        
        # Redimensionner l'image du fond pour qu'elle prenne la taille de l'écran
        self.image = pygame.transform.scale(self.image, (screen_width, screen_height))
        
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Créer une liste pour stocker les positions des différentes images de fond
        self.x_positions = []

        # Initialisation des positions des images du fond
        for i in range(texture_count):
            self.x_positions.append(i * self.screen_width)  # Position initiale pour chaque image du fond

    def move(self, speed):
        """Déplace le fond pour créer l'effet de mouvement infini."""
        for i in range(len(self.x_positions)):
            self.x_positions[i] -= speed  # Déplacer l'image du fond vers la gauche

            # Si une image sort complètement de l'écran, la replacer à la fin
            if self.x_positions[i] <= -self.screen_width:
                # Remet l'image à la fin de la liste, en l'éloignant à la fin de l'écran
                # La nouvelle position est la dernière position + la largeur de l'écran
                self.x_positions[i] = self.x_positions[-1] + self.screen_width

    def draw(self, screen):
        """Dessine les images du fond à leur position actuelle."""
        for x in self.x_positions:
            # Dessiner chaque image à sa position actuelle
            screen.blit(self.image, (x, 0))  # Position verticale fixe (0) pour que le fond soit aligné
