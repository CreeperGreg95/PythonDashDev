# grounds.py version 4

import pygame

class Ground:
    def __init__(self, screen_width, screen_height, ground_height, texture_count=50000):
        # Charger l'image du sol
        self.image = pygame.image.load("resources/ground01.png")
        
        # Redimensionner l'image pour qu'elle conserve sa taille d'origine sans étirement
        self.image = pygame.transform.scale(self.image, (self.image.get_width(), self.image.get_height()))
        
        self.screen_height = screen_height  # Hauteur de l'écran
        self.ground_height = ground_height  # Hauteur du sol (en dessous du joueur)
        
        self.y = self.screen_height - self.ground_height  # Position du sol, juste au bas de l'écran
        self.screen_width = screen_width
        self.ground_width = self.image.get_width()
        
        # Créer la liste de textures du sol
        self.textures = []
        self.x_positions = []
        
        # Initialisation des positions des textures
        for i in range(texture_count):
            self.textures.append(self.image)
            self.x_positions.append(i * self.ground_width)

    def move(self, speed):
        """Déplace le sol pour créer l'effet de mouvement infini."""
        for i in range(len(self.x_positions)):
            self.x_positions[i] -= speed  # Déplace la texture vers la gauche

            # Si une texture sort de l'écran, la replacer à la fin
            if self.x_positions[i] <= -self.ground_width:
                self.x_positions[i] = self.x_positions[-1] + self.ground_width

    def draw(self, screen):
        """Dessine les textures du sol à leur position actuelle."""
        for x in self.x_positions:
            screen.blit(self.image, (x, self.y))  # Dessiner le sol à la bonne position