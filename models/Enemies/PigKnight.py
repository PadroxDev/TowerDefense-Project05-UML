from Enemies.Enemy import Enemy
from pygame.math import Vector2

class PigKnight(Enemy):
    hp = 400
    speed = 25
    dropMoney = 25
    def __init__(self, pos: Vector2):
        super().__init__(pos, PigKnight.hp, PigKnight.speed, PigKnight.dropMoney)