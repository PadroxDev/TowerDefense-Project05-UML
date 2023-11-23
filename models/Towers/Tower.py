from enum import Enum
from models.Enemies.Enemy import Enemy
from pygame.math import Vector2
from pygame import Surface, Color
import pygame.draw as draw
import pygame.transform as ouryel

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
        
    def resizeImage(self):
        self.image = ouryel.scale(self.image, Vector2(1, 1) * 200)

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