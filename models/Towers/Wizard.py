from models.Towers.Tower import TowerBase, TargetMode
from pygame.math import Vector2
from models.Enemies.Enemy import Enemy
import pygame.draw as draw
import pygame.image as img
from pygame import Surface, Color

class WizardI(TowerBase):
    Price = 550
    Range = 275.0
    Damage = 20.0
    ASP = 3
    TargetMode = TargetMode.Nearest
    SpritePath = "res/sprites/towers/Wizard.png"
    AOERange = 120

    def __init__(self, position: Vector2):
        super().__init__(position, self.Price, self.Range, self.Damage, self.ASP, self.TargetMode, 0)
        self.image = img.load(self.SpritePath).convert_alpha()
        self.resizeImage()
        self.impactPos = Vector2(0, 0)

    def attack(self, target:Enemy, enemies: list):
        self.impactPos = target.position
        for enemy in enemies:
            distance = (enemy.position - self.position).magnitude()
            if(distance <= self.AOERange):
                enemy.takeDamage(self.damage)
        target.takeDamage(self.damage)

    def render(self, surf):
        super().render(surf)
        draw.circle(surf, Color(100, 100, 255), self.impactPos, self.AOERange, 3)