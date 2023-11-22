import pygame
from pygame import Rect
from pygame.mouse import get_pos as mouse_pos
from pygame.mouse import get_pressed as mouse_buttons

class Button:
    def __init__(self, imgPath, dest:Rect=Rect(0, 0, 100, 100))->None:
        self.displaySurf = pygame.display.get_surface()
        self.sprite = pygame.image.load(imgPath).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (dest.w,dest.h))
        self.dest = dest
        self.onClick = None
        self.previously_clicked = False
        self.rect = dest

    def bind(self, to)->None:
        self.onClick = to

    def update(self)->None:
        if self.rect.collidepoint(mouse_pos()) and mouse_buttons()[0]:
            if self.onClick and not self.previously_clicked:
                self.previously_clicked = True
                self.onClick()
                
        else:
            self.previously_clicked = False

    def render(self)->None:
        if not self.displaySurf:
            print("No surface found on button initialization!")
            return

        self.rect = self.displaySurf.blit(self.sprite, self.dest)

    def resize(self,h,w)->None:
        self.sprite = pygame.transform.scale(self.sprite, (w,h))
