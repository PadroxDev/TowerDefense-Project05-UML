import pygame
from controllers.Button import Button
from pygame.locals import *
from models.constants import BACKGROUND_COLOR
from view.Page import Page

class MainMenu ( Page ) :
    def __init__(self, window ):
        Page.__init__(self, window)
        self.mainTitle = pygame.image.load("res/sprites/main_title.png").convert_alpha()
        self.maintTitleRect = Rect(350, 50, 600, 200)
        self.mainTitle = pygame.transform.scale(self.mainTitle, (self.maintTitleRect.w, self.maintTitleRect.h))

        self.listeButton.append(Button("res/sprites/button/button_play.png", pygame.Rect(500, 250, 200, 100)))
        self.listeButton.append(Button("res/sprites/button/button_settings.png", pygame.Rect(500, 350, 200, 100)))
        self.listeButton.append(Button("res/sprites/button/button_sprite.png", pygame.Rect(500, 450, 200, 100)))
        self.listeButton.append(Button("res/sprites/button/button_sprite.png", pygame.Rect(500, 550, 200, 100)))

        self.background = BACKGROUND_COLOR
    
    
            