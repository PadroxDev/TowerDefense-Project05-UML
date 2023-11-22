from models.Towers.Tower import TowerBase, TargetMode
from pygame.math import Vector2
from models.Enemies.Enemy import Enemy
import pygame.draw as draw
import pygame.image as img
from pygame import Surface

class LancerI(TowerBase):
    Price = 650
    Range = 300.0
    Damage = 20.0
    ASP = 0.75
    TargetMode = TargetMode.Nearest
    SpritePath = "res/sprites/towers/LancerI.gif"

    def __init__(self, position: Vector2):
        super().__init__(position, self.Price, self.Range, self.Damage, self.ASP, self.TargetMode, 0)
        self.image = img.load(self.SpritePath).convert_alpha()

    def attack(self, enemies: list):
        target: Enemy = self.findTarget(enemies)
        target.takeDamage(self.Damage)

    def render(self, surf: Surface):
        surf.blit(self.image, self.position)
