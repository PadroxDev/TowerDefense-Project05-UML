import pygame
from pygame.locals import *
from pygame.math import Vector2
from controllers.Button import Button
from controllers.PlayerManager import PlayerManager
from controllers.TowerManager import TowerManager
from controllers.EventManager import EventManager
from models.Money import Money
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
        GameManager.money = Money(450)
        GameManager.towerManager = TowerManager(self.money)
        GameManager.eventManager = EventManager(self.money)

        self.background = pygame.image.load("res/sprites/map.png")
        self.background = pygame.transform.scale(self.background, (1280, 720))

        self.backButton = Button("res/sprites/button/back.png", Rect(20, 20, 50, 50))
        self.backButton.bind(self.stop)

        self.listeButton = []
        self.listeButton.append(Button("res/sprites/button/golem_button.png", Rect(1150, 600, 80, 80)))
        self.BindButton(0,GameManager.towerManager.createGolem)
        self.listeButton.append(Button("res/sprites/button/archer_button.png", Rect(1060, 600, 80, 80)))
        self.BindButton(1,GameManager.towerManager.createArcher)
        self.listeButton.append(Button("res/sprites/button/wizard_button.png", Rect(970, 600, 80, 80)))
        self.BindButton(2,GameManager.towerManager.createWizard)

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
                pygame.quit()
            elif(event.type == MOUSEBUTTONDOWN):
                GameManager.towerManager.createTurret()


    def update(self):
        GameManager.deltaTime = GameManager.clock.tick(200) / 1000
        self.backButton.update()
        self.eventManager.update(self.deltaTime)
        self.towerManager.update(self.deltaTime, self.eventManager.enemiesAlive)
        self.money.update()

        for button in self.listeButton :
            button.update()

    def render(self):
        GameManager.screen.fill([255, 255, 255])
        GameManager.screen.blit(self.background, (0,0))

        self.backButton.render()
        self.backButton.update()
            
        self.eventManager.render(self.screen)
        self.towerManager.render(self.screen)
        self.money.render(self.screen)

        pygame.display.update()

    def stop(self):
        GameManager.running = False

    def BindButton(self, index:int, function):
        self.listeButton[index].bind(function)