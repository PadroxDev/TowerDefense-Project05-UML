import pygame
from models.Money import Money
from view.Loose import LooseScreen

class PlayerManager:
    def __init__(self):
        self.maxHealth = 1000
        self.hp = self.maxHealth
        self.money = Money(550)

    def setLife(self, hp):
        self.hp = hp

    # Return if dead
    def takeDamage(self, damage):
        self.hp -= damage
        if(self.hp <= 0):
            LooseScreen(pygame.display.get_surface()).run()
    
    def healPlayer(self, heal):
        self.takeDamage(-(heal))

    def removeMoney(self, money : int):
        self.money.removeMoney(money)

    def addMoney(self, money : int):
        self.money.addMoney(money)