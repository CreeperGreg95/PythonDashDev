# player.py Version 2

import pygame

class Player:
    def __init__(self, icon):
        self.icon = icon
        self.size = 50
        self.x = 100
        self.y = 400 - self.size
        self.velocity_y = 0
        self.jump_strength = 15
        self.gravity = 0.8
        self.is_jumping = False
        self.rotation_angle = 0

        # Crée un masque initial en utilisant l'icône d'origine
        self.mask = pygame.mask.from_surface(self.icon)
        self.mask_offset = (self.x, self.y)

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.velocity_y = -self.jump_strength

    def apply_gravity(self):
        if self.is_jumping:
            self.y += self.velocity_y
            self.velocity_y += self.gravity
            self.rotation_angle -= 5
            if self.y >= 400 - self.size:
                self.y = 400 - self.size
                self.is_jumping = False
                self.rotation_angle = 0

    def draw(self, screen):
        # Fait tourner l'icône et crée un rectangle englobant centré
        rotated_icon = pygame.transform.rotate(self.icon, self.rotation_angle)
        icon_rect = rotated_icon.get_rect(center=(self.x + self.size // 2, self.y + self.size // 2))
        screen.blit(rotated_icon, icon_rect.topleft)

        # Met à jour le masque pour la nouvelle orientation de l'icône
        self.mask = pygame.mask.from_surface(rotated_icon)
        self.mask_offset = (self.x, self.y)

    def get_rect(self):
        """
        Retourne un rectangle englobant basé sur la position et la taille du joueur.
        """
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def get_position(self):
        return self.x, self.y
