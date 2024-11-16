import pygame

class Obstacle:
    def __init__(self, x, speed):
        self.image = pygame.image.load("resources/spike01.png")
        self.image = pygame.transform.scale(self.image, (45, 45))  # Redimensionne à 45x45 pixels
        self.x = x
        self.y = 400 - self.image.get_height()  # Place l'obstacle au niveau du sol
        self.speed = speed

        # Crée un masque basé sur l'image pour la détection de collision
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.x -= self.speed
        if self.x < -45:
            self.x = 800  # Réinitialise la position de l'obstacle à droite de l'écran

    def draw(self, screen, show_hitboxes):
        # Dessine l'image de l'obstacle
        screen.blit(self.image, (self.x, self.y))

        # Si show_hitboxes est activé, dessiner la hitbox
        if show_hitboxes:
            # Dessine un rectangle rouge autour de la zone de collision de l'obstacle
            pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.image.get_width(), self.image.get_height()), 2)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def get_position(self):
        return self.x, self.y