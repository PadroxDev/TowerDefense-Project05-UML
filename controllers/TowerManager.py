from controllers.Button import Button
from pygame.math import Vector2
from pygame.rect import Rect
from models.Towers.Golem import GolemI
from models.Towers.Archer import ArcherI
from models.Towers.Wizard import WizardI
from models.Text import Text
import pygame

class TowerManager:
    def __init__(self, money: int) -> None:
        TowerManager.towersList = []
        self.money = money
        TowerManager.towersListTemp = []
        self.notEnoughMoneyMessage = None
        self.displayMoneyMessageTimer = 0
        self.notEnoughMoneyMessage = Text("Not enough money !", Rect(100, 200, 300, 100), 18, pygame.Color(185, 30, 30))

    def CheckIfBuildable(self):
        mousePos: Vector2 = pygame.mouse.get_pos()
        for tower in TowerManager.towersList:
            distance = (tower.position - Vector2(mousePos)).magnitude()
            if(distance <= 150):
                return False
        return True

    def update(self, dT, enemies):
        self.displayMoneyMessageTimer -= dT

        for tower in self.towersList:
            tower.update(dT, enemies)
        
        for tower in self.towersListTemp:
            tower.update(dT, enemies)
            tower.updatePosition()
            self.updateColor()

    def render(self, surf: pygame.Surface):
        if (self.displayMoneyMessageTimer > 0):
            self.notEnoughMoneyMessage.render(surf)

        for tower in self.towersList:
            tower.render(surf)
        
        for tower in self.towersListTemp:
            tower.render(surf)

    def PlaceHighlightLancer(self):
        TowerManager.towersListTemp[0].setOpacity(100)
        TowerManager.towersListTemp[0].SetRedimage()

    def createTurret(self):
        if(self.CheckIfBuildable() and len(TowerManager.towersListTemp) != 0):
            TowerManager.towersList.append(TowerManager.towersListTemp[0])
            TowerManager.towersList[-1].setOpacity(255)
            TowerManager.towersListTemp.pop()

    def updateColor(self):
        if(self.CheckIfBuildable()):
            TowerManager.towersListTemp[0].changeNormal()
        else:
            TowerManager.towersListTemp[0].changeRed()

    def createGolem(self):
        if(len(self.towersListTemp)==0):
            if(self.money.getMoney() >= GolemI.Price):
                TowerManager.towersListTemp.append(GolemI(Vector2(1,1)))
                self.PlaceHighlightLancer()
                self.money.removeMoney(GolemI.Price)
            else:
                self.displayMoneyMessageTimer = 2
                self.notEnoughMoneyMessage.setContent("Not enough money to buy an Golem !")
    
    def createArcher(self):
        if(len(self.towersListTemp)==0):
            if(self.money.getMoney() >= ArcherI.Price):
                TowerManager.towersListTemp.append(ArcherI(Vector2(1,1)))
                self.PlaceHighlightLancer()
                self.money.removeMoney(ArcherI.Price)
            else:
                self.displayMoneyMessageTimer = 2
                self.notEnoughMoneyMessage.setContent("Not enough money to buy an Archer !")

    def createWizard(self):
        if(len(self.towersListTemp)==0):
            if(self.money.getMoney() >= WizardI.Price):
                TowerManager.towersListTemp.append(WizardI(Vector2(1,1)))
                self.PlaceHighlightLancer()
                self.money.removeMoney(WizardI.Price)
            else:
                self.notEnoughMoneyMessage.setContent("Not enough money to buy a Wizard !")
                self.displayMoneyMessageTimer = 2
