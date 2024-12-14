class GameOptions:
    def __init__(self):
        self.obstacle_speed = 5
        self.show_hitboxes = False

        self.screen_width = 1200
        self.screen_height = 650
        self.aspect_ratio = self.screen_width / self.screen_height

        self.fps_limit = 60
        self.background_speed_factor = 0.1

    def update_window_size(self, width, height):
        new_aspect_ratio = width / height
        if new_aspect_ratio > self.aspect_ratio:
            self.screen_width = int(height * self.aspect_ratio)
            self.screen_height = height
        else:
            self.screen_width = width
            self.screen_height = int(width / self.aspect_ratio)

    def increase_difficulty(self):
        self.obstacle_speed += 0.5

    def toggle_hitboxes(self):
        """Active ou désactive l'affichage des hitboxes."""
        self.show_hitboxes = not self.show_hitboxes
        print(f"Affichage des hitboxes : {'activé' if self.show_hitboxes else 'désactivé'}")

    def set_fps_limit(self, fps):
        self.fps_limit = fps

    def set_window_size(self, width, height):
        self.screen_width = width
        self.screen_height = height

    def set_background_speed_factor(self, factor):
        self.background_speed_factor = factor
