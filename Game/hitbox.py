import pygame

class Hitbox:
    def __init__(self, x, y, width, height):
        # Initialise la hitbox triangulaire
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (255, 0, 0)  # Couleur de la hitbox (rouge)
        
    def update(self, x, y, width, height):
        # Mise à jour de la position et de la taille de la hitbox
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def draw(self, screen):
        # Dessiner la hitbox triangulaire (rouge)
        # Triangle: Points de base
        points = [
            (self.x, self.y + self.height),  # Bas gauche (coin bas)
            (self.x + self.width // 2, self.y),  # Sommet du triangle
            (self.x + self.width, self.y + self.height)  # Bas droit
        ]
        pygame.draw.polygon(screen, self.color, points, 2)  # Dessiner le triangle en rouge
