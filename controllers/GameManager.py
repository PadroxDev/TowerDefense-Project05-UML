import pygame
from pygame.locals import *
from controllers.Button import Button
from PlayerManager import PlayerManager

class GameManager:
    def __init__(self):
        pygame.init()
        GameManager.screen = pygame.display.set_mode((1280, 720))
        GameManager.player = PlayerManager()
        GameManager.clock = pygame.time.Clock()
        GameManager.deltaTime = 0
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
        GameManager.deltaTime = GameManager.clock.tick()

        print(GameManager.deltaTime)
        Button.update()

    def render(self):
        GameManager.screen.fill(Color('lime'))



        GameManager.screen.fill(Color('gray'))
        Button.render()
        pygame.display.update()