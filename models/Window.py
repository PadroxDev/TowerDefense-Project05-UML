import pygame
from controllers.GameManager import GameManager 
from view.MainMenu import MainMenu
from view.SettingsMenu import SettingsMenu
from view.Credits import Credits

class Window () :
    def __init__(self):
        self.window = pygame.display.set_mode((1280, 720))
        self.game = GameManager(self.window)
        self.mainMenu = MainMenu(self.window)
        self.Settings = SettingsMenu(self.window)
        self.Credits = Credits(self.window)

        self.mainMenu.BindButton(0,self.game.run)
        self.mainMenu.BindButton(1,self.Settings.run)
        self.mainMenu.BindButton(2,self.Credits.run)
        self.mainMenu.BindButton(3,self.quit)

    def globalGame(self):
        is_running = True
        while (is_running):
            self.mainMenu.run()
            is_running = False

    def quit(self):
        pygame.quit()