import pygame
# from controllers.GameManager import GameManager
from models.Window import Window

pygame.init()

if __name__ == "__main__":
    Window().globalGame()
    pygame.quit()