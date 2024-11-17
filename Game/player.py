# player.py version 4

import pygame

class Player:
    def __init__(self, icon, ground_height, screen_height=None):
        self.icon = icon
        self.size = 50  # Taille fixe de la hitbox (50x50)
        self.x = 100
        self.ground_height = ground_height

        # Ajuste la taille de l'icône pour qu'elle soit toujours 50x50
        self.icon = pygame.transform.scale(self.icon, (self.size, self.size))  # Redimensionner l'icône à 50x50

        # Calcul de la position y du joueur
        self.screen_height = screen_height
        self.y = self.screen_height - self.ground_height - self.icon.get_height()

        self.velocity_y = 0
        self.jump_strength = 15
        self.gravity = 0.8
        self.is_jumping = False
        self.rotation_angle = 0

    def apply_gravity(self):
        if self.is_jumping:
            self.y += self.velocity_y
            self.velocity_y += self.gravity
            self.rotation_angle -= 5
            if self.y >= self.screen_height - self.ground_height - self.icon.get_height():
                self.y = self.screen_height - self.ground_height - self.icon.get_height()
                self.is_jumping = False
                self.rotation_angle = 0

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.velocity_y = -self.jump_strength

    def adjust_size(self, new_screen_height):
        """Ajuste la taille de l'icône à 50x50, mais garde la hitbox fixe."""
        self.icon = pygame.transform.scale(self.icon, (self.size, self.size))  # Taille fixe à 50x50
        self.y = new_screen_height - self.ground_height - self.icon.get_height()

    def draw(self, screen):
        rotated_icon = pygame.transform.rotate(self.icon, self.rotation_angle)
        # La hitbox reste 50x50, l'icône est centrée dans cette hitbox
        icon_rect = rotated_icon.get_rect(center=(self.x + self.size // 2, self.y + self.size // 2))
        screen.blit(rotated_icon, icon_rect.topleft)

    def get_rect(self):
        # Retourner la hitbox fixe (50x50)
        return pygame.Rect(self.x, self.y, self.size, self.size)