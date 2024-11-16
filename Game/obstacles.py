import pygame
from random import randint
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_HEIGHT

class Obstacles:
    def __init__(self):
        self.image = pygame.image.load("Resources/spike01.png")
        self.obstacles = []
        self.spawn_timer = 0

    def update(self):
        # Ajouter un nouvel obstacle toutes les 100 frames
        self.spawn_timer += 1
        if self.spawn_timer > 100:
            self.spawn_timer = 0
            x = SCREEN_WIDTH
            y = SCREEN_HEIGHT - GROUND_HEIGHT - self.image.get_height()
            self.obstacles.append(pygame.Rect(x, y, self.image.get_width(), self.image.get_height()))

        # Déplacer les obstacles
        for obstacle in self.obstacles:
            obstacle.x -= 5  # Vitesse de défilement

        # Supprimer les obstacles hors de l'écran
        self.obstacles = [obstacle for obstacle in self.obstacles if obstacle.x > -self.image.get_width()]

    def draw(self, screen):
        for obstacle in self.obstacles:
            screen.blit(self.image, obstacle)
