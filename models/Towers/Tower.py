from enum import Enum
from models.Enemies.Enemy import Enemy
from pygame.math import Vector2

class TargetMode(Enum):
    First = 1
    Last = 2
    Strongest = 3
    Weakest = 4

class Tower:
    def __init__(self, position: Vector2, price: int, range: float, damage: float, asp: float, targetMode: TargetMode, level: int):
        self.position = position
        self.price = price
        self.range = range
        self.damage = damage
        self.asp = asp
        self.targetMode = targetMode
        self.level = level

    def attack(self, target: Enemy):
        pass

    def findTarget(self):
        pass

    def upgrade(self):
        pass