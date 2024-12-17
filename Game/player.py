import pygame
from hitbox import Hitbox
from death import DeathManager

class Player:
    def __init__(self, icon, ground_height, screen_height):
        self.icon = pygame.transform.scale(icon, (50, 50))
        self.size = 50
        self.x = 100
        self.ground_height = ground_height
        self.screen_height = screen_height
        self.y = screen_height - ground_height - self.size

        self.velocity_y = 0
        self.jump_strength = 13.87
        self.gravity = 0.8
        self.is_jumping = False
        self.rotation_angle = 0

        # Ajout de la gestion de la vitesse
        self.default_speed = 1.0
        self.speed = self.default_speed  # Vitesse actuelle

        # Hitboxes
        self.outer_hitbox = Hitbox(self.x, self.y, self.size, self.size, color=(0, 0, 255), shape="rectangle")
        self.inner_hitbox = Hitbox(self.x + 10, self.y + 10, self.size - 20, self.size - 20, color=(255, 255, 0), shape="rectangle")

    def apply_gravity(self):
        if self.is_jumping:
            self.y += self.velocity_y
            self.velocity_y += self.gravity
            self.rotation_angle -= 5
            if self.y >= self.screen_height - self.ground_height - self.size:
                self.y = self.screen_height - self.ground_height - self.size
                self.is_jumping = False
                self.rotation_angle = 0

        self.outer_hitbox.update(self.x, self.y)
        self.inner_hitbox.update(self.x + 10, self.y + 10)

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.velocity_y = -self.jump_strength

    def draw(self, screen, show_hitboxes):
        rotated_icon = pygame.transform.rotate(self.icon, self.rotation_angle)
        icon_rect = rotated_icon.get_rect(center=(self.x + self.size // 2, self.y + self.size // 2))
        screen.blit(rotated_icon, icon_rect.topleft)

        if show_hitboxes:
            self.outer_hitbox.draw(screen)
            self.inner_hitbox.draw(screen)

    def get_rect(self):
        return self.outer_hitbox.get_rect()

    def check_collision(self, obstacle_hitbox):
        return DeathManager.check_collision(self.outer_hitbox, [obstacle_hitbox])

    def reset_speed(self):
        """Réinitialise la vitesse à sa valeur par défaut."""
        self.speed = self.default_speed
