import pygame

# keybinds.py

def handle_event(event, player, options):
    """
    Gère les pressions sur les touches pour contrôler le joueur et les options.
    
    :param event: L'événement KEYDOWN de Pygame.
    :param player: L'objet Player pour exécuter les actions.
    :param options: Les options de jeu pour activer/désactiver des fonctionnalités.
    """
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            # Le joueur saute verticalement
            player.jump()
            print("la touche espace a été pressée !")
        elif event.key == pygame.K_UP:
            # Le joueur saute verticalement
            player.jump()
            print("La touche flèche haute a été pressée !")
        elif event.key == pygame.K_h:
            # Basculer la visibilité des hitboxes
            options.toggle_hitboxes()

        """
        A mettre en fonctionnement quand le platformer sera developpé (pas tout de suite lol)

        elif event.key == pygame.K_LEFT:
            # Le joueur saute vers la gauche
            player.jump(-1)
        elif event.key == pygame.K_RIGHT:
            # Le joueur saute vers la droite
            player.jump(1)
        """

    elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Clic gauche
            player.jump()
            print("Le clic gauche de la souris a été pressée !")