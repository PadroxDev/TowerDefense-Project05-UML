from models.Enemies.Enemy import Enemy
import pygame
from pygame.math import Vector2
from pygame import Surface
from pygame.image import load

class Iris(Enemy):
    hp = 600
    speed = 15
    dropMoney = 50
    Iris = "res/sprites/enemies/Iris.png"
    def __init__(self, pos: Vector2):
        super().__init__(pos, Iris.hp, Iris.speed, Iris.dropMoney, 1)
        self.image = load(self.Iris).convert_alpha()
        self.image = pygame.transform.scale(self.image, (250, 250))
    
    def render(self, surf: Surface):
        surf.blit(self.image, self.position - Vector2(1, 1) * 125)