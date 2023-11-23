from enum import Enum
from models.Enemies.Enemy import Enemy
from pygame.math import Vector2

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

    def canAttack(self):
        return self.attackDebounce >= self.asp

    def update(self, dT: float, enemies: list):
        self.attackDebounce += dT
        target: Enemy = self.findTarget(enemies)
        if(self.canAttack() and target is not None):
            self.attackDebounce -= self.asp
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

    def render(self):
        print("Render method wasn't overrided !")

    def upgrade(self):
        pass