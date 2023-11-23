from controllers.Button import Button
from pygame.math import Vector2
from pygame.rect import Rect
from models.Towers.Golem import GolemI
from models.Towers.Archer import ArcherI
from models.Towers.Wizard import WizardI
import pygame

class TowerManager:
    def __init__(self) -> None:
        TowerManager.towersList = []
        self.baka = 1

    def CheckIfBuildable(self):
        mousePos: Vector2 = pygame.mouse.get_pos()
        for tower in TowerManager.towersList:
            distance = (tower.position - Vector2(mousePos)).magnitude()
            if(distance <= 130):
                return False
        self.BuildTurret(mousePos)
    

    def BuildTurret(self, mousePos: Vector2):
        mousePos = pygame.mouse.get_pos()
        unit = None
        archer = ArcherI(mousePos)
        wizard = WizardI(mousePos)
        if(self.baka % 3 == 0):
            unit = GolemI(mousePos)
        elif(self.baka % 3 == 1):
            unit = ArcherI(mousePos)
        elif(self.baka % 3 == 2):
            unit = WizardI(mousePos)
        self.baka += 1
        TowerManager.towersList.append(unit)

    def update(self, dT, enemies):
        for tower in self.towersList:
            tower.update(dT, enemies)

    def render(self, surf: pygame.Surface):
        for tower in self.towersList:
            tower.render(surf)
        
