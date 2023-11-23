from controllers.Button import Button
from pygame.math import Vector2
from pygame.rect import Rect
from models.Towers.Lancer import LancerI
from models.Towers.Archer import ArcherI
from models.Towers.Wizard import WizardI
import pygame

class TowerManager:
    def __init__(self) -> None:
        TowerManager.towersList = []

    def CheckIfBuildable(self):
        mousePos: Vector2 = pygame.mouse.get_pos()
        for tower in TowerManager.towersList:
            distance = (tower.position - Vector2(mousePos)).magnitude()
            if(distance <= 256):
                return False
        self.BuildTurret(mousePos)
    
    def BuildTurret(self, mousePos: Vector2):
        mousePos = pygame.mouse.get_pos()
        lancer = LancerI(mousePos - Vector2(1,1)*256*0.5)
        archer = ArcherI(mousePos - Vector2(1,1)*256*0.5)
        wizard = WizardI(mousePos - Vector2(1,1)*256*0.5)
        TowerManager.towersList.append(archer)

    def update(self, dT, enemies):
        for tower in self.towersList:
            tower.update(dT, enemies)

    def render(self, surf: pygame.Surface):
        for tower in self.towersList:
            tower.render(surf)
        
