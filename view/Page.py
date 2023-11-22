import pygame
from controllers.Button import Button
from pygame.locals import *
from models.constants import BACKGROUND_COLOR

class Page () :
    def __init__(self, window ):

        self.listeButton = []
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

    def BindButton(self, index:int, function):
        self.listeButton[index].bind(function)

    def Update(self):
        for button in self.listeButton :
            button.update()

    def Render(self):
        self.screen.fill(self.background)
        self.screen.blit(self.mainTitle, self.maintTitleRect)
        for button in self.listeButton :
            button.render()

        pygame.display.update()

    def Stop(self):
        self.running = False