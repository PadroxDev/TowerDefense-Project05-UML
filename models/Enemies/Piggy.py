from Enemies.Enemy import Enemy
from pygame.math import Vector2

class Piggy(Enemy):
    hp = 150
    speed = 50
    dropMoney = 10
    def __init__(self, pos: Vector2) -> None:
        super().__init__(pos, Piggy.hp, Piggy.speed, Piggy.dropMoney)