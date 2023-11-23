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
        self.listeButton.append(Button("res/sprites/button/button_sprite_test.png", Rect(1200, 650, 40, 40)))
        self.BindButton(0,GameManager.towerManager.createGolem)
        self.listeButton.append(Button("res/sprites/button/button_sprite_test.png", Rect(1150, 650, 40, 40)))
        self.BindButton(1,GameManager.towerManager.createArcher)
        self.listeButton.append(Button("res/sprites/button/button_sprite_test.png", Rect(1100, 650, 40, 40)))
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
<<<<<<< HEAD
=======

        for i in range(len(Path)-1):
            p1 = Path[i]
            p2 = Path[i+1]
            pygame.draw.line(self.screen, Color(255, 255, 255), p1, p2, 16)

        for button in self.listeButton :
            button.render()
>>>>>>> 39bc9e86436749760d6a983e95009cfff268a466
            
        self.eventManager.render(self.screen)
        self.towerManager.render(self.screen)
        self.money.render(self.screen)

        pygame.display.update()

    def stop(self):
        GameManager.running = False

    def BindButton(self, index:int, function):
        self.listeButton[index].bind(function)