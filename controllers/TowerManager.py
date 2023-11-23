from controllers.Button import Button
from pygame.math import Vector2
from pygame.rect import Rect
from models.Towers.Golem import GolemI
from models.Towers.Archer import ArcherI
from models.Towers.Wizard import WizardI
import pygame

class TowerManager:
    def __init__(self, player) -> None:
    #def __init__(self, money: int) -> None:
        TowerManager.towersList = []
        TowerManager.player = player
        TowerManager.towersListTemp = []

        TowerManager.buttonList = []
        TowerManager.buttonList.append(Button("res/sprites/button/cross.png", Rect(890, 600, 80, 80)))
        TowerManager.buttonList[0].bind(self.cancelTurret)

    def CheckIfBuildable(self, turret ):
        mousePos: Vector2 = pygame.mouse.get_pos()
        for tower in TowerManager.towersList:
            distance = (tower.position - Vector2(mousePos)).magnitude()
            if(distance <= 130):
                return False
        if (turret.price > TowerManager.player.money.money):
            return False
        return True

    # def BuildTurret(self, mousePos: Vector2):
    #     mousePos = pygame.mouse.get_pos()
    #     unit = None
    #     archer = ArcherI(mousePos)
    #     wizard = WizardI(mousePos)
    #     TowerManager.towersList.append(lancer)

    def update(self, dT, enemies):
        for tower in self.towersList:
            tower.update(dT, enemies)
        
        for tower in self.towersListTemp:
            tower.updatePosition()
            self.updateColor()
        
        if len(TowerManager.towersListTemp) != 0 :
            TowerManager.buttonList[0].update()

    def render(self, surf: pygame.Surface):
        for tower in self.towersList:
            tower.render(surf)
        
        for tower in self.towersListTemp:
            tower.render(surf)

        if len(TowerManager.towersListTemp) != 0:
            TowerManager.buttonList[0].render()


    #Code relatif au placement d'une tourelle en transparence

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
        
