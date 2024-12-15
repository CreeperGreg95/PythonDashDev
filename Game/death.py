import pygame

class DeathManager:
    @staticmethod
    def check_collision(player_hitbox, obstacle_hitboxes):
        """
        Vérifie si le joueur entre en collision avec un obstacle.
        """
        for obstacle_hitbox in obstacle_hitboxes:
            if DeathManager._check_hitbox_collision(player_hitbox, obstacle_hitbox):
                return True
        return False

    @staticmethod
    def _check_hitbox_collision(hitbox1, hitbox2):
        """
        Vérifie les collisions entre deux hitboxes en fonction de leur forme.
        """
        if hitbox1.shape == "rectangle" and hitbox2.shape == "rectangle":
            return hitbox1.get_rect().colliderect(hitbox2.get_rect())
        elif hitbox1.shape == "triangle" or hitbox2.shape == "triangle":
            return DeathManager._triangle_collision(hitbox1, hitbox2)
        return False

    @staticmethod
    def _triangle_collision(hitbox1, hitbox2):
        """
        Vérifie les collisions entre deux triangles ou un triangle et un rectangle.
        """
        if hitbox1.shape == "triangle":
            points1 = hitbox1.points
        else:  # hitbox1 est un rectangle
            points1 = DeathManager._rect_to_points(hitbox1)

        if hitbox2.shape == "triangle":
            points2 = hitbox2.points
        else:  # hitbox2 est un rectangle
            points2 = DeathManager._rect_to_points(hitbox2)

        return DeathManager._polygons_collide(points1, points2)

    @staticmethod
    def _rect_to_points(hitbox):
        """
        Convertit une hitbox rectangulaire en une liste de points pour ses quatre coins.
        """
        rect = hitbox.get_rect()
        return [
            (rect.x, rect.y),  # Haut gauche
            (rect.x + rect.width, rect.y),  # Haut droit
            (rect.x, rect.y + rect.height),  # Bas gauche
            (rect.x + rect.width, rect.y + rect.height)  # Bas droit
        ]

    @staticmethod
    def _polygons_collide(points1, points2):
        """
        Vérifie si deux polygones définis par des listes de points se chevauchent.
        Utilise la méthode de séparation des axes (Separating Axis Theorem).
        """
        def project_polygon(axis, points):
            projections = [axis[0] * p[0] + axis[1] * p[1] for p in points]
            return min(projections), max(projections)

        def overlap(min1, max1, min2, max2):
            return max1 >= min2 and max2 >= min1

        edges = []
        for i in range(len(points1)):
            p1 = points1[i]
            p2 = points1[(i + 1) % len(points1)]
            edges.append((p2[1] - p1[1], p1[0] - p2[0]))  # Normale au bord

        for i in range(len(points2)):
            p1 = points2[i]
            p2 = points2[(i + 1) % len(points2)]
            edges.append((p2[1] - p1[1], p1[0] - p2[0]))  # Normale au bord

        for axis in edges:
            min1, max1 = project_polygon(axis, points1)
            min2, max2 = project_polygon(axis, points2)
            if not overlap(min1, max1, min2, max2):
                return False

        return True

    @staticmethod
    def handle_death():
        """
        Logique à exécuter lorsqu'une collision fatale est détectée.
        """
        print("Game Over!")