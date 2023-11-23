from models.Enemies.Enemy import Enemy
from pygame.math import Vector2
from pygame import Surface
from pygame.image import load
import pygame.draw as draw
from pygame import Color

class Piggy(Enemy):
    hp = 150
    speed = 100
    dropMoney = 10
    PiggySprite = "res/sprites/enemies/piggy.png"

    def __init__(self, pos: Vector2) -> None:
        super().__init__(pos, Piggy.hp, Piggy.speed, Piggy.dropMoney, 1)
        self.image = load(self.PiggySprite).convert_alpha()

    def render(self, surf: Surface):
<<<<<<< HEAD
        surf.blit(self.image, self.position - Vector2(1, 1) * 125)
=======
        surf.blit(self.image, self.position - Vector2(1, 1) * 288 * 0.5)
>>>>>>> 39bc9e86436749760d6a983e95009cfff268a466
