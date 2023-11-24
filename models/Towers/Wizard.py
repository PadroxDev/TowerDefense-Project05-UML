from models.Towers.Tower import TowerBase, TargetMode
from pygame.math import Vector2
from models.Enemies.Enemy import Enemy
import pygame.draw as draw
import pygame.image as img
from pygame import Surface, Color

class WizardI(TowerBase):
    Price = 650
    Range = 300
    Damage = 40
    ASP = 1.7
    TargetMode = TargetMode.Nearest
    SpritePath = "res/sprites/towers/Wizard.png"
    AOERange = 120

    def __init__(self, position: Vector2):
        super().__init__(position, self.Price, self.Range, self.Damage, self.ASP, self.TargetMode, 0)
        self.normalImage = img.load(self.SpritePath).convert_alpha()
        self.impactPos = Vector2(0, 0)
        self.redImage = img.load(self.SpritePath).convert_alpha()
        self.currentImage = self.normalImage
        self.imageRect = self.normalImage.get_rect()
        self.resizeImage()

    def attack(self, target:Enemy, enemies: list):
        super().attack(target)
        self.impactPos = target.position
        for enemy in enemies:
            distance = (enemy.position - self.impactPos).magnitude()
            if(distance <= self.AOERange):
                enemy.takeDamage(self.damage)
        target.takeDamage(self.damage)

    def render(self, surf):
        super().render(surf)
        draw.circle(surf, Color(100, 100, 255), self.impactPos, self.AOERange, 3)