import pygame
from controllers.GameManager import GameManager 
from view.MainMenu import MainMenu

class Window () :
    def __init__(self):
        self.window = pygame.display.set_mode((1280, 720))
        self.game = GameManager(self.window)
        self.mainMenu = MainMenu("res/sprites/main_title.png", self.window)
        self.mainMenu.BindButton(0,self.game.run)

    def globalGame(self):
        is_running = True
        while (is_running):
            self.mainMenu.DrawMenu()
            is_running = False