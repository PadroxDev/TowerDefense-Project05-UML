
import pygame
from controllers.Button import Button
from pygame.locals import *
from models.constants import BACKGROUND_COLOR, BLACK
from view.Page import Page
from models.Text import Text


class Credits ( Page ) :
    def __init__(self, window ):
        Page.__init__(self, window)

        self.listeButton.append(Button("res/sprites/button/back.png", pygame.Rect(20, 20, 50, 50)))
        self.listeButton[0].bind(self.Stop)

        self.listeText.append(Text("Credits",pygame.Rect(450, 100, 300, 200),80, BLACK))
        self.listeText.append(Text("Developpers: ",pygame.Rect(450, 200, 300, 200),45, BLACK))
        self.listeText.append(Text("Bailleul Wiliam",pygame.Rect(470, 260, 300, 200),30, BLACK))
        self.listeText.append(Text("Boisseau Romain",pygame.Rect(470, 300, 300, 200),30, BLACK))
        self.listeText.append(Text("Vollet Antoine",pygame.Rect(470, 340, 300, 200),30, BLACK))
        self.listeText.append(Text("Arhancet Benjamin",pygame.Rect(470, 380, 300, 200),30, BLACK))

        self.background = BACKGROUND_COLOR
    