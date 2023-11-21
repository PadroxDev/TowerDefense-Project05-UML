import pygame
from pygame.locals import *
from controllers.PlayerManager import PlayerManager
from models.constants import *

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
        GameManager.deltaTime = GameManager.clock.tick(200) / 1000

    def render(self):
        GameManager.screen.fill(BACKGROUND_COLOR)

        pygame.display.update()