from models.Enemies.Enemy import Enemy
from pygame.math import Vector2
from pygame import Surface
from pygame.image import load
import pygame.draw as draw
from pygame import Color
import pygame

class Piggy(Enemy):
    hp = 60
    speed = 175
    dropMoney = 35
    PiggySprite = "res/sprites/enemies/piggy.png"

    def __init__(self, pos: Vector2) -> None:
        super().__init__(pos, Piggy.hp, Piggy.speed, Piggy.dropMoney, 1)
        self.image = load(self.PiggySprite).convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.image = pygame.transform.flip(self.image, True, False)

    def render(self, surf: Surface):
        super().render(surf)
        surf.blit(self.image, self.position - Vector2(1, 1) * 100)
