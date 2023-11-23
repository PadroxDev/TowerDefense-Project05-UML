from enum import Enum
from models.Enemies.Enemy import Enemy
from pygame.math import Vector2
from pygame import Surface, Color, BLEND_ADD
import pygame.draw as draw
import pygame.transform as ouryel
import pygame.mouse as mouse
import math

class TargetMode(Enum):
    First = 1
    Last = 2
    Strongest = 3
    Weakest = 4
    Nearest = 5
    Furthest = 6

class TowerBase:
    def __init__(self, position: Vector2, price: int, range: float, damage: float, asp: float, targetMode: TargetMode, level: int):
        self.position = position
        self.price = price
        self.range = range
        self.damage = damage
        self.asp = asp
        self.targetMode = targetMode
        self.level = level
        self.attackDebounce = asp
        self.currentImage : Surface
        self.normalImage : Surface
        self.redImage : Surface
        self.angle = 180

    def resizeImage(self):
        self.currentImage = ouryel.scale(self.currentImage, Vector2(1, 1) * 200)
        self.normalImage = ouryel.scale(self.normalImage, Vector2(1, 1) * 200)
        self.redImage = ouryel.scale(self.redImage, Vector2(1, 1) * 200)

    def canAttack(self):
        return self.attackDebounce >= self.asp

    def update(self, dT: float, enemies: list):
        self.attackDebounce += dT
        target: Enemy = self.findTarget(enemies)
        if(self.canAttack() and target is not None):
            self.attackDebounce = 0
            self.attack(target, enemies)

    def findTarget(self, enemies: list):
        nearestTarget = None
        targetDistance = self.range + 1
        for enemy in enemies:
            distance = (enemy.position - self.position).magnitude()
            if(distance > self.range and distance >= targetDistance): continue

            nearestTarget = enemy
            targetDistance = distance
        
        return nearestTarget

    def attack(self, target: Enemy):
        dir: Vector2 = (target.position - self.position)
        if(dir != Vector2(0,0)): dir = dir.normalize()
        self.dir = dir.copy()
        self.angle = math.degrees(math.atan2(dir.y, dir.x))

    def upgrade(self):
        pass

    def render(self, surf: Surface):
        rotatedImage = ouryel.rotate(self.currentImage, self.angle)
        surf.blit(rotatedImage, self.position - Vector2(1, 1) * 200 * 0.5)

    def SetRedimage(self):
        self.redImage.fill(Color(255, 0, 0), None, BLEND_ADD)
    
    def changeRed(self):
        self.currentImage = self.redImage
    
    def changeNormal(self):
        self.currentImage = self.normalImage

    def setOpacity(self, alpha : int):
        self.currentImage.set_alpha(alpha)

    def updatePosition(self):
        mousePos = mouse.get_pos()
        self.position = mousePos
