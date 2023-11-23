from models.Towers.Tower import TowerBase, TargetMode
from pygame.math import Vector2
from models.Enemies.Enemy import Enemy
import pygame.draw as draw
import pygame.image as img
from pygame import Surface

class WizardI(TowerBase):
    Price = 550
    Range = 400.0
    Damage = 20.0
    ASP = 0.5
    TargetMode = TargetMode.Nearest
    SpritePath = "res/sprites/towers/wizard.webp"

    def __init__(self, position: Vector2):
        super().__init__(position, self.Price, self.Range, self.Damage, self.ASP, self.TargetMode, 0)
        self.image = img.load(self.SpritePath).convert_alpha()

    def attack(self, target:Enemy, enemies: list):
        target.takeDamage(self.Damage)

    def render(self, surf: Surface):
        surf.blit(self.image, self.position)
