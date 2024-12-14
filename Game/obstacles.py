import pygame
from hitbox import Hitbox

class Obstacle:
    def __init__(self, screen_width, screen_height, speed, ground_height):
        self.width = 50
        self.height = 50
        self.x = screen_width
        self.y = screen_height - ground_height - self.height
        self.speed = speed

        # Texture de l'obstacle
        self.image = pygame.image.load("Resources/editor/obstacles/spike01.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        # Hitbox triangulaire
        self.hitbox = Hitbox(self.x, self.y, self.width, self.height, color=(255, 0, 0), shape="triangle")

    def move(self):
        self.x -= self.speed
        self.hitbox.update(self.x, self.y)

    def draw(self, screen, show_hitboxes):
        screen.blit(self.image, (self.x, self.y))
        if show_hitboxes:
            self.hitbox.draw(screen)

    def is_off_screen(self):
        return self.x + self.width < 0

    def get_rect(self):
        return self.hitbox.get_rect()