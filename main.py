import pygame
from controllers.GameManager import GameManager
from models.Window import Window

if __name__ == "__main__":
    Window().globalGame()
    #GameManager(window).run()
    pygame.quit()