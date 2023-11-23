import pygame
from controllers.Button import Button
from pygame.locals import *
from models.constants import BACKGROUND_COLOR, BLACK
from view.Page import Page
from models.Text import Text

class LooseScreen ( Page ) :
    def __init__(self, window ):
        Page.__init__(self, window)

        
        self.listeButton.append(Button("res/sprites/button/button_leave.png", pygame.Rect(500, 550, 200, 100)))
        self.listeButton[0].bind(self.Stop)

        self.listeText.append(Text("Perdu",pygame.Rect(450, 100, 300, 200),80, BLACK))

        self.background = BACKGROUND_COLOR

    def Stop(self):
        pygame.quit()