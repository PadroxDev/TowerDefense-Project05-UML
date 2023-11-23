from models.Enemies.Enemy import Enemy
import pygame
from pygame.math import Vector2
from pygame import Surface
from pygame.image import load

class PigKnight(Enemy):
    hp = 400
    speed = 45
    dropMoney = 25
    PigKnightSprite = "res/sprites/enemies/pigknight.png"
    def __init__(self, pos: Vector2):
        super().__init__(pos, PigKnight.hp, PigKnight.speed, PigKnight.dropMoney, 1)
        self.image = load(self.PigKnightSprite).convert_alpha()
        self.image = pygame.transform.scale(self.image, (250, 250))

    
    def render(self, surf: Surface):
        surf.blit(self.image, self.position - Vector2(1, 1) * 125)