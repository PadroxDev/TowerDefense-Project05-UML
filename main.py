import pygame
from pygame.locals import *

class GameManager:
    def __init__(self):
        pygame.init()
        GameManager.screen = pygame.display.set_mode((1280, 720))
        GameManager.player = Player()
        GameManager.clock = Clock()
        GameManager.running = True

    def run(self):
        while GameManager.running:
            self.handleEvents()
            self.update()
            self.render()
        pygame.quit()

    def handleEvents(self):
        for event in pygame.event.get():
            if(event.type == QUIT):
                GameManager.running = False

    def update(self):
        pass

    def render(self):
        GameManager.screen.fill(Color('gray'))



        pygame.display.update()


if __name__ == "__main__":
    GameManager().run()