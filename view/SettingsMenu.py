import pygame
from controllers.Button import Button
from pygame.locals import *
from models.constants import DARK_BACKGROUND, BLACK
from view.Page import Page
from models.Text import Text

class SettingsMenu ( Page ) :
    def __init__(self, window ):
        Page.__init__(self, window)

        self.listeText.append(Text("Settings",pygame.Rect(450, 100, 300, 200),80, BLACK))

        self.listeButton.append(Button("res/sprites/button/back.png", pygame.Rect(20, 20, 50, 50)))
        self.listeButton[0].bind(self.Stop)

        self.background = DARK_BACKGROUND

    