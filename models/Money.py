from models.Text import Text
import pygame
from models.constants import BLACK
from pygame import Surface
from pygame.math import Vector2

class Money:
    def __init__(self, money: int) -> None:
        self.money = money

    def addMoney(self, money: int):
        self.money += money

    def removeMoney(self, money: int):
        self.money -= money

    def update(self):
        self.moneyText = Text("Money: " + str(self.money), pygame.Rect(10, 645, 500, 250), 50, BLACK)

    def render(self, surf: Surface):
        self.moneyText.render(surf)