# options.py version 3

class GameOptions:
    def __init__(self):
        # Paramètres de base du jeu
        self.obstacle_speed = 5
        self.show_hitboxes = False

        # Paramètres de la fenêtre
        self.screen_width = 800
        self.screen_height = 400
        self.aspect_ratio = self.screen_width / self.screen_height  # Proportion de l'écran

        # Paramètres des FPS
        self.fps_limit = 60

        # Paramètres du background
        self.background_speed_factor = 0.1

    def update_window_size(self, width, height):
        """Met à jour la taille de la fenêtre tout en respectant les proportions."""
        new_aspect_ratio = width / height
        if new_aspect_ratio > self.aspect_ratio:
            # Si la fenêtre est plus large que nécessaire, ajuster la largeur
            self.screen_width = int(height * self.aspect_ratio)
            self.screen_height = height
        else:
            # Si la fenêtre est plus haute que nécessaire, ajuster la hauteur
            self.screen_width = width
            self.screen_height = int(width / self.aspect_ratio)

    # Méthode pour augmenter la difficulté (augmentation de la vitesse des obstacles)
    def increase_difficulty(self):
        self.obstacle_speed += 0.5

    # Méthode pour activer/désactiver l'affichage des hitboxes
    def toggle_hitboxes(self):
        self.show_hitboxes = not self.show_hitboxes

    # Méthode pour modifier les FPS du jeu
    def set_fps_limit(self, fps):
        """Permet de modifier la limite des FPS"""
        self.fps_limit = fps

    # Méthode pour changer la taille de la fenêtre
    def set_window_size(self, width, height):
        """Permet de modifier la taille de la fenêtre"""
        self.screen_width = width
        self.screen_height = height

    # Méthode pour changer la vitesse du background
    def set_background_speed_factor(self, factor):
        """Permet de modifier la vitesse du background"""
        self.background_speed_factor = factor

