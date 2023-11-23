import pygame
from models.Money import Money

class PlayerManager:
    def __init__(self):
        self.hp = 3
        self.money = Money(450)

    def setLife(self, hp):
        self.hp = hp

    def takeDamage(self, damage):
        self.hp -= damage
    
    def healPlayer(self, heal):
        self.takeDamage(-(heal))

    def removeMoney(self, money : int):
        self.money.removeMoney(money)

    def addMoney(self, money : int):
        self.money.addMoney(money)