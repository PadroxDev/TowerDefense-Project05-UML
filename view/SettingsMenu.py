import pygame
from controllers.Button import Button
from pygame.locals import *
from models.constants import DARK_BACKGROUND
from view.Page import Page

class SettingsMenu ( Page ) :
    def __init__(self, window ):
        Page.__init__(self, window)
        self.mainTitle = pygame.image.load("res/sprites/settings_title.png").convert_alpha()
        self.maintTitleRect = Rect(350, 50, 600, 200)
        self.mainTitle = pygame.transform.scale(self.mainTitle, (self.maintTitleRect.w, self.maintTitleRect.h))

        self.listeButton.append(Button("res/sprites/button/back.png", pygame.Rect(20, 20, 50, 50)))
        self.listeButton[0].bind(self.Stop)

        self.background = DARK_BACKGROUND

    