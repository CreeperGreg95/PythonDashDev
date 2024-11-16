# options.py version 2

class GameOptions:
    def __init__(self):
        # Paramètres de base du jeu
        self.obstacle_speed = 5  # Vitesse des obstacles
        self.show_hitboxes = False  # Option pour afficher/désactiver les hitboxes
        
        # Paramètres de la fenêtre
        self.screen_width = 800  # Largeur de la fenêtre
        self.screen_height = 400  # Hauteur de la fenêtre
        
        # Paramètres des FPS
        self.fps_limit = 60  # Limite des FPS par défaut
        
        # Paramètres du background
        self.background_speed_factor = 0.1  # Facteur de vitesse du background par rapport à la vitesse des obstacles

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

