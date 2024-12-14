import pygame

class Hitbox:
    def __init__(self, x, y, width, height, color=(255, 0, 0), shape="rectangle"):
        """Initialise une hitbox (rectangle ou triangle)."""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.shape = shape  # "rectangle" ou "triangle"
        if self.shape == "triangle":
            self.points = self.calculate_points()

    def calculate_points(self):
        """Calcule les trois sommets d'un triangle."""
        top = (self.x + self.width // 2, self.y)  # Sommet supérieur
        bottom_left = (self.x, self.y + self.height)  # Coin inférieur gauche
        bottom_right = (self.x + self.width, self.y + self.height)  # Coin inférieur droit
        return [top, bottom_left, bottom_right]

    def update(self, x, y, width=None, height=None):
        """Met à jour la position et les dimensions de la hitbox."""
        self.x = x
        self.y = y
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if self.shape == "triangle":
            self.points = self.calculate_points()

    def draw(self, screen):
        """Dessine la hitbox (triangle ou rectangle)."""
        if self.shape == "triangle":
            pygame.draw.polygon(screen, self.color, self.points, 2)
        else:  # Rectangle
            rect = pygame.Rect(self.x, self.y, self.width, self.height)
            pygame.draw.rect(screen, self.color, rect, 2)

    def get_rect(self):
        """Retourne un rectangle englobant la hitbox."""
        return pygame.Rect(self.x, self.y, self.width, self.height)