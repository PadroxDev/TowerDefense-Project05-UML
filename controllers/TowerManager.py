import Button
from pygame.math import Vector2
from pygame.rect import Rect
from models.Towers.Tower import Tower
import pygame

class TowerManager:
    def __init__(self) -> None:
        TowerManager.towersList = []

    def CheckIfBuildable(self, mousePos: Vector2):
        mousePos = pygame.mouse.get_pos()
        for tower in TowerManager.towersList:
            distance = (tower.position - mousePos).magnitude()
            if(distance <= 50):
                return False
        self.BuildTurret(mousePos)
    
    def BuildTurret(self, mousePos: Vector2):
        mousePos = pygame.mouse.get_pos()
        Button("res/sprites/button/button_sprite_test.png", Rect(mousePos.x, mousePos.y, 200, 200))
        TowerManager.towersList.append()
        
