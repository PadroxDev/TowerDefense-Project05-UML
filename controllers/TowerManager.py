from controllers.Button import Button
from pygame.math import Vector2
from pygame.rect import Rect
from models.Towers.Lancer import LancerI
import pygame

class TowerManager:
    def __init__(self) -> None:
        TowerManager.towersList = []

    def CheckIfBuildable(self):
        mousePos = pygame.mouse.get_pos()
        for tower in TowerManager.towersList:
            distance = (tower.position - mousePos).magnitude()
            if(distance <= 50):
                return False
        self.BuildTurret(mousePos)
    
    def BuildTurret(self, mousePos: Vector2):
        mousePos = pygame.mouse.get_pos()
        #Button("res/sprites/button/button_sprite_test.png", Rect(mousePos.x, mousePos.y, 200, 200))
        lancer = LancerI(mousePos - Vector2(1,1)*256*0.5)
        TowerManager.towersList.append(lancer)

    def update(self, dT):
        for tower in self.towersList:
            tower.update(dT)

    def render(self):
        for tower in self.towersList:
            tower.render()
        
