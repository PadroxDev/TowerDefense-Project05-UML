from models.Enemies.Enemy import Enemy
import pygame
from pygame.math import Vector2
from pygame import Surface
from pygame.image import load

class Iris(Enemy):
    hp = 600
    speed = 40
    dropMoney = 200
    Iris = "res/sprites/enemies/iris.png"
    def __init__(self, pos: Vector2):
        super().__init__(pos, Iris.hp, Iris.speed, Iris.dropMoney, 1)
        self.image = load(self.Iris).convert_alpha()
        self.image = pygame.transform.scale(self.image, (250, 250))
        self.image = pygame.transform.flip(self.image, True, False)
    
    def render(self, surf: Surface):
        super().render(surf)
        surf.blit(self.image, self.position - Vector2(1, 1) * 125)