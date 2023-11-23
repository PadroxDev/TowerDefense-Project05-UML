from models.Towers.Tower import TowerBase, TargetMode
from pygame.math import Vector2
from models.Enemies.Enemy import Enemy
import pygame.draw as draw
import pygame.image as img
from pygame import Surface, Color
import math
from enum import Enum

class States(Enum):
    SearchingForTarget = 1
    Attack = 2
    Recovering = 3

class GolemI(TowerBase):
    Price = 650
    Range = 150.0
    Damage = 20.0
    ASP = 1.5
    TargetMode = TargetMode.Nearest
    SpritePath = "res/sprites/towers/Golem.png"

    def __init__(self, position: Vector2):
        super().__init__(position, self.Price, self.Range, self.Damage, self.ASP, self.TargetMode, 0)
        self.normalImage = img.load(self.SpritePath).convert_alpha()
        self.angle = 0
        self.dir = Vector2(0, 0)
        self.currentTarget = States.SearchingForTarget
        self.resizeImage()
        self.redImage = img.load(self.SpritePath).convert_alpha()
        self.currentImage = self.normalImage
        self.imageRect = self.normalImage.get_rect()

    def attack(self, target:Enemy, enemies: list):
        dir: Vector2 = (target.position - self.position)
        if(dir != Vector2(0,0)): dir = dir.normalize()
        self.dir = dir.copy()
        self.angle = math.degrees(math.atan2(dir.y, dir.x))
        target.takeDamage(self.Damage)

