# player.py version 3

import pygame
from speed import JUMP_HORIZONTAL_SPEED

class Player:
    def __init__(self, icon, ground_height):
        self.icon = icon
        self.size = 50
        self.x = 100
        self.y = 400 - self.size - ground_height  # Décale la position du joueur par rapport au sol
        self.velocity_y = 0
        self.jump_strength = 15
        self.gravity = 0.8
        self.is_jumping = False
        self.rotation_angle = 0
        self.ground_height = ground_height  # Ajouter cette ligne pour stocker le ground_height

        # Crée un masque initial en utilisant l'icône d'origine
        self.mask = pygame.mask.from_surface(self.icon)
        self.mask_offset = (self.x, self.y)

    def jump(self, direction):
        if not self.is_jumping:
            self.is_jumping = True
            self.velocity_y = -self.jump_strength
            self.velocity_x = JUMP_HORIZONTAL_SPEED * direction
            print(f"Jump initiated. Direction: {direction}, Velocity X: {self.velocity_x}, Velocity Y: {self.velocity_y}")

    def apply_gravity(self):
        if self.is_jumping:
            self.y += self.velocity_y
            self.velocity_y += self.gravity
            self.rotation_angle -= 5
            if self.y >= 400 - self.size - self.ground_height:  # Utiliser self.ground_height ici
                self.y = 400 - self.size - self.ground_height
                self.is_jumping = False
                self.rotation_angle = 0

    def draw(self, screen):
        rotated_icon = pygame.transform.rotate(self.icon, self.rotation_angle)
        icon_rect = rotated_icon.get_rect(center=(self.x + self.size // 2, self.y + self.size // 2))
        screen.blit(rotated_icon, icon_rect.topleft)

        self.mask = pygame.mask.from_surface(rotated_icon)
        self.mask_offset = (self.x, self.y)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def get_position(self):
        return self.x, self.y
