import pygame
from pygame.locals import *
from controllers.Button import Button
from controllers.PlayerManager import PlayerManager
from models.constants import *

class GameManager:
    def __init__(self, screen):
        pygame.init()
        GameManager.screen = screen
        GameManager.player = PlayerManager()
        GameManager.clock = pygame.time.Clock()
        GameManager.deltaTime = 0
        GameManager.running = True

        self.backButton = Button("res/sprites/button/back.png", Rect(20, 20, 50, 50))
        self.backButton.bind(self.stop)

    def run(self):
        GameManager.running = True
        while GameManager.running:
            self.handleEvents()
            self.update()
            self.render()

    def handleEvents(self):
        for event in pygame.event.get():
            if(event.type == QUIT):
                GameManager.running = False

    def update(self):
        GameManager.deltaTime = GameManager.clock.tick(200) / 1000
        self.backButton.update()

    def render(self):
        GameManager.screen.fill(BACKGROUND_COLOR)

        self.backButton.render()
        self.backButton.update()

        pygame.display.update()

    def stop(self):
        GameManager.running = False