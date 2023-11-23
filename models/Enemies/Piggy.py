from models.Enemies.Enemy import Enemy
from pygame.math import Vector2
from pygame import Surface
from pygame.image import load

class Piggy(Enemy):
    hp = 150
    speed = 50
    dropMoney = 10
    PiggySprite = "res/sprites/enemies/piggy.webp"

    def __init__(self, pos: Vector2) -> None:
        super().__init__(pos, Piggy.hp, Piggy.speed, Piggy.dropMoney, 1)
        self.image = load(self.PiggySprite).convert_alpha()

    def render(self, surf: Surface):
        surf.blit(self.image, self.position)