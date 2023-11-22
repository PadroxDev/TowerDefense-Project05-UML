import pygame
from pygame.locals import *
from models.constants import BACKGROUND_COLOR

class Page () :
    def __init__(self, window ):

        self.listeButton = []
        self.listeText = []
        self.screen = window
        self.running = True

        self.background = BACKGROUND_COLOR

    def run(self): 
        self.running = True
        while(self.running):
            
            self.Update()
            self.Render()
            
            self.handleEvents()
            
    def handleEvents(self):
        for event in pygame.event.get():
            if(event.type == QUIT):
                self.running = False
                pygame.quit()

    def BindButton(self, index:int, function):
        self.listeButton[index].bind(function)

    def Update(self):
        for button in self.listeButton :
            button.update()

    def Render(self):
        self.screen.fill(self.background)
        for button in self.listeButton :
            button.render()

        for text in self.listeText :
            text.render(self.screen)

        pygame.display.update()

    def Stop(self):
        self.running = False