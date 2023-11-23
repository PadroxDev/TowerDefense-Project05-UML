from controllers.Button import Button
from pygame.math import Vector2
from pygame.rect import Rect
from models.Towers.Golem import GolemI
from models.Towers.Archer import ArcherI
from models.Towers.Wizard import WizardI
import pygame

class TowerManager:
    def __init__(self, money) -> None:
        TowerManager.towersList = []
        self.money = money
        TowerManager.towersListTemp = []

    def CheckIfBuildable(self):
        mousePos: Vector2 = pygame.mouse.get_pos()
        for tower in TowerManager.towersList:
            distance = (tower.position - Vector2(mousePos)).magnitude()
            if(distance <= 130):
                return False
        return True
        #self.BuildTurret(mousePos)
        
    def BuildTurret(self, mousePos: Vector2):
        mousePos = pygame.mouse.get_pos()
        lancer = GolemI(mousePos)
        archer = ArcherI(mousePos)
        wizard = WizardI(mousePos)
        TowerManager.towersList.append(lancer)
        self.money.removeMoney(lancer.price)
    # def BuildTurret(self, mousePos: Vector2):
    #     mousePos = pygame.mouse.get_pos()
    #     lancer = LancerI(mousePos - Vector2(1,1)*256*0.5)
    #     TowerManager.towersList.append(lancer)

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
            tower.update(dT, enemies)
            tower.updatePosition()
            self.updateColor()

    def render(self, surf: pygame.Surface):
        for tower in self.towersList:
            tower.render(surf)
        
        for tower in self.towersListTemp:
            tower.render(surf)

    #Code relatif au placement d'une tourelle en transparence

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
