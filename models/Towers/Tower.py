from enum import Enum
from models.Enemies.Enemy import Enemy
from pygame.math import Vector2
from pygame import Surface, Color
import pygame.draw as draw
import pygame.transform as ouryel
import pygame.mouse as mouse

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

    def resizeImage(self):
        self.currentImage = ouryel.scale(self.currentImage, Vector2(1, 1) * 200)

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
        print("Attack Method wasn't overrided !")

    def render(self, surf: Surface):
        draw.circle(surf, Color(255, 255, 255, 30), self.position, self.range, 2)
        surf.blit(self.image, self.position - Vector2(1, 1) * 200 * 0.5)

    def upgrade(self):
        pass

    def render(self, surf: Surface):
        surf.blit(self.currentImage, self.position)

    def SetRedimage(self):
        for x in range(self.currentImage.get_width()):
            for y in range(self.currentImage.get_height()):
                pixel_color = self.currentImage.get_at((x, y))
                # Appliquer le filtre rouge en augmentant la composante rouge
                new_color = (min(pixel_color[0] + 100, 255), pixel_color[1], pixel_color[2])
                self.redImage.set_at((x, y), new_color)
    
    def changeRed(self):
        self.currentImage = self.redImage
    
    def changeNormal(self):
        self.currentImage = self.normalImage

    def setOpacity(self, alpha : int):
        self.currentImage.set_alpha(alpha)

    def updatePosition(self):
        mousePos = mouse.get_pos()
        self.position = Vector2(mousePos[0]-(self.imageRect.w//2) ,mousePos[1] - (self.imageRect.h//2))
