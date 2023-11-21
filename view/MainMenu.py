import pygame
from controllers.Button import Button
from pygame.locals import *
from models.constants import BACKGROUND_COLOR

class MainMenu () :
    def __init__(self, imgPath : str, window ):

        self.mainTitle = pygame.image.load(imgPath).convert_alpha()
        self.maintTitleRect = self.mainTitle.get_rect()
        self.listeButton = []
        self.screen = window
        self.running = True

        self.listeButton.append(Button("res/sprites/button/button_play.png", pygame.Rect(400, 250, 200, 100)))
        self.listeButton.append(Button("res/sprites/button/button_sprite.png", pygame.Rect(400, 350, 200, 100)))
        self.listeButton.append(Button("res/sprites/button/button_sprite.png", pygame.Rect(400, 450, 200, 100)))
        self.listeButton.append(Button("res/sprites/button/button_sprite.png", pygame.Rect(400, 550, 200, 100)))

    def DrawMenu(self): 

        while(self.running):
            self.screen.fill(BACKGROUND_COLOR)
            self.mainTitle.blit(self.screen, self.maintTitleRect)
            for button in self.listeButton :
                button.render()
                button.update()

            self.handleEvents()
            pygame.display.update()
        

    def handleEvents(self):
        for event in pygame.event.get():
            if(event.type == QUIT):
                self.running = False

    def BindButton(self, index:int, function):
        self.listeButton[index].bind(function)
