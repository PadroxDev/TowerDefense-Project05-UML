from models.Towers.Tower import TowerBase, TargetMode
import pygame
from pygame.math import Vector2
from models.Enemies.Enemy import Enemy
import pygame.draw as draw
import pygame.image as img
from pygame import Surface

class ArcherI(TowerBase):
    Price = 400
    Range = 600.0
    Damage = 20.0
    ASP = 0.25
    TargetMode = TargetMode.Nearest
<<<<<<< HEAD
    SpritePath = "res/sprites/towers/Archer.png"
=======
    SpritePath = "res/sprites/towers/archer.png"
>>>>>>> 39bc9e86436749760d6a983e95009cfff268a466

    def __init__(self, position: Vector2):
        super().__init__(position, self.Price, self.Range, self.Damage, self.ASP, self.TargetMode, 0)
        self.normalImage = img.load(self.SpritePath).convert_alpha()
        self.redImage = img.load(self.SpritePath).convert_alpha()
        self.currentImage = self.normalImage
        self.imageRect = self.normalImage.get_rect()

    def attack(self, target:Enemy, enemies: list):
        target.takeDamage(self.Damage)
