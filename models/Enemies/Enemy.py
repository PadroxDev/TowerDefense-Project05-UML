from pygame.math import Vector2

class Enemy:
    def __init__(self, pos: Vector2, hp: int, speed: int, dropMoney: int):
        self.position = pos
        self.hp = hp
        self.speed = speed
        self.dropMoney = dropMoney

    def move(self, dT):
        pass

    def takeDamage(self, damage):
        self.hp -= damage
