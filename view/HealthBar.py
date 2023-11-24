from pygame import Rect, Color, Surface
from pygame.math import Vector2, clamp
import pygame.draw as draw
from models.Text import Text

BACKGROUND_COLOR = Color(173, 173, 173)
BORDER_COLOR = Color(255, 255, 255)
LOW_COLOR = Color(255, 0, 0)
FULL_COLOR = Color(0, 200, 0)

class HealthBar:
    def __init__(self, position: Vector2, size: Vector2, borderSize: float = 8):
        self.position = position
        self.size = size
        self.health = 0
        self.maxHealth = 0
        self.borderSize = borderSize

    def update(self, health: float, maxHealth: float):
        self.health = health
        self.maxHealth = maxHealth

    def render(self, surf: Surface):
        rect: Rect = Rect(self.position, self.size)
        draw.rect(surf, BACKGROUND_COLOR, rect)
        draw.rect(surf, BORDER_COLOR, rect, self.borderSize)
        alpha = clamp(self.health / self.maxHealth, 0, 1)
        healthColor = Color.lerp(LOW_COLOR, FULL_COLOR, alpha)
        innerRect = Rect(rect.x + self.borderSize, rect.y + self.borderSize, rect.w * alpha - self.borderSize * 2, rect.h - self.borderSize * 2)
        draw.rect(surf, healthColor, innerRect)