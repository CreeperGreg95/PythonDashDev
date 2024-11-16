class GameOptions:
    def __init__(self):
        self.obstacle_speed = 5
        self.show_hitboxes = False  # Nouvelle option pour afficher/désactiver les hitboxes

    def increase_difficulty(self):
        self.obstacle_speed += 0.5

    def toggle_hitboxes(self):
        """Permet d'activer/désactiver l'affichage des hitboxes"""
        self.show_hitboxes = not self.show_hitboxes