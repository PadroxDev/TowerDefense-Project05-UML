from Enemies.Enemy import Enemy
from pygame.math import Vector2

class Iris(Enemy):
    hp = 600
    speed = 10
    dropMoney = 50
    def __init__(self, pos: Vector2):
        super().__init__(pos, Iris.hp, Iris.speed, Iris.dropMoney)