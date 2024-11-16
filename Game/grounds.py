# grounds.py version 2

import pygame

class Ground:
    def __init__(self, screen_width, screen_height, ground_height, texture_count=50000):
        # Charger l'image du sol
        self.image = pygame.image.load("resources/ground01.png")
        
        # Redimensionner l'image du sol pour la rendre plus petite
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 2, self.image.get_height() // 2))
        
        self.y = screen_height - ground_height  # Position du sol, juste au-dessus du bas de l'écran
        self.screen_width = screen_width  # Largeur de l'écran
        self.ground_width = self.image.get_width()
        self.ground_height = self.image.get_height()

        # Créer une liste pour stocker toutes les textures du sol
        self.textures = []
        self.x_positions = []
        
        # Initialisation des positions des textures
        for i in range(texture_count):
            self.textures.append(self.image)  # Ajouter l'image redimensionnée à la liste
            self.x_positions.append(i * self.ground_width)  # Position initiale pour chaque texture (alignée)

    def move(self, speed):
        """Déplace le sol pour créer l'effet de mouvement infini."""
        for i in range(len(self.x_positions)):
            self.x_positions[i] -= speed  # Déplacer la texture vers la gauche

            # Si une texture sort complètement de l'écran, la replacer à la fin
            if self.x_positions[i] <= -self.ground_width:
                # Remet la texture à la fin de la liste, en l'éloignant à la fin de l'écran
                # La nouvelle position est la dernière position + la largeur du sol
                self.x_positions[i] = self.x_positions[-1] + self.ground_width

    def draw(self, screen):
        """Dessine les textures du sol à leur position actuelle."""
        for x in self.x_positions:
            # Dessiner chaque texture à sa position actuelle
            screen.blit(self.image, (x, self.y))
