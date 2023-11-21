import pygame

class PlayerManager:
    def stats(self):
        self.hp = 3
        self.money

    def setLife(self, hp):
        self.hp = hp

    def takeDamage(self, damage):
        self.hp -= damage
    
    def healPlayer(self, heal):
        self.takeDamage(-(heal))