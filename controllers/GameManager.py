import pygame
from pygame.locals import *
from pygame.math import Vector2
from controllers.Button import Button
from controllers.PlayerManager import PlayerManager
from controllers.TowerManager import TowerManager
from models.constants import *
from models.Map import Path

class GameManager:
    def __init__(self, screen):
        pygame.init()
        GameManager.screen = screen
        GameManager.player = PlayerManager()
        GameManager.clock = pygame.time.Clock()
        GameManager.deltaTime = 0
        GameManager.running = True
        GameManager.towerManager = TowerManager()

        self.buttonTest = Button("res/sprites/button/button_sprite_test.png", Rect(100, 100, 200, 200))

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
            elif(event.type == MOUSEBUTTONDOWN):
                GameManager.towerManager.CheckIfBuildable()


    def update(self):
        GameManager.deltaTime = GameManager.clock.tick(200) / 1000
        self.buttonTest.update()
        self.towerManager.update(self.deltaTime)

    def render(self):
        GameManager.screen.fill(BACKGROUND_COLOR)

        self.buttonTest.render()
        self.towerManager.render(self.screen)

        for i in range(len(Path)-1):
            p1 = Path[i]
            p2 = Path[i+1]
            pygame.draw.line(self.screen, Color(212, 123, 74), p1, p2, 16)

        pygame.display.update()