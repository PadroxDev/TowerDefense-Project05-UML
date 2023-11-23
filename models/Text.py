import pygame

class Text () :

    def __init__(self, text : str, rect: pygame.Rect, size : int, color : pygame.Color):

        self.font =  pygame.font.SysFont("verdana", size)
        self.content = self.font.render(text, True, color)
        self.color = color
        self.rect = rect
    
    def render(self, window):
        window.blit(self.content, self.rect)

    def setContent(self, text):
        self.content = self.font.render(text, True, self.color)

