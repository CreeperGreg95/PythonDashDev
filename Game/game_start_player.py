import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_HEIGHT

class Player:
    def __init__(self):
        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 4
        self.rect.y = SCREEN_HEIGHT - GROUND_HEIGHT - self.rect.height
        self.velocity_y = 0
        self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.velocity_y = -15  # Vitesse de saut

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.jump()

        # Appliquer la gravité
        self.velocity_y += 1
        self.rect.y += self.velocity_y

        # Empêcher de passer à travers le sol
        if self.rect.bottom >= SCREEN_HEIGHT - GROUND_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT - GROUND_HEIGHT
            self.is_jumping = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
