from models.Towers.Tower import TowerBase, TargetMode
import pygame
from pygame.math import Vector2
from models.Enemies.Enemy import Enemy
import pygame.draw as draw
import pygame.image as img
from pygame import Surface

class ArcherI(TowerBase):
    Price = 400
    Range = 400
    Damage = 20.0
    ASP = 0.6
    TargetMode = TargetMode.Nearest
    SpritePath = "res/sprites/towers/Archer.png"

    def __init__(self, position: Vector2):
        super().__init__(position, self.Price, self.Range, self.Damage, self.ASP, self.TargetMode, 0)
        self.image = img.load(self.SpritePath).convert_alpha()
        self.resizeImage()

    def attack(self, target:Enemy, enemies: list):
        target.takeDamage(self.Damage)