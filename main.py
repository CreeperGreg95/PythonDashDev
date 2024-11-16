import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from game_start_player import Player
from grounds import Ground
from obstacles import Obstacles

pygame.init()

# Initialisation de l'écran
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python Dash")
clock = pygame.time.Clock()

# Chargement des éléments du jeu
player = Player()
ground = Ground()
obstacles = Obstacles()

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Mise à jour
        player.update()
        obstacles.update()
        
        # Dessin
        screen.fill((135, 206, 235))  # Couleur de fond (bleu ciel)
        ground.draw(screen)
        obstacles.draw(screen)
        player.draw(screen)
        
        # Rafraîchir l'écran
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
