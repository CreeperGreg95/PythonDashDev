class SpeedEffect:
    def apply_speed_effect(self, player, speed_type):
        """Applique l'effet du speed au joueur et ajuste la difficulté des obstacles."""
        if speed_type == "boost0.5":
            print("Le speed x0.5 a apparu.")
            player.speed *= 0.5  # Diminution de la vitesse
        elif speed_type == "boost4":
            print("Le speed x4 a apparu.")
            player.speed *= 4.0  # Augmentation modérée de la vitesse
        elif speed_type == "speed1":
            print("Le speed x1 a apparu.")
            player.speed *= 1.0  # Petit boost de la vitesse
        elif speed_type == "speed2":
            print("Le speed x2 a apparu.")
            player.speed *= 2.0  # Boost moyen de la vitesse
        elif speed_type == "speed3":
            print("Le speed x3 a apparu.")
            player.speed *= 3.0  # Grand boost de la vitesse

        return player.speed
