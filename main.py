# Programme principal
import multiprocessing
from multiprocessing import freeze_support
from heure import update_time
import pygame  # Importer pygame
pygame.init()

win = pygame.display.set_mode((800, 600))  # Créer une fenêtre
pygame.display.set_caption("game-day-night")


running = True


if __name__ == "__main__":
    freeze_support()
    queue = multiprocessing.Queue()

    process = multiprocessing.Process(target=update_time, args=(queue,))
    process.start()
    process.join()

    while running:
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                running = False

        heure = queue.get()  # Obtenir l'heure actuelle en jeu

        if heure == 0:
            win.fill((0, 0, 0))

        elif heure == 6:
            win.fill((153, 153, 0))

        elif heure == 12:
            win.fill((255, 255, 51))

        # win.fill((0, 0, 0))
        pygame.display.update()
