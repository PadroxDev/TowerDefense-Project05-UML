import pygame
from controllers.GameManager import GameManager 
from view.MainMenu import MainMenu
from view.SettingsMenu import SettingsMenu

class Window () :
    def __init__(self):
        self.window = pygame.display.set_mode((1280, 720))
        self.game = GameManager(self.window)
        self.mainMenu = MainMenu(self.window)
        self.Settings = SettingsMenu(self.window)

        self.mainMenu.BindButton(0,self.game.run)
        self.mainMenu.BindButton(1,self.Settings.run)

    def globalGame(self):
        is_running = True
        while (is_running):
            self.mainMenu.run()
            is_running = False