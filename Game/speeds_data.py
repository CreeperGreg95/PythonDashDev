from hitbox import Hitbox
import pygame
import random

class Speed:
    def __init__(self, screen_width, screen_height, speed, ground_height):
        # Sauvegarde des dimensions de l'écran
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Charger un speed aléatoire parmi les 5 images
        speeds_images = [
            "resources/speeds/boost0.5.png",
            "resources/speeds/boost4.png",
            "resources/speeds/speed1.png",
            "resources/speeds/speed2.png",
            "resources/speeds/speed3.png"
        ]
        
        # Choix aléatoire de l'image
        self.image_path = random.choice(speeds_images)
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (45, int(45 * 1.25)))  # Taille augmentée de 1.25

        # Position du speed
        self.x = self.screen_width
        self.y = self.screen_height - self.image.get_height() - ground_height

        # Vitesse du déplacement
        self.speed = speed

        # Création de la hitbox (verte)
        self.hitbox = Hitbox(self.x, self.y, self.image.get_width(), self.image.get_height(), color=(0, 255, 0))

    def move(self):
        """Déplace le speed vers la gauche."""
        self.x -= self.speed
        self.hitbox.update(self.x, self.y)

    def draw(self, screen, show_hitboxes):
        """Dessine le speed sur l'écran."""
        screen.blit(self.image, (self.x, self.y))
        if show_hitboxes:
            self.hitbox.draw(screen)

    def is_off_screen(self):
        """Vérifie si le speed est hors de l'écran."""
        return self.x < -self.image.get_width()

    def apply_effect(self, player):
        """Applique l'effet du speed au joueur et retourne la nouvelle vitesse."""
        if "boost0.5" in self.image_path:
            return player.speed * 0.975
        elif "boost4" in self.image_path:
            return player.speed * 2
        elif "speed1" in self.image_path:
            return player.speed
        elif "speed2" in self.image_path:
            return player.speed * 1.231
        elif "speed3" in self.image_path:
            return player.speed * 1.60786
