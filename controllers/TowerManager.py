from controllers.Button import Button
from pygame.math import Vector2
from pygame.rect import Rect
from models.Towers.Golem import GolemI
from models.Towers.Archer import ArcherI
from models.Towers.Wizard import WizardI
from models.Text import Text
import pygame

class TowerManager:
    def __init__(self, player) -> None:
    #def __init__(self, money: int) -> None:
        TowerManager.towersList = []
        TowerManager.player = player
        TowerManager.towersListTemp = []

        TowerManager.notEnoughMoneyMessage = None
        TowerManager.displayMoneyMessageTimer = 0
        TowerManager.notEnoughMoneyMessage = Text("Cannot build this tower !", Rect(1280 * 0.35 , 720-100, 1280 * 0.5, 100), 35, pygame.Color(255, 80, 80))

        TowerManager.buttonList = []
        TowerManager.buttonList.append(Button("res/sprites/button/cross.png", Rect(890, 600, 80, 80)))
        TowerManager.buttonList[0].bind(self.cancelTurret)

    def CheckIfBuildable(self, turret ):
        mousePos: Vector2 = pygame.mouse.get_pos()
        if (turret.price > TowerManager.player.money.money):
            return False
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
            tower.updatePosition()
            self.updateColor()
        
        if len(TowerManager.towersListTemp) != 0 :
            TowerManager.buttonList[0].update()

    def render(self, surf: pygame.Surface):
        if (self.displayMoneyMessageTimer > 0):
            self.notEnoughMoneyMessage.render(surf)

        for tower in self.towersList:
            tower.render(surf)
        
        for tower in self.towersListTemp:
            tower.renderRange(surf)
            tower.render(surf)

        if len(TowerManager.towersListTemp) != 0:
            TowerManager.buttonList[0].render()

    def PlaceHighlightLancer(self):
        TowerManager.towersListTemp[0].setOpacity(100)
        TowerManager.towersListTemp[0].SetRedimage()

    def createTurret(self):
        
        if len(TowerManager.towersListTemp) != 0 :
            TowerManager.buttonList[0].update()
        if len(TowerManager.towersListTemp) != 0 :
            if(self.CheckIfBuildable(TowerManager.towersListTemp[0])):
                print(TowerManager.towersListTemp[0].price)
                TowerManager.towersList.append(TowerManager.towersListTemp[0])
                TowerManager.towersList[-1].setOpacity(255)
                TowerManager.player.removeMoney(TowerManager.towersListTemp[0].price)
                
                TowerManager.towersListTemp.clear()
            else:
                self.displayMoneyMessageTimer = 2
      
    def updateColor(self):
        if len(TowerManager.towersListTemp) != 0 :
            if(self.CheckIfBuildable(TowerManager.towersListTemp[0])):
                TowerManager.towersListTemp[0].changeNormal()
            else:
                TowerManager.towersListTemp[0].changeRed()

    def createGolem(self):
        if(len(self.towersListTemp)==0):
            TowerManager.towersListTemp.append(GolemI(Vector2(1,1)))
            self.PlaceHighlightLancer()
    
    def createArcher(self):
        if(len(self.towersListTemp)==0):
            TowerManager.towersListTemp.append(ArcherI(Vector2(1,1)))
            self.PlaceHighlightLancer()

    def createWizard(self):
        if(len(self.towersListTemp)==0):
            TowerManager.towersListTemp.append(WizardI(Vector2(1,1)))
            self.PlaceHighlightLancer()

    def cancelTurret(self):
        TowerManager.towersListTemp.clear()
        
