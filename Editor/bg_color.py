import pygame

def apply_color_overlay(surface, color, opacity):
    """Applique une superposition de couleur transparente uniforme sur une image."""
    # Créer une surface transparente de la même taille que l'image
    overlay = pygame.Surface(surface.get_size(), pygame.SRCALPHA)

    # Remplir la surface avec la couleur et l'opacité
    overlay.fill((*color, opacity))

    # Superposer la surface sur l'image originale en utilisant le mélange alpha
    filtered_surface = surface.copy()
    filtered_surface.blit(overlay, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    return filtered_surface
